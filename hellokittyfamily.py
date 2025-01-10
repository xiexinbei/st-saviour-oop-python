from sanrio import Sanrio


class HelloKittyFamily(Sanrio):
    def __init__(self, name: str, nationality: str, age: int, personalities: list[str]):
        super().__init__('United Kingdom', ['warm', 'supportive', 'family-oriented'])
        self.name = name
        self.nationality = nationality
        self.age = age
        self.personalities = personalities 

    def __str__(self):
       return f'HelloKittyFamily(name: {self.name})'

    def make_friends(self, friend: str):
        print(self.name + ' who lives in ' + self.location + ' is now friends with ' + friend)

    def add_themes(self, *args):
        for arg in args:
            self.themes.append(arg)
        