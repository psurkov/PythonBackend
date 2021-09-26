import unittest
from fastapi import HTTPException
import src.main.service.task_service as task_service
from src.main.model.task_model import TaskCreateModel
import src.main.dao.task_dao as task_dao


class TestCreateTask(unittest.TestCase):
    def test_create_simple_task(self):
        created_task = task_service.create_task(TaskCreateModel(name="name",
                                                                description="description",
                                                                original_score=10.0))
        self.assertEqual("name", created_task.name)
        self.assertEqual("description", created_task.description)
        self.assertAlmostEqual(10.0, created_task.original_score, delta=0.1)
        self.assertAlmostEqual(8.0, created_task.score_after_soft_deadline, delta=0.1)

        saved_task = task_dao.get_task_by_id(created_task.id)
        self.assertEqual(created_task, saved_task)

    def test_create_task_with_zero_score(self):
        created_task = task_service.create_task(TaskCreateModel(name="name",
                                                                description="description",
                                                                original_score=0))
        self.assertEqual("name", created_task.name)
        self.assertEqual("description", created_task.description)
        self.assertAlmostEqual(0, created_task.original_score, delta=0.1)
        self.assertAlmostEqual(0, created_task.score_after_soft_deadline, delta=0.1)

        saved_task = task_dao.get_task_by_id(created_task.id)
        self.assertEqual(created_task, saved_task)

    def test_create_task_with_negative_score(self):
        with self.assertRaises(HTTPException) as context:
            task_service.create_task(TaskCreateModel(name="test", description="test", original_score=-10.0))
        self.assertEqual(400, context.exception.status_code)


class TestGetTask(unittest.TestCase):
    def test_get_existing_task(self):
        task = task_service.get_task("566")
        self.assertEqual("Name3", task.name)
        self.assertEqual("description3", task.description)
        self.assertAlmostEqual(5.0, task.original_score, delta=0.1)
        self.assertAlmostEqual(0.1, task.score_after_soft_deadline, delta=0.1)

    def test_get_non_existing_task(self):
        with self.assertRaises(HTTPException) as context:
            task_service.get_task("1293489402123")
        self.assertEqual(400, context.exception.status_code)


if __name__ == '__main__':
    unittest.main()
