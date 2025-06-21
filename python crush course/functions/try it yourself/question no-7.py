def make_album(artist_name, album_title, tracks=None):
    """Return a dictionary containing artist name and album title."""
    album = {'artist': artist_name, 'album': album_title}
    if tracks is not None:
        album['tracks'] = tracks
    return album
album1 = make_album('jimi hendrix', 'are you experienced')
album2 = make_album('john hooker', 'the blues' )
album3 = make_album('bb king', 'live at the regal')
print(album1)
print(album2)
print(album3)
