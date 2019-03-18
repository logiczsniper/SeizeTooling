from unittest import TestCase
from src.file_manager import FileManager


class TestFileManager(TestCase):

    def setUp(self):
        self.dir_path = "test_directory"
        self.file_path = self.dir_path + "/test_file{}.txt"
        self.python_file_path = self.dir_path + "/test_py_file.py"
        self.all_file_path = self.dir_path + "/test_all_file.{}"
        self.sub_dir_path = self.dir_path + "/sub_test_directory"
        self.sub_dir_move_path = self.dir_path + "/sub_move_test_directory"
        self.sub_file_path = self.sub_dir_path + "/test_file{}.txt"
        self.file_manager = FileManager()

        # Create test directory.
        self.file_manager.create_dir(self.dir_path)

    def test_write_read_data(self):
        # Write data to file.
        self.file_manager.write_data(self.file_path, "test_data")

        # Test.
        self.assertEqual(self.file_manager.read_data(self.file_path), "test_data")

    def test_get_items(self):
        # Create test items.
        for difference in [1, 2, 3]:
            self.file_manager.create_file(self.file_path.format(difference))

        # Test.
        self.assertEqual([entry.path.split("\\")[1] for entry in self.file_manager.get_items(self.dir_path)],
                         ["test_file1.txt", "test_file2.txt", "test_file3.txt"])

    def test_delete_file(self):
        # Create test item.
        self.file_manager.create_file(self.file_path)

        # Delete item.
        self.file_manager.delete_file(self.file_path)

        # Test.
        self.assertEqual([entry.path.split("\\")[1] for entry in self.file_manager.get_items(self.dir_path)], list())

    def test_copy_file(self):
        # Create test file.
        self.file_manager.create_file(self.file_path.format(str()))

        # Create directory to copy file to.
        self.file_manager.create_dir(self.sub_dir_path)

        # Copy file.
        self.file_manager.copy_file(self.file_path.format(str()), self.sub_dir_path)

        # Test.
        self.assertEqual([entry.path.split("\\")[1] for entry in self.file_manager.get_items(self.sub_dir_path)],
                         ["test_file.txt"])

    def test_copy_dir(self):
        # Create test directory.
        self.file_manager.create_dir(self.sub_dir_path)

        # Create file in sub test directory.
        self.file_manager.create_file(self.sub_file_path.format("_move"))

        # Copy directory.
        self.file_manager.copy_dir(self.sub_dir_path, self.sub_dir_move_path)

        # Test.
        self.assertEqual([entry.path.split("\\")[1] for entry in self.file_manager.get_items(self.sub_dir_move_path)],
                         ["test_file_move.txt"])

    def test_move_object(self):
        # Create test directory.
        self.file_manager.create_dir(self.sub_dir_path)

        # Create file to be moved.
        self.file_manager.create_file(self.file_path)

        # Move file.
        self.file_manager.move_object(self.file_path, self.sub_dir_path)

        # Test.
        self.assertEqual([entry.path.split("\\")[1] for entry in self.file_manager.get_items(self.sub_dir_path)],
                         ["test_file{}.txt"])

    def test_refactor_python_file(self):
        # Create python file. Add lines to the file.
        with open(self.python_file_path, "w+") as file:
            file.write("\n".join(["my_str = 'refactor_this'", "print(my_str)"]))

        # Refactor python file.
        self.file_manager.refactor_python_file(self.python_file_path, "refactor_this", "I_got_refactored")

        # Test.
        with open(self.python_file_path, "r") as file:
            self.assertEqual(["my_str = 'I_got_refactored'\n", "\n", "print(my_str)"], file.readlines())

    def test_get_specific_files(self):
        # Create test files to be found.
        for extension in ["txt", "png", "wav", "ttf"]:
            self.file_manager.create_file(self.all_file_path.format(extension))

        # Test.
        for extension in ["txt", "png", "wav", "ttf"]:
            self.assertEqual(self.file_manager.get_specific_files(self.dir_path, "all_file", extension)[0].path,
                             f"test_directory\\test_all_file.{extension}")

    def tearDown(self):
        # Delete test objects.
        self.file_manager.delete_dir(self.dir_path)
        pass
