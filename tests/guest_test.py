import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Splinter", "Rat Trap", 14.00)
        self.guest_2 = Guest("Shredder", "Baby Shark", 5.00)
        self.room_1 = Room(1, 10.00)
        self.song1 = Song("Rat Trap", "Boomtown Rats")

    def test_guest_has_name(self):
        self.assertEqual("Splinter", self.guest_1.name)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Rat Trap", self.guest_1.fave_song)
    
    def test_customer_has_money(self):
        self.assertEqual(14.00, self.guest_1.wallet)
    
    def test_guest_pay_entry_subtracts_money(self):
        self.guest_1.pay_entry(self.room_1)
        self.assertEqual(4.00, self.guest_1.wallet)

    def test_favourite_song_reaction(self):
        self.room_1.add_song(self.song1.title)
        self.assertEqual("Cowabunga!", self.guest_1.favourite_song(self.guest_1.fave_song))
        
    def test_guest_can_afford_to_sing(self):
        self.room_1.check_in_guest(self.guest_1.wallet)
        self.assertEqual("Welcome!", self.guest_1.can_afford(self.room_1.entry_fee))

    def test_guest_cant_afford_to_sing(self):
        self.room_1.check_in_guest(self.guest_2.wallet)
        self.assertEqual("Sorry, you can't afford to sing here.", self.guest_2.can_afford(self.room_1.entry_fee))

