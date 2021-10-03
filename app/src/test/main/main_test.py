import unittest
import app.src.main.main as main
from fastapi.testclient import TestClient
import graphene.test
from app.src.main.graphene_query.calendar import CalendarQuery


class MainTest(unittest.TestCase):
    client = TestClient(main.app)
    graphqlClient = graphene.test.Client(graphene.Schema(query=CalendarQuery))

    def test_root(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual({'message': 'Hello World'}, response.json())

    def test_get_task(self):
        response = self.client.get('/task/30')
        self.assertEqual(200, response.status_code)
        self.assertEqual({'description': 'description1',
                          'id': '30',
                          'name': 'Name1',
                          'original_score': 10.0,
                          'score_after_soft_deadline': 0.3},
                         response.json())

    def test_hello(self):
        response = self.graphqlClient.execute('''{hello(name: "test_name")}''')
        self.assertEqual({'data': {'hello': 'Hello test_name'}}, response)

    def test_timestamp(self):
        response = self.graphqlClient.execute('''{timestamp}''')
        self.assertIsNotNone(response.get('data').get('timestamp'))


if __name__ == '__main__':
    unittest.main()
