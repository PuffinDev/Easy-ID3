import eyed3


filepath = input("Type a filepath: ")

try:
    file = eyed3.load(filepath)
except FileNotFoundError:
    print("That file does not exist.")
    exit()

print("Artist: " + file.tag.artist)
print("Album: " + file.tag.album)
