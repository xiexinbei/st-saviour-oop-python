from abc import ABC, abstractmethod

# Sanrio Class
class Sanrio(ABC):
    def __init__(self, location: str, themes: list[str]):
        self.location = location
        self.themes = themes

    @abstractmethod
    def add_themes(self, *args):
        pass