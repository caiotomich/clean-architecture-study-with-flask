import unittest
from app.infrastructure.api.api import create_app, db
from app.infrastructure.api.models.users import User
from app.config.test import TestConfig
from app.domain.users.enums import UserErrorMessagesEnum
import json

class UserTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Clean up after tests"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user_with_empty_name(self):
        """Test creating a new user with empty name"""
        response = self.client.post('/users', json={
            "name": "",
            "email": "john.doe@example.com"
        })
        obj = json.loads(str(response.data.decode('utf-8')))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(obj['code'], 'USER_NAME_CANNOT_BE_EMPTY')

    def test_create_user_with_invalid_email(self):
        """Test creating a new user with invalid email"""
        response = self.client.post('/users', json={
            "name": "John Doe",
            "email": "john.doe@"
        })
        obj = json.loads(str(response.data.decode('utf-8')))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(obj['code'], 'USER_EMAIL_NOT_VALID')

    def test_create_user(self):
        """Test creating a new user"""
        response = self.client.post('/users', json={
            "name": "John Doe",
            "email": "john.doe@example.com"
        })
        obj = json.loads(str(response.data.decode('utf-8')))

        print(obj)
        self.assertEqual(response.status_code, 201)
        self.assertIn('John Doe', str(response.data))
    
    def test_get_user(self):
        """Test retrieving a user"""
        user = User(name='John Doe', email='john.doe@example.com')
        db.session.add(user)
        db.session.commit()

        response = self.client.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', str(response.data))

    # def test_update_user(self):
    #     """Test updating a user"""
    #     user = User(name='John Doe', email='john.doe@example.com')
    #     db.session.add(user)
    #     db.session.commit()

    #     response = self.client.put(f'/users/{user.id}', json={
    #         'name': 'Jane Doe'
    #     })
    #     self.assertEqual(response.status_code, 200)

    #     updated_user = User.query.get(user.id)
    #     self.assertEqual(updated_user.name, 'Jane Doe')

    # def test_delete_user(self):
    #     """Test deleting a user"""
    #     user = UserModel(name='John Doe', email='john.doe@example.com')
    #     db.session.add(user)
    #     db.session.commit()

    #     response = self.client.delete(f'/users/{user.id}')
    #     self.assertEqual(response.status_code, 200)

    #     deleted_user = UserModel.query.get(user.id)
    #     self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
