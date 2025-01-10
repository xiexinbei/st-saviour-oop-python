from abc import ABC, abstractmethod

# Sanrio Class
#abstact makes sure that every class to follow the rule
class Sanrio(ABC):
    def __init__(self, location: str, themes: list[str]):
        self.location = location
        self.themes = themes

    @abstractmethod
    def add_themes(self, *args):
        pass