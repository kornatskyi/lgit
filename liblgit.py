import os

print(os.listdir("./"))


class File:
    def __init__(self, name, content=None):
        self.name = name
        self.content = content
        pass


class Dir:
    def __init__(self, name, files):
        self.name = name
        self.files = files
        pass


class Saving:
    def __init__(self, name):
        self.name = name
        pass


class DotDir:
    def __init__(self):
        self.dir_name = '.lgit'
        pass

    # Initialize a new .lgit directory
    def init(self):
        if os.path.isdir('./.lgit'):
            print(".lgit directory already exists")
        else:
            os.mkdir(path='./' + self.dir_name)
            os.mkdir(path='./' + self.dir_name + '/' + "savings")
            print("New .lgit is initialized!")


def main():
    print()
    dot_dir = DotDir()
    dot_dir.init()

    pass


if __name__ == '__main__':
    main()
