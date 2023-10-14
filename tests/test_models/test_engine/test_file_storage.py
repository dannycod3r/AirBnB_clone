import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj3 = BaseModel()
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.new(self.obj3)
        self.storage.save()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn('BaseModel.{}'.format(self.obj1.id), objects)
        self.assertIn('BaseModel.{}'.format(self.obj2.id), objects)
        self.assertIn('BaseModel.{}'.format(self.obj3.id), objects)

    def test_new(self):
        obj4 = BaseModel()
        self.storage.new(obj4)
        objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(obj4.id), objects)

    def test_save(self):
        self.storage.save()
        self.assertTrue(
            os.path.exists(self.storage.__class__._FileStorage__file_path))

    def test_reload(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertIn('BaseModel.{}'.format(self.obj1.id), objects)
        self.assertIn('BaseModel.{}'.format(self.obj2.id), objects)
        self.assertIn('BaseModel.{}'.format(self.obj3.id), objects)
