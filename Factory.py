from abc import ABC, abstractmethod

class File(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def edit(self, content):
        pass

    @abstractmethod
    def save(self):
        pass
class JsonFile(File):
    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def open(self):
        print(f"Opening JSON file: {self.filename}")


    def edit(self, content):
        print(f"Editing JSON file: {self.filename}")
        self.content = content

    def save(self):
        print(f"Saving JSON file: {self.filename}")



class XmlFile(File):
    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def open(self):
        print(f"Opening XML file: {self.filename}")


    def edit(self, content):
        print(f"Editing XML file: {self.filename}")
        self.content = content

    def save(self):
        print(f"Saving XML file: {self.filename}")
       
class FileFactory:
    @staticmethod
    def create_file(file_type, filename):
        if file_type == 'json':
            return JsonFile(filename)
        elif file_type == 'xml':
            return XmlFile(filename)
        else:
            raise ValueError("Unsupported file type")


def main():
    file_type = input("Enter file type (json/xml): ").strip().lower()
    filename = input("Enter file name: ")

    try:
        file = FileFactory.create_file(file_type, filename)
        file.open()

        content = input("Enter new content for the file: ")
        file.edit(content)
        file.save()

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
