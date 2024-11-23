class MusicPlayer:
    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if self.current_song is None or len(self.playlist) == 0:
            return False
        else:
            current_song_index = self.playlist.index(self.current_song)
            previous_song_index = (current_song_index - 1) % len(self.playlist)
            self.current_song = self.playlist[previous_song_index]
            return True