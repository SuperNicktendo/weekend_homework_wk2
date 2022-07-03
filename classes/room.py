class Room:
    def __init__(self, _room_number, _entry_fee):
        self.room_number = _room_number
        self.entry_fee = _entry_fee
        self.capacity = []
        self.song = []

    def capacity_count(self):
        return len(self.capacity)

    def check_in_guest(self, guest):
        full_up = "Sorry, we're fully booked."
        if len(self.capacity) < 10:
            self.capacity.append(guest)
        return full_up
        
    def check_out_guest(self, guest):
        if guest in self.capacity:
            self.capacity.remove(guest)
    
    def add_song(self, song):
        self.song.append(song)

    