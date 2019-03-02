from abc import abstractmethod, ABC


class Command(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def run(self):
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class This(Command):

    def __init__(self):
        super().__init__("title")

    def run(self):
        pass


class Transfer(Command):

    def __init__(self):
        super().__init__("transfer")

    def run(self):
        pass


class Shift(Command):

    def __init__(self):
        super().__init__("shift")

    def run(self):
        pass
