from fnmatch import fnmatch
from os import makedirs, scandir, mkdir, remove
from subprocess import call
from shutil import move, copytree, rmtree, copy2
from json import load
from typing import Iterable


class FileManager:

    @staticmethod
    def write_data(file, data):
        with open(file, "w") as file:
            file.write(data)

    @staticmethod
    def read_data(file) -> str:
        with open(file, "r") as file:
            return file.read()

    @staticmethod
    def get_items(directory) -> Iterable:
        return list(scandir(directory))

    @staticmethod
    def create_dir(path):
        try:
            mkdir(path)
            return True
        except FileExistsError:
            return False

    @staticmethod
    def create_dirs(path):
        try:
            makedirs(path)
            return True
        except FileExistsError:
            return False

    @staticmethod
    def create_file(path):
        with open(path, "w+"):
            pass

    @staticmethod
    def delete_file(file):
        remove(file)

    @staticmethod
    def delete_dir(directory):
        rmtree(directory, ignore_errors=True)

    @staticmethod
    def copy_file(source, destination):
        copy2(source, destination)

    @staticmethod
    def copy_dir(source, destination):
        copytree(source, destination)

    @staticmethod
    def move_object(source, destination):
        move(source, destination)

    @staticmethod
    def refactor_python_file(source, old_path, new_path):

        with open(source, "r") as file:
            lines = file.readlines()

        # Change all occurrences of the old_path to new_path
        new_lines = list()
        for line in lines:
            line = line.replace(old_path, new_path) if old_path in line else line
            new_lines.append(line)

        with open(source, "w") as file:
            file.write("\n".join(new_lines))

    @staticmethod
    def git():

        with open("user_settings.json") as json_file:
            gitPath = load(json_file).get("gitPath")

        # List to set directory and working tree
        dirList = ["--git-dir=./.git", "--work-tree=."]

        # Adds all files in folder
        call([gitPath] + dirList + ["add", "."])

        # Commits the change with the message
        call([gitPath] + dirList + ["commit", "--message", "Seize file organisation complete!"])

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

    def get_specific_files(self, directory, keyword, file_type: str):
        return [entry for entry in self.get_items(directory) if fnmatch(entry, f"*{keyword}*.{file_type}")]

    def get_images(self, directory):
        return [entry for entry in self.get_items(directory) if entry.endswith(".png", ".jpg", ".gif", ".jpeg")]

    def get_sounds(self, directory):
        return [entry for entry in self.get_items(directory) if entry.endswith(".mp3", ".mp4", ".wav", ".ogg")]

    def get_fonts(self, directory):
        return [entry for entry in self.get_items(directory) if entry.endswith(".ttf", ".otf")]
