# Sanrio Class
class Sanrio:
    def __init__(self, location: str, themes: list[str]):
        self.location = location
        self.themes = themes

    def add_themes(self, *args):
        for arg in args:
            self.themes.append(arg)