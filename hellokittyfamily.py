from sanrio import Sanrio


class HelloKittyFamily(Sanrio):
    def __init__(self, name: str, nationality: str, age: int, personalities: list[str]):
        super().__init__('United Kingdom', ['warm', 'supportive', 'family-oriented'])
        self.name = name
        self.nationality = nationality
        self.age = age
        self.personalities = personalities 

    def make_friends(self, friend: str):
        print(self.name + ' who lives in ' + self.location + ' is now friends with ' + friend)

        

        