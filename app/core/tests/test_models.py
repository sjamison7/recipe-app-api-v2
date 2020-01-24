from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@equinoxhealth.com'
        password = 'testequinox1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EQUINOXHEALTH.COM'
        user = get_user_model().objects.create_user(email, 'testequinox1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that a new user provides a valid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testequinox1234')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@equinoxhealth.com',
            'testequinox1234'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
