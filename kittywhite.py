from hellokittyfamily import HelloKittyFamily

class KittyWhite(HelloKittyFamily):
    def __init__(self, favorite_food: str, appearance: str):
        super().__init__('Kitty White', 'British', 'forever 5 years old', ['kind_hearted', 'playful', 'curious'])
        self.favorite_food = favorite_food
        self.appearance = appearance


    def help_others(self):
        return 'KittyWhite from ' + self.location + ' wants to make friends with you!'
