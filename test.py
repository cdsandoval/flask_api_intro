import unittest

from config import config
from app import create_app, db


class TestAPI(unittest.TestCase):
    def setUp(self):
        enviroment = config['test']
        self.app = create_app(enviroment)
        self.client = self.app.test_client()

        self.content_type = 'application/json'
        self.path = 'http://127.0.0.1:5000/api/v1/tasks'

    def tearDown(self) -> None:
        with self.app.app_context():
            db.drop_all()

    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    def test_get_one_task(self):
        new_path = self.path + '/1'

        response = self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        # data = json.loads(response.data.decode('utf-8'))
        # task_id = data['data']['id']

        # self.assertEqual(task_id, 1)


if __name__ == '__main__':
    unittest.main()
