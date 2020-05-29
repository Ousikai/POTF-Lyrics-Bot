#!/usr/bin/env python
import os
import sys
import random
import tweepy
# from secrets_poets import *
import time
import datetime
import json

def lambda_handler(event, context):
    # compose_tweet(1)
    print("pizza")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# 1) Choose random song
# 2) Grab random lyric from song
# 3) Add to list compose[]
# 4) Repeat two more times
# 5) Check if less than 140 chars. Repeat steps 1-5 if failure
# 6) Tweet result!
def compose_tweet(count):
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
        if "\n" not in lyric:
          lyric = lyric + "\n"
        compose = compose + lyric

    # Tweet result!
    tweet(compose, count)

# Code I'm utilizing from https://github.com/molly/twitterbot_framework
def tweet(text, count):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Stop trying to upload a tweet after 4 failed attemps
    if (count >=4):
        sys.stdout.write("4 failed attempts. Twitter is probably down heh. \n")
        return 0
    # Send the tweet and log success or failure
    try:
        api.update_status(text)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #timestamp = "[TIMESTAMP]"
        sys.stdout.write("Tweet successful![" + str(timestamp) + "]\n")
        sys.stdout.write(text)
        sys.stdout.write("-----------------------------------------------\n")
    except:
        #Implement logging later...
        sys.stdout.write("Tweet failed. Writing new tweet...\n")
        compose_tweet(count+1)

# Grab a random song from the lyrics folder
def get_song():
    file_names = os.listdir("lyrics/")
    song_name = random.choice(file_names)
    return song_name
