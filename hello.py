from sanrio import Sanrio

if __name__ == '__main__':
    # print('new dawn, new day')
    hello_kitty = Sanrio('United Kingdom', [])
    print('themes: ' + str(hello_kitty.themes))
    hello_kitty.add_themes('happy', 'wholesome')
    print('themes: ' + str(hello_kitty.themes))