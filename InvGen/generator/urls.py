from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('gen/<int:inv_id>', views.generate_pdf, name="gen"),
    path('generator_form', views.GeneratorForm.as_view(), name="generator_form"),
    path('invitations', views.ManageInvitationListView.as_view(), name="invitations"),
    path('invitations/update/<int:pk>', views.UpdateInvitationView.as_view(), name="invitation_update"),
    path('invitations/delete/<int:pk>', views.InvitationDeleteView.as_view(), name="invitation_delete"),
    path("customtemplate/create/", views.CreateCustomTemplateView.as_view(), name="customtemplate_create"),
    path('templates', views.CustomTemplateListView.as_view(), name="templates"),
    path('custom_generator/<int:id>', views.CreateInvitationWithCustomTemplateView.as_view(), name="custom_generator"),
]