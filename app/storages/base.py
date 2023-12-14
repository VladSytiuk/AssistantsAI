from abc import ABC, abstractmethod


class BaseStore(ABC):
    @abstractmethod
    def store(self, query, agent, answer):
        pass
