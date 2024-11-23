class MusicPlayer:
    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        if len(self.playlist) == 0:
            return False
        else:
            random.shuffle(self.playlist)
            return True