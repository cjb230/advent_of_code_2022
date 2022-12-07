SOURCE_FILE = 'day_7_input.txt'
from typing_extensions import Self


class File(object):
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class Directory(object):
    path: str
    name: str
    files: list
    directories: [Self]
    parent: Self
        
    def __init__(self, path, name, parent):
        self.path = path
        self.name = name
        self.parent = parent
    
    def add_file(self, file: File):
        self.files.append(file)

    def add_sub_directory(self, dir: Directory):
        self.directories.append(dir)
    
    def size(self) -> int:
        result = 0
        for file in self.files:
            result += file.size
        for dir in self.directories:
            result += dir.size()
        return result


def main() -> None:
    with open(SOURCE_FILE) as f:
        lines = f.readlines()
    
    current_object = Directory(path=None, name="/")
    for line in lines:
        if line[0:5] == "$ cd ":
            if line[6:8] == "..":
                current_object = current_object.parent
            else:
                current_path.append(line[5:].strip())
            continue
        if line[0:4] == "$ ls":
            
        


if __name__ == "__main__":
    main()
