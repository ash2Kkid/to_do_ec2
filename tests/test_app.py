import unittest
from app import app

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Todo API', response.data)

    def test_favicon(self):
        response = self.app.get('/favicon.ico')
        self.assertEqual(response.status_code, 204)

    def test_404_error(self):
        response = self.app.get('/invalid-route')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Endpoint not found', response.data)

    def test_add_todo(self):
        response = self.app.post('/todos', json={"task": "Test todo"})
        self.assertEqual(response.status_code, 201)

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)

    def test_update_todo(self):
        self.app.post('/todos', json={"task": "Original"})
        response = self.app.put('/todos/0', json={"task": "Updated"})
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        self.app.post('/todos', json={"task": "To delete"})
        response = self.app.delete('/todos/0')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
