class MusicPlayer:
    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        """
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"Song '{song}' has been removed from the playlist.")
        else:
            print(f"Song '{song}' is not in the playlist.")