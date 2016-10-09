#!/usr/bin/env python
import os
import sys
import random   
    
# Grab a random song from the lyrics folder
def get_song():
    file_names = os.listdir("lyrics/")
    song_name = random.choice(file_names)
    return song_name

# 1) Choose random song
# 2) Grab random lyric from song
# 3) Add to list compose[]
# 4) Repeat two more times
# 5) Check if less than 140 chars. Repeat steps 1-5 if failure
# 6) Tweet result!
def compose_tweet():
    compose = []
    for iter in range(0,3): 
        # Open the song file we want to use and create an array of lines
        song_name = get_song()
        song_location = "lyrics/" + song_name
        song = open(song_location,"r")    
        lines = song.readlines()
        song.close()
        length = len(lines)
    
        # Choose random lyric based on file size, then add to compose[]
        ptr = random.randrange(length) 
        lyric = lines[ptr]
        compose.append(lyric)

    # Tweet result!
    for iter in range(0,3):
        sys.stdout.write(compose[iter])
    
    
# It's showtime      
if __name__ == "__main__":
    compose_tweet()
    #get_song()
