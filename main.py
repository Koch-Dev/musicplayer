#!/usr/bin/env python3

import os
import sys
from youtubesearchpython import VideosSearch

def play_audio(query):
    video_search = VideosSearch(query, limit=1)
    results = video_search.result()

    if results['result']:
        video_url = results['result'][0]['link']
        os.system(f"mpv --no-video {video_url}")
    else:
        print(f"No results found for '{query}'.")

def play_video(query):
    video_search = VideosSearch(query, limit=1)
    results = video_search.result()

    if results['result']:
        video_url = results['result'][0]['link']
        os.system(f"mpv {video_url}")
    else:
        print(f"No results found for '{query}'.")

def play_songs(song_list):
    for current_song in song_list:
        print(f"Playing: {current_song}")
        play_audio(current_song)

def main():
    if len(sys.argv) < 3:
        print("Usage: ./main.py play 'song name' OR ./main.py playlist 'song1' 'song2' ... OR ./main.py vplay 'video name'")
        sys.exit(1)

    command = sys.argv[1].lower()
    media_names = sys.argv[2:]

    if command == "play":
        if len(media_names) != 1:
            print("Usage: ./main.py play 'song name'")
            sys.exit(1)
        play_audio(media_names[0])
    elif command == "playlist":
        play_songs(media_names)
    elif command == "vplay":
        if len(media_names) != 1:
            print("Usage: ./main.py vplay 'video name'")
            sys.exit(1)
        play_video(media_names[0])
    else:
        print("Unknown command. Use 'play' for a single song, 'playlist' for a list of songs, or 'vplay' for a video.")
        sys.exit(1)

if __name__ == "__main__":
    main()
