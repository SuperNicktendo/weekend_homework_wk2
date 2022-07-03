import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 14.00)
        self.room_2 = Room(2, 18.00)
        self.guest1 = Guest("Mikey", "Go Ninja Go", 10.00)
        self.guest2 = Guest("Raph", "Happy Together", 16.00)
        self.guest3 = Guest("Leo", "Go Ninja Go", 25.00)
        self.guest4 = Guest("Donnie", "Happy Together", 30.00)
        self.song1 = Song("Go Ninja Go", "Vanilla Ice")
        self.song2 = Song("Happy Together", "The Turtles")
    
    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)
    
    def test_entry_fee(self):
        self.assertEqual(18.00, self.room_2.entry_fee)
    
    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest1.name)
        self.assertEqual(["Mikey"], self.room_1.capacity)
    
    def test_check_out_guest(self):
        self.room_1.check_in_guest(self.guest1.name)
        self.room_1.check_out_guest(self.guest1.name)
        self.assertEqual(0, self.room_1.capacity_count())

    def test_add_song(self):
        self.room_1.add_song(self.song1.title)
        self.assertEqual(["Go Ninja Go"], self.room_1.song)
    
    def test_room_is_full(self):
        self.room_1.capacity_count = 10
        self.assertEqual("Sorry, we're fully booked.", self.room_1.check_in_guest(self.guest3.name))
        
    


    
    
