class MusicPlayer:
    def previous_song(self):
        current_song_index = self.playlist.index(self.current_song)
        previous_song_index = (current_song_index - 1) % len(self.playlist)
        self.current_song = self.playlist[previous_song_index]
        return True