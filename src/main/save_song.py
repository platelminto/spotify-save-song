import sys

import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from spotify_api.spotify import Spotify
from main import notif_handler

options_file = '../options.txt'


class SpotifySaveSong:

    def __init__(self):
        self.monthly_playlist = SpotifySaveSong.read_option('monthly_playlist')

        if self.monthly_playlist == 'yes':
            self.monthly_playlist = True
        else:
            self.monthly_playlist = False

        self.spotify = Spotify()

    @staticmethod
    def read_option(option):
        with open(options_file) as file:
            line = file.readline().rstrip()
            while not line.startswith(option):
                line = file.readline().rstrip()

            return line.split('=')[1]

    def save_song(self):
        song_id = self.spotify.currently_playing_id()

        if song_id:

            is_saved = self.spotify.is_saved(song_id)

            if is_saved:

                if self.monthly_playlist:
                    self.spotify.remove_song_from_monthly_playlist('spotify:track:' + song_id)
                notif_handler.make_notif(self.spotify.remove_songs_from_library(song_id),
                                         'removed from', 'remove from')

            else:

                if self.monthly_playlist:
                    self.spotify.add_songs_to_monthly_playlist('spotify:track:' + song_id)
                notif_handler.make_notif(self.spotify.add_songs_to_library(song_id), 'added to', 'add to')
