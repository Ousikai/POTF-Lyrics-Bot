
#!/usr/bin/env python
import os
import sys

def get_songs_list():
    #Get unique lyrics for each song
    file_names = os.listdir("lyrics/")
    for song in file_names:
        unique = []
        #Break song into array of lyrics
        with open("lyrics/" + song, "r") as s:
            lyrics = s.readlines()
            #Check if lyric has been seen before and if not, add to unique[]
            for lyric in lyrics:
                lyric.strip()
                if not(lyric in unique):
                    unique.append(lyric)
        #Rewrite entire file line-by-line
        update = open("lyrics/" + song, "w")
        for lyric in unique:
             update.write(lyric)
        update.close()


if __name__ == "__main__":
    get_songs_list()
