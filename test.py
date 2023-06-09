import unittest
from app import create_app, db
from config import config

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config["test"])
        self.client = self.app.test_client()
        self.content_type = "application/json"
        self.path = "http://127.0.0.1:5000/api/v1"


    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_one_one(self):
        self.assertEqual(1,1)

    def test_get_all_tasks(self):
        response = self.client.get(path=self.path + "/tasks")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()