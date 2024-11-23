class MusicPlayer:
    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"Song '{song}' has been removed from the playlist.")
        else:
            print(f"Song '{song}' is not in the playlist.")