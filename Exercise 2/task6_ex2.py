#Song class
class Song:
    def __init__(self, title, artist, genre, year):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year

#Printing song details
song1 = Song("BangerSongs", "Chris", "Rock", 1990)
print(f"Song title: {song1.title}, artist: {song1.artist}, genre: {song1.genre}, release: {song1.year}")