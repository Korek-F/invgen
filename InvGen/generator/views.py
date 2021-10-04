from django.shortcuts import get_list_or_404, redirect, render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from django.template.loader import render_to_string
from django.views.generic.detail import DetailView
from weasyprint import HTML, CSS
from .forms import InvitationForm, CustomTemplateForm,InvitationWithCustomForm
from .models import Invitation, CustomTemplate
from django.views.generic.list import ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import DeleteView, CreateView
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(View):
    def get(self, request):
        return render(request, "generator/home.html")

class GeneratorForm(View):
    def get(self, request):
        form = InvitationForm
        return render(request, "generator/generator_form.html", {'form': form})

    def post(self, request):
        form = InvitationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            if request.user.is_authenticated:
                invitation.owner = request.user
            invitation.save()
            return generate_pdf(request, invitation.id)
        return render(request, "generator/generator_form.html", {'form': form}) 
            

#function that creates a pdf from an id of invitation
def generate_pdf(request, inv_id, custom=False):
    invitation = Invitation.objects.all().get(id=inv_id)
    if invitation.owner:
        if not request.user == invitation.owner:
            return HttpResponseForbidden()

    if invitation.template_name:
        inv_template = invitation.template_name.docfile.url[1:]
    else:
        inv_template = 'static/css/templates/'+ str(invitation.template)+'_css.css'

    if not inv_template:
        inv_template = "black"
    html_string = render_to_string("generator/inv_templates/template.html", {"invitation": invitation})
    if custom: 
        print(custom)
        pdf_file = HTML(string=html_string).write_pdf(stylesheets=[CSS(str(custom[1:]))])
    else:
        pdf_file = HTML(string=html_string).write_pdf(stylesheets=[CSS(str(inv_template))])
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="invitation.pdf"'
    return response


class InvitationOwnerMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class ManageInvitationListView(LoginRequiredMixin, InvitationOwnerMixin, ListView):
    model = Invitation
    template_name = 'generator/invitation_list.html'

    
class UpdateInvitationView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'generator/update_invitation.html'
    invitation = None 

    def get_form(self, data=None):
        return InvitationForm(instance=self.invitation,data=data)

    def dispatch(self, request, pk):
        self.invitation =  get_object_or_404(Invitation, id=pk, owner=request.user)
        return super().dispatch(request, pk)

    def get(self, request, pk):
        form = self.get_form()
        return self.render_to_response({'invitation':self.invitation, 'form':form})
    
    def post(self, request, pk):
        form = self.get_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('invitations')
        return self.render_to_response({'invitation':self.invitation, 'form':form})

class InvitationDeleteView(DeleteView):
    model = Invitation
    success_url = reverse_lazy('invitations')


class CreateCustomTemplateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CustomTemplateForm
        return render(request, "generator/create_custom_template.html", {'form': form})

    def post(self, request):
        form = CustomTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            template = form.save(commit=False)
            template.owner = request.user
            template.save()
            return redirect("home")
        return render(request, "generator/generator_form.html", {'form': form})
    
class CustomTemplateListView(ListView):
    model = CustomTemplate
    template_name = 'generator/custom_template_list.html'

class CreateInvitationWithCustomTemplateView(View):
    def get(self, request, id):
        form = InvitationWithCustomForm
        custom_template = get_object_or_404(CustomTemplate, id=id)
        context={'form': form, "custom_template":custom_template}
        return render(request, "generator/generator_form_with_custom.html", context)
    
    def post(self, request, id):
        form = InvitationForm(data=request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            if request.user.is_authenticated:
                invitation.owner = request.user
            if request.POST["custom_template"]:
                template = get_object_or_404(CustomTemplate, id=request.POST["custom_template"])
                invitation.template_name = template
            invitation.save()
            return generate_pdf(request, invitation.id, invitation.template_name.docfile.url)
        return render(request, "generator/generator_form_with_custom.html", {'form': form})