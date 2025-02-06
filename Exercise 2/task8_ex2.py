from task6_ex2 import song1, song2, song3

def songs_of_genre(song_list: list, genre: str):
    matching_genre = []
    for song in song_list:
        if song.genre == genre:
            matching_genre.append(song)
    return matching_genre

songs = [song1, song2, song3]
print("Songs in the rock genre:")
for song in songs_of_genre(songs, "Rock"):
    print(f"{song.artist}: {song.title}")


