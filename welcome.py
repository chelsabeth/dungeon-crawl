from tomlkit import string


def info_welcome():
    print('Welcome to our version of the ultimate Dungeon Crawler.')
    print('\n')
    print('This game was created as a hacktoberfest project to get my wife and I into building something fun together...')
    print('\n')
    print('If you have any suggestions let us know... enjoy')
    print('\n')

def ask_name():
    name = string(input('What is your name adventurer?'))
    print('\n')
    print('{name}, that is a wonderful name!\n')
    print('Let us begin!')
    return name