class MusicPlayer:
    def previous_song(playlist):
        current_song_index = playlist.index(current_song)
        previous_song_index = (current_song_index - 1) % len(playlist)
        return playlist[previous_song_index]