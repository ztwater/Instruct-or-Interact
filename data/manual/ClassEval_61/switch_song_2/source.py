class MusicPlayer:
    def switch_song(playlist):
        # Check if the playlist is empty
        if len(playlist) == 0:
            print("Playlist is empty.")
            return
    
        # Get the current song index
        current_song_index = playlist.index(current_song)
    
        # Check if the current song is the last song in the playlist
        if current_song_index == len(playlist) - 1:
            print("This is the last song in the playlist.")
            return
    
        # Switch to the next song
        next_song = playlist[current_song_index + 1]
        print("Switching to the next song:", next_song)
    
        # Update the current song
        current_song = next_song