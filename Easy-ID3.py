import eyed3


filepath = input("Type a filepath: ")

try:
    file = eyed3.load(filepath)
except OSError:
    print("That file does not exist.")
    exit()

print("Artist: " + file.tag.artist)
print("Album: " + file.tag.album)
print("\n")

file.tag.artist = input("What do you want to change the artist to? ")
file.tag.album = input("What do you want to change the album to? ")

file.tag.save()