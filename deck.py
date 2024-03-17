import random


class Deck:
    def __init__(self, suit, uni_id):
        self.suit = suit
        self.uni_id = uni_id

    def make_whole_suit(self):
        whole_suit = {}
        card_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]
        i = 0
        j = 0
        for num in card_nums:
            i += 1
            whole_suit.update({chr(self.uni_id + num): i})

        for card, value in whole_suit.items():
            face_names = ["Jack", "Queen", "King"]
            if value == 1:
                whole_suit.update({card: "Ace"})
            if value > 10:
                whole_suit.update({card: face_names[j]})
                j += 1
        return whole_suit






