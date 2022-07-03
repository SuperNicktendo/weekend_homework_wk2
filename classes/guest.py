class Guest:
    def __init__(self, _name, _fave_song, _wallet):
        self.name = _name
        self.fave_song = _fave_song
        self.wallet = _wallet

    def favourite_song(self, song):
        song_reaction = "Cowabunga!"
        if song == self.fave_song:
            return song_reaction
    
    def pay_entry(self, amount):
        if self.wallet >= amount.entry_fee:
            self.wallet -= amount.entry_fee
    
    def can_afford(self, amount):
        if self.wallet >= amount:
            return "Welcome!"
        else:
            return "Sorry, you can't afford to sing here."