from fnmatch import fnmatch
import os
import shutil


class FileManager:

    @staticmethod
    def write_data(file, data):
        with open(file, "w") as file:
            file.write(data)

    @staticmethod
    def read_data(file):
        with open(file, "r") as file:
            return file.read()

    @staticmethod
    def get_items(directory):
        with os.scandir(directory) as entries:
            return entries

    @staticmethod
    def create_dir(path):
        try:
            os.mkdir(path)
            return True
        except FileExistsError:
            return False

    @staticmethod
    def create_dirs(path):
        try:
            os.makedirs(path)
            return True
        except FileExistsError:
            return False

    @staticmethod
    def delete_file(file):
        os.remove(file)

    @staticmethod
    def delete_dir(directory):
        shutil.rmtree(directory, ignore_errors=True)

    @staticmethod
    def copy_file(source, destination):
        shutil.copy2(source, destination)

    @staticmethod
    def copy_dir(source, destination):
        shutil.copytree(source, destination)

    @staticmethod
    def move_object(source, destination):
        shutil.move(source, destination)

    def get_files(self, directory):
        return [entry for entry in self.get_items(directory) if entry.is_file()]

    def get_sub_dirs(self, directory):
        return [entry for entry in self.get_items(directory) if entry.is_dir()]

    def get_python_files(self, directory, recursive=False):
        # TODO if no recursive functionality is required, simplify the method

        output = list()

        if recursive:
            for item in self.get_items(directory):

                if item.is_dir():
                    embedded_files = self.get_python_files(item)
                    output.extend(embedded_files)
                elif item.endswith(".py"):
                    output.append(item)
        else:
            output = [entry for entry in self.get_items(directory) if entry.endswith(".py")]

        return output

    def get_specific_files(self, directory, keyword, file_type):
        return [entry for entry in self.get_items(directory) if fnmatch(entry, f"*{keyword}*.{file_type}")]

    def get_images(self, directory):
        return [entry for entry in self.get_items(directory) if entry.endswith(".png", ".jpg", ".gif", ".jpeg")]

    def get_sounds(self, directory):
        return [entry for entry in self.get_items(directory) if entry.endswith(".mp3", ".mp4", ".wav", ".ogg")]

    def get_fonts(self, directory):
        return [entry for entry in self.get_items(directory) if entry.endswith(".ttf", ".otf")]
