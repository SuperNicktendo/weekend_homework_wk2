import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Twist and Shout", "The Beatles")
        self.song_2 = Song("Sound and Vision", "David Bowie")
        
    def test_song_has_title(self):
        self.assertEqual("Twist and Shout", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("David Bowie", self.song_2.artist)