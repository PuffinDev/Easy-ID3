# How to set up your config file

The config file tells Eazy ID3 what to change.

## This is what the file looks like:
```ini
[FILENAME]
remove_text = 
change_text_to =


[TRACKNAME]
remove_text = 
change_text_to = 


[ARTIST]
remove_text = 
change_text_to = 


[ALBUM]
remove_text = 
change_text_to = 
```

There is a section for each attribute of a file. Underneath you can set what you want changed.

## remove_text

If you want any spesific text removed from a tag then set it here. If not, leave it blank.

## change_text_to

If you want to completely overwrite the tag and change the value to something new, set it here.


# Example file
```ini
[FILENAME]
remove_text = 
change_text_to = A song

[TRACKNAME]
remove_text = C418 - 
change_text_to = 

[ARTIST]
remove_text = 
change_text_to = C418

[ALBUM]
remove_text = 
change_text_to = excursions
```

This will change all filenames to **"A song"**, remove **"C418 - "** from track names, set the artist to **C418**, and set the album name to **"Excursions"**.

# Use cases

If you have a collection of music that is tagged with the wrong artist for example, just put it all in a directory, edit your config.ini file, and start easy id3 up. It will automatically change all the tags for you!