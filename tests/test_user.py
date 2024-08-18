import unittest
from app.infrastructure.api import create_app, db
from app.infrastructure.models.user import UserModel
from app.config.test import TestConfig

class UserTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.app = create_app()
        self.app.config.from_object('app.config.test.TestConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Clean up after tests"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        """Test creating a new user"""
        response = self.client.post('/users', json={
            "name": "John Doe",
            "email": "john.doe@example.com"
        })
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('John Doe', str(response.data))

    # def test_get_user(self):
    #     """Test retrieving a user"""
    #     user = UserModel(name='John Doe', email='john.doe@example.com')
    #     db.session.add(user)
    #     db.session.commit()

    #     response = self.client.get(f'/users/{user.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('John Doe', str(response.data))

    # def test_update_user(self):
    #     """Test updating a user"""
    #     user = UserModel(name='John Doe', email='john.doe@example.com')
    #     db.session.add(user)
    #     db.session.commit()

    #     response = self.client.put(f'/users/{user.id}', json={
    #         'name': 'Jane Doe'
    #     })
    #     self.assertEqual(response.status_code, 200)

    #     updated_user = UserModel.query.get(user.id)
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
