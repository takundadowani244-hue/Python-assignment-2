## Question 5: Abstract Base Class — FileHandler##
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            content = f.read()
        print(f"Text content read from {self.filename}:\n{content}")
        return content

    def write(self, data):
        with open(self.filename, "w") as f:
            f.write(data)
        print(f"Text data written to {self.filename}.")


class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "rb") as f:
            content = f.read()
        print(f"Binary content read from {self.filename}: {len(content)} bytes")
        return content

    def write(self, data):
        with open(self.filename, "wb") as f:
            f.write(data)
        print(f"Binary data written to {self.filename}.")


# Demonstration
text_handler = TextFileHandler("notes.txt")
text_handler.write("Hello, this is a text file.")
text_handler.read()

binary_handler = BinaryFileHandler("data.bin")
binary_handler.write(b"\x00\x01\x02\x03")
binary_handler.read()

# Attempting to instantiate the abstract class directly fails:
# handler = FileHandler()   # TypeError: Can't instantiate abstract class