#!/usr/bin/env python
import os
import sys
import random   
import tweepy
from secrets import *
import time

# 1) Choose random song
# 2) Grab random lyric from song
# 3) Add to list compose[]
# 4) Repeat two more times
# 5) Check if less than 140 chars. Repeat steps 1-5 if failure
# 6) Tweet result!
def compose_tweet():
    compose = ""
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
        compose = compose + lyric

    # Tweet result!
    tweet(compose)

# Code I'm utilizing from https://github.com/molly/twitterbot_framework
def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    if (len(text)<=140):
        api.update_status(text)
    else:
        #Implement logging later...
        sys.stdout.write("Twitter bot failed tweet")
    
# Grab a random song from the lyrics folder
def get_song():
    file_names = os.listdir("lyrics/")
    song_name = random.choice(file_names)
    return song_name

    
# It's showtime      
if __name__ == "__main__":
    #Post tweet every 10 seconds
    while True:
        compose_tweet()
        time.sleep(30)
