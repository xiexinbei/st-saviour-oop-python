from hellokittyfamily import HelloKittyFamily

class KittyWhite(HelloKittyFamily):
    def __init__(self, favorite_food: str, appearance: str):
        super().__init__('British', '48 years old', ['kind_hearted', 'playful', 'curious'])
        self.favorite_food = favorite_food
        self.appearance = appearance


    def help_others():
        print('KittyWhite from '+ self.nationality + 'wants to make friend with you!')
