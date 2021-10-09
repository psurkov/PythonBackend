import unittest
import app.src.main.dao.task_dao as task_dao
from app.src.main.model.task_model import TaskModel
import app.src.main.database as database


class GetTaskByIdTest(unittest.TestCase):

    def setUp(self) -> None:
        database.init()
        database.execute('''
            insert into tasks(id, name, description, original_score, score_after_soft_deadline)
            values ('{}', '{}', '{}', '{}', '{}')
            '''.format(
            "30",
            "Name1",
            "description1",
            10.0,
            0.3)
        )
        database.execute('''
                    insert into tasks(id, name, description, original_score, score_after_soft_deadline)
                    values ('{}', '{}', '{}', '{}', '{}')
                    '''.format(
            "239",
            "Name2",
            "description2",
            13.0,
            0.5)
        )
        database.execute('''
                    insert into tasks(id, name, description, original_score, score_after_soft_deadline)
                    values ('{}', '{}', '{}', '{}', '{}')
                    '''.format(
            "566",
            "Name3",
            "description3",
            5.0,
            0.1)
        )

    def tearDown(self) -> None:
        database.clear()

    def test_get_task_by_id_existing(self):
        task = task_dao.get_task_by_id("566")
        self.assertEqual("Name3", task.name)
        self.assertEqual("description3", task.description)
        self.assertAlmostEqual(5.0, task.original_score, delta=0.1)
        self.assertAlmostEqual(0.1, task.score_after_soft_deadline, delta=0.1)

    def test_get_task_by_id_existing_another(self):
        task = task_dao.get_task_by_id("239")
        self.assertEqual("Name2", task.name)
        self.assertEqual("description2", task.description)
        self.assertAlmostEqual(13.0, task.original_score, delta=0.1)
        self.assertAlmostEqual(0.5, task.score_after_soft_deadline, delta=0.1)

    def test_get_task_by_id_non_existing(self):
        task = task_dao.get_task_by_id("23348209381")
        self.assertIsNone(task)


class UpsertTaskTest(unittest.TestCase):
    def setUp(self) -> None:
        database.init()

    def tearDown(self) -> None:
        database.clear()

    def test_upsert_task(self):
        new_task = TaskModel(id="100", name="Name4", description="description4", original_score=10.0,
                             score_after_soft_deadline=3.0)
        task_dao.upsert_task(new_task)
        upserted_task = task_dao.get_task_by_id(new_task.id)
        self.assertEqual("Name4", upserted_task.name)
        self.assertEqual("description4", upserted_task.description)
        self.assertAlmostEqual(10.0, upserted_task.original_score, delta=0.1)
        self.assertAlmostEqual(3.0, upserted_task.score_after_soft_deadline, delta=0.1)

    def test_upsert_task_without_name_and_description(self):
        new_task = TaskModel(id="100", name="", description="", original_score=10.0,
                             score_after_soft_deadline=3.0)
        task_dao.upsert_task(new_task)
        upserted_task = task_dao.get_task_by_id(new_task.id)
        self.assertEqual("", upserted_task.name)
        self.assertEqual("", upserted_task.description)
        self.assertAlmostEqual(10.0, upserted_task.original_score, delta=0.1)
        self.assertAlmostEqual(3.0, upserted_task.score_after_soft_deadline, delta=0.1)

    def test_upsert_task_with_zero_score(self):
        new_task = TaskModel(id="100", name="Name4", description="description4", original_score=0,
                             score_after_soft_deadline=0)
        task_dao.upsert_task(new_task)
        upserted_task = task_dao.get_task_by_id(new_task.id)
        self.assertEqual("Name4", upserted_task.name)
        self.assertEqual("description4", upserted_task.description)
        self.assertAlmostEqual(0, upserted_task.original_score, delta=0.1)
        self.assertAlmostEqual(0, upserted_task.score_after_soft_deadline, delta=0.1)


if __name__ == '__main__':
    unittest.main()
