from django.http import response
from django.test import TestCase, client
from django.urls import reverse
from .models import Invitation
from .forms import InvitationForm

from django.contrib.auth.models import User
class TestView(TestCase):
#SETUPDATA
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    
        Invitation.objects.create(owner=user, p_from="test",p_to="test1",place="test2",invitation_date="test3", description="test4", template="black", is_formal=False)



#TEST MODEL
    def test_should_show_invitation_fields(self):
        inv = Invitation.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(str(inv.p_from), "test")
        self.assertEqual(str(inv.p_to), "test1")
        self.assertEqual(str(inv.place), "test2")
        self.assertEqual(str(inv.invitation_date), "test3")
        self.assertEqual(str(inv.description), "test4")
        self.assertEqual(str(inv.template), "black")
        self.assertEqual(str(inv.is_formal), 'False')
        self.assertEqual(inv.owner, user)

#PAGE VIEW TEST
    def test_should_show_register_page(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/registration.html')

    def test_should_show_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
    
    def test_shoul_show_user_invitations_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("invitations"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['invitation_list'].all()[0].owner), "john")
""" 
    def test_should_generate_pdf(self):
        response = self.client.get(reverse("generator_form"))
        self.assertEqual(response.status_code, 200)
        form_data = {'p_from': 'as', 'p_to': 'dasd', 'place': 'asdasd', 'invitation_date': 'asdas', 'description': 'dasdasd', 'template': 'happy'}
        form = InvitationForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post("generator_form", form_data)
        self.assertEqual(response.status_code, 200)
    
"""

        