from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("Commands must implement an execute method")