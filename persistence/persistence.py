from abc import ABC, abstractmethod

class PersistenceLayer(ABC):
    @abstractmethod
    def create(self, data):
        raise NotImplementedError("Persistence layers must implement a create method")

    @abstractmethod
    def list(self, order_by=None):
        raise NotImplementedError("Persistence layers must implement a list method")

    @abstractmethod
    def edit(self, boookmark_id, bookmark_data):
        raise NotImplementedError("Persistence layers must implement a list method")

    @abstractmethod
    def delete(self, bookmark_id):
        raise NotImplementedError("Persistence layers must implement a delete method")