import eyed3
from progress.bar import Bar
import configparser
import os
import fnmatch


tags = ['title', 'artist', 'album']


directory = input(\
"""
=====================================
Easy ID3 Menu
-------------------------------------
Welcome to easy id3! To get started,
read the instructions in README.md on 
how to setup your config.ini.
=====================================

Enter the directory containing your audio files
> """)

config_file_name = input("\nType the name of your config file (enter for default) : ")

config = configparser.ConfigParser()
try:
    config.read(config_file_name)
    config.sections()
except:
    print("That is not a valid config file.")
    exit()


if os.path.exists(directory):
    #Count files
    filecount = 0
    print("Initialising...")
    for path, subdirs, files in os.walk(directory):  #Count files for progress bar
        for name in files:
            filecount += 1


    matching_files = []
    patterns = ['*.mp3']

    for path, subdirs, files in os.walk(directory):  #Find files with specified patterns
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    matching_files.append(os.path.join(path, name))
else:
    print("That directory does not exist.")

bar = Bar('Editing tags...', max=filecount)
for file in matching_files:
    music = eyed3.load(file)

    #remove_text
    if len(config['TRACKNAME']['remove_text']) > 0:
        music.tag.title.replace(config['TRACKNAME']['remove_text'], '')
    if len(config['ARTIST']['remove_text']) > 0:
        music.tag.artist = music.tag.artist.replace(config['ARTIST']['remove_text'], '')
    if len(config['ALBUM']['remove_text']) > 0:
        music.tag.artist = music.tag.artist.replace(config['ALBUM']['remove_text'], '')

    #change_text_to
    if config['TRACKNAME']['change_text_to']:
        music.tag.artist = music.tag.title = config['TRACKNAME']['change_text_to']
    if config['ARTIST']['change_text_to']:
        music.tag.artist = config['ARTIST']['change_text_to']
    if config['ALBUM']['change_text_to']:
        music.tag.artist = config['ALBUM']['change_text_to']

    music.tag.save()
    
    bar.next()

print("\n\nDone!")
    