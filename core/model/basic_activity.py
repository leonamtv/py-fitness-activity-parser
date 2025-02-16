from abc import ABC, abstractmethod

from core.utils.serialization import to_json

class BasicActivity(ABC):

    @abstractmethod
    def to_json(self):
        return to_json(self)