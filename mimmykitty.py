from hellokittyfamily import HelloKittyFamily

class MimmyKitty(HelloKittyFamily):
    def __init__(self, outfit:str, favorite_book:str):
        super().__init__('British', 'Audlt mother age', ['traditional', 'helpful'])
        self.outfit = outfit
        self.favorite_book = favorite_book


    def read_book():
        print('MimmyKitty wants to share book with you!')
