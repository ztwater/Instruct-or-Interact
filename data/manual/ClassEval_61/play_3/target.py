class MusicPlayer:
    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        """
        if self.current_song is not None:
            print("Now playing:", self.current_song)
            return self.current_song
        else:
            print("No current song.")
            return False
