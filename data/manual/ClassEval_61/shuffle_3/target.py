class MusicPlayer:
    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.shuffle()
        True
        """
        if len(self.playlist) == 0:
            return False
        random.shuffle(self.playlist)
        return True