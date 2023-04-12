from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from baseuser.forms import BaseUserForm
from .forms import LoginForm
from core.models import Setting


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword1',
            'password2': 'Testpassword1'
        }

    def test_register_view(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        form = response.context['form']
        self.assertIsInstance(form, BaseUserForm)

        data = self.user
        response = self.client.post(self.register_url, data)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        user = User.objects.get(username=data['username'])
        self.assertEquals(user.username, data['username'])
        self.assertEquals(user.email, data['email'])

    def test_login_view(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        form = response.context['form']
        self.assertIsInstance(form, LoginForm)

        user = User.objects.create_user(**self.user)
        response = self.client.post(self.login_url, self.user)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_profile_edit_view(self):
        user = User.objects.create_user(**self.user)
        self.client.force_login(user)

        response = self.client.get(reverse('profile_edit'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_edit.html')

        form = response.context['form']
        self.assertEquals(form.instance, user)

        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password': 'Newpassword1',
            'password2': 'Newpassword1'
        }

        response = self.client.post(reverse('profile_edit'), data)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        user.refresh_from_db()
        self.assertEquals(user.first_name, data['first_name'])
        self.assertEquals(user.last_name, data['last_name'])
        self.assertEquals(user.email, data['email'])

    def test_delete_account_view(self):
        user = User.objects.create_user(**self.user)
        self.client.force_login(user)

        response = self.client.get(reverse('delete_account'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_account.html')

        data = {
            'password': 'Newpassword1',
            'confirm_delete': 'yes'
        }

        response = self.client.post(reverse('delete_account'), data)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        self.assertEquals(User.objects.filter(username=user.username).count(), 0)
