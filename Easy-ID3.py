import eyed3

def edit_tags(file, **kwargs):
    
    if 'artist' in kwargs.keys(): file.tag.artist = kwargs['artist']
    if 'album' in kwargs.keys(): file.tag.album = kwargs['album']

    print("Updated tags.")

def print_tags(file):
    print("Title: " + file.tag.title)
    print("Artist: " + file.tag.artist)
    print("Album: " + file.tag.album)



filepath = input("Type a filepath: ")

try:
    file = eyed3.load(filepath)
except OSError:
    print("That file does not exist.")
    exit()

choice = input(\
"""
==============
Eazy ID3 Menu"
--------------
(v)iew tags
(e)dit tags
==============

> """)

if choice == 'v':
    print_tags(file)
    

elif choice == 'e':
    edit_tags(file, artist=input("Artist > "), album=input("Album > "))
else:
    print("That is not a valid option.")
    exit()
