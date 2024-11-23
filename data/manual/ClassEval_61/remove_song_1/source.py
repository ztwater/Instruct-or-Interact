class MusicPlayer:
    def remove_song(playlist, song):
        if song in playlist:
            playlist.remove(song)
            print(f"Song '{song}' has been removed from the playlist.")
        else:
            print(f"Song '{song}' is not in the playlist.")
    