import os
import enum
import datetime
from utils import generate_folder_name_from_date


class FileStatus(enum.Enum):
    CHANGED = True
    SAVED = True


class File:
    def __init__(self, name, path, content=None, status=FileStatus.CHANGED):
        self.name = name
        self.path = path
        self.content = content
        self.status = status
        pass


class Dir:
    def __init__(self, name, path, files=None, ):
        self.name = name
        self.path = path
        self.files = files
        pass

    def parse_files(self):
        file_names = os.listdir(self.path)
        for f in file_names:
            if os.path.isdir(f):
                self.files.append(Dir("dirname " + f, f))
            else:
                self.files.append(File("filename " + f, f))


class Saving:
    def __init__(self, name, date: datetime.datetime):
        self.name = name
        self.date = date
        pass

    def save(self):
        os.mkdir('./.lgit/savings/' + generate_folder_name_from_date(self.date))
        pass


class DotDir:
    def __init__(self):
        self.files = []
        self.dir_name = '.lgit'

    # Initialize a new .lgit directory
    def init(self):
        if os.path.isdir('./.lgit'):
            print(".lgit directory already exists")
        else:
            os.mkdir(path='./' + self.dir_name)
            os.mkdir(path='./' + self.dir_name + '/' + "savings")
            self.x = print("New .lgit is initialized!")

    # Parse all files from the ./ directory, filter ignored files, and create objects of all file and directories
    def save_state(self):
        file_paths = os.listdir()
        ignore_paths = ['.lgit', '.lgitignore']
        # Parse filenames from .lgitignore
        with open('.lgitignore') as f:
            ignore_paths.extend(f.read().split())

        for f in file_paths:
            # If files not in git ignore create corresponding objects
            if not f in ignore_paths:
                if os.path.isdir(f):
                    self.files.append(Dir("dirname " + f, f))
                else:
                    self.files.append(File("filename " + f, f))

    def status(self):
        for f in self.files:
            print(f.name)


def main():
    dot_dir = DotDir()
    dot_dir.save_state()
    dot_dir.status()
    saving = Saving('name', datetime.datetime.now())
    saving.save()
    pass


if __name__ == '__main__':
    main()
