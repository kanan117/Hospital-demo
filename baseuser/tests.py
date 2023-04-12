from django.test import TestCase, Client
from django.urls import reverse
from baseuser.models import BaseUser
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from baseuser.forms import BaseUserForm


###register TEST
class BaseUserRegistrationTest(TestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')  
        self.user_data = {
            'username': 'testuser1111',
            'email': 'testuser@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
        }
        
    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, 'Register')
        
    def test_register_form(self):
        form = BaseUserForm(data=self.user_data)
        self.assertTrue(form.is_valid())
        
    def test_register_post_success(self):
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/', target_status_code=200)
        self.assertEqual(get_user_model().objects.count(), 1)

        
    def test_register_post_failure(self):
            # Test when passwords don't match
        self.user_data['password2'] = 'wrongpassword'
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The two password fields didn’t match.')
        self.assertEqual(get_user_model().objects.count(), 0)


####LOGIN UCUN
class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = BaseUser.objects.create_user(
            username='testuser1111',
            password='Testuser1111',

        )

    def test_login_view_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser1111', 'password': 'Testuser1111'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/')

    def test_login_view_failure(self):
        response = self.client.post(self.login_url, {'username': 'testuser1111', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password.")



# class ProfileEditTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user_data = {
#             'username': 'testuser1111',
#             'email': 'test@test.test',
#             'first_name': 'test',
#             'last_name': 'test',
#             'password': 'Testuser1111',
#         }
#         self.user = BaseUser.objects.create_user(**self.user_data)
#         self.login_url = reverse('login')
#         self.edit_profile_url = reverse('profile_edit')

#     def test_profile_edit_view_success(self):
#         self.client.login(username=self.user_data['username'], password=self.user_data['password'])
#         response = self.client.get(self.edit_profile_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profile_edit.html')

#     def test_profile_edit_form_success(self):
#         self.client.login(username=self.user_data['username'], password=self.user_data['password'])
#         response = self.client.post(self.edit_profile_url, {
#             'email': 'newemail@test.com',
#             'first_name': 'New',
#             'last_name': 'New ',
#         })
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('/en/'))
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.email, 'newemail@test.com')
#         self.assertEqual(self.user.first_name, 'New')
#         self.assertEqual(self.user.last_name, 'New')
    
    # def test_profile_edit_view_failure(self):
    #     response = self.client.get(self.edit_profile_url)
    #     self.assertRedirects(response, f"{self.login_url}?next={self.edit_profile_url}")
    #     response = self.client.post(self.edit_profile_url, {
    #         'email': '',
    #         'first_name': 'New First Name',
    #         'last_name': 'New Last Name',
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFormError(response, 'form', 'email', 'This field is required.')
    #     self.user.refresh_from_db()
    #     self.assertNotEqual(self.user.first_name, 'New First Name')
    #     self.assertNotEqual(self.user.last_name, 'New Last Name')


    # def test_delete_account_view(self):
    #     user = User.objects.create_user(**self.user)
    #     self.client.force_login(user)

    #     response = self.client.get(reverse('delete_account'))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'delete_account.html')

    #     data = {
    #         'password': 'testpassword',
    #         'confirm_delete': 'yes'
    #     }

    #     response = self.client.post(reverse('delete_account'), data)
    #     self.assertEquals(response.status_code, 302)
    #     self.assertRedirects(response, reverse('home'))

    #     self.assertEquals(User.objects.filter(username=user.username).count(), 0)
