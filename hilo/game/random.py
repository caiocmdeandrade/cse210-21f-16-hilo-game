
import random


class R_Cards:
    def __init__(self, random):
        print(f"The card is: {random}")
        self.random = random

random_N = random.randint(1,13)
R_card = R_Cards(random_N)

