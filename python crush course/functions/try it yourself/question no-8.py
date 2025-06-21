def make_album(artist, title):
    """Return a dictionary containing artist name and album title."""
    album = {'artist': artist, 'title': title}
    return album
while True:
    print("\nPlease tell me the name of an artist:")
    print("Enter 'q' at any time to quit.")
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
    title = input("Album title: ")
    if title.lower() == 'q':
        break
    album_info = make_album(artist, title)
    print(f"\nAlbum info: {album_info['artist']} , {album_info['title']}")
