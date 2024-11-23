class MusicPlayer:
    def switch_song(self):
        # Check if the playlist is empty
        if len(self.playlist) == 0:
            print("Playlist is empty.")
            return False
        
        # Get the current song index
        current_song_index = self.playlist.index(self.current_song)
        
        # Check if the current song is the last song in the playlist
        if current_song_index == len(self.playlist) - 1:
            print("This is the last song in the playlist.")
            return False
        
        # Switch to the next song
        next_song = self.playlist[current_song_index + 1]
        print("Switching to the next song:", next_song)
        
        # Update the current song
        self.current_song = next_song
        return True