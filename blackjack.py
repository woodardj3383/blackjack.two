import random
from IPython.display import clear_output


class Deck:

    def __init__(self):

        suits = ['Spades', 'Clubs', 'Hearts', "Diamonds"]
        ranks = list(range(1, 14))
        self.deck = [(rank, suit) for rank in ranks for suit in suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        return self.deck.pop(random.randrange(len(self.deck)))


class Player:
    def __init__(self):
        self.hand_1 = []

    def reveal(self):
        print(f'Player Hand: {self.hand_1}|')

    def clean_tuple(self):
        self.hand_1 = [list(i)for i in self.hand_1]
        for i in self.hand_1:
            if i[0] == 11 or i[0] == 12 or i[0] == 13:
                i[0] = 10
        return self.hand_1

    def tally_total(self):
        total = 0
        self.clean_tuple()
        for i in self.hand_1:
            total += i[0]
            while total <= 11:
                if i[0] == 1 or i[1] == 1:
                    total += 10
                elif i[0] == 1 and i[1] == 1:
                    total += 10
                else:
                    break

                break
            while total > 21:
                for i in self.hand_1:
                    if i[0] == 1 or i[1] == 1:
                        total -= 10
                    else:
                        break

        return total


class Dealer(Player):
    def __init__(self):
        super().__init__()

    def hit(self, card):
        self.hand_1.append(card)
        print(f'Dealer Hand: {self.hand_1[:]} | ')

    def deal(self, a_deck, person):
        i = 0
        while i < 2:
            person.hand_1.append(a_deck.pop())
            i += 1

    def reveal(self):
        print(f'Dealer Hand: {self.hand_1}|')

    def show(self):
        print(f'Dealer Hand: {self.hand_1[0]} |{self.tally_d()} ')

    def tally_d(self):
        total = 0
        for i in self.hand_1:
            self.clean_tuple()
            if i[0] == 1:
                total += 10
            else:
                break
        return i[0]


class Human(Player):

    def __init__(self):
        super().__init__()

    def hit(self, card):
        self.hand_1.append(card)

        print(f'Player_1 Hand: {self.hand_1}| {self.tally_total()}')


class Game:

    def main():
        my_deck = Deck()
        player_1 = Human()
        dealer = Dealer()

        def wrap(function):
            def decorate(greeting):
                print(
                    "=====================================================================")
                function(greeting)
                print(
                    "=====================================================================")
            return decorate

        @wrap
        def print_greeting(greeting):
            print(greeting)
        print_greeting("""
        Howdy Folks! Care for a game of Black-Jack?!?

        It's easy. The object of the game is to get your cards to add up to 21 without 
        going over -- Going over is called a "Bust".

        Number cards are worth face value. Face cards are worth 10 a piece, and A's are worth
        1 or 11 depending on what other cars you are holding.

        You and the dealer start with two cards a piece. 
        All cards are dealt face up except for one of the dealer's cards.

        If your hand needs more cards in order to beat the dealer choose "Hit" for another
        card. If you feel good about your hand choose "Stand".

        At that point the dealer will reveal their second car. The dealer must "Hit" if 
        their hand is 16 or less, and "Stand" if it is 17 or more.

        If your first two cards add up to 21 that's an automatic "Black-Jack" and you win!


        """)
        game_over = False
        start = input('Would you like to play? Y/N: ').lower()
        while not game_over:

            clear_output()
            if start == 'n':
                print("Goodbye!")
                game_over = True

            elif start == 'y':
                clear_output()
                player_1.hand_1.clear()
                dealer.hand_1.clear()
                my_deck.shuffle_deck()
                dealer.deal(my_deck.deck, player_1)
                dealer.deal(my_deck.deck, dealer)
                player_1.reveal()
                print('====================')
                print(player_1.tally_total())
                print('====================')
                dealer.show()
                print('====================')
                print(dealer.tally_d())

            else:
                print(f'Please pick a valid respone')
                pass

            playing = True
            while playing:
                clear_output()
                player_1.reveal()
                print('====================')
                print(player_1.tally_total())
                print('====================')
                dealer.show()

                print(dealer.tally_d())
                print('====================')
                if player_1.tally_total() == 21 and len(player_1.hand_1) == 2:
                    confirm = input(
                        'Black-Jack! You Win! Care for another game? Y/N').lower()
                    if confirm == 'y':
                        playing = False
                        break
                    elif confirm == 'n':
                        playing = False
                        game_over = True
                elif player_1.tally_total() > 21:
                    clear_output()
                    player_1.reveal()
                    print('====================')
                    print(player_1.tally_total())
                    print('====================')
                    dealer.show()
                    print('====================')
                    print(dealer.tally_d())
                    confirm = input(
                        'Bust! You Lose! Care for another game? Y/N').lower()
                    if confirm == 'y':
                        #playing = True
                        break
                        game_over = False
                    elif confirm == 'n':
                        #clear_output()
                        #playing= True
                        break
                        game_over = True
                        print('Goodbye!')

                card1 = my_deck.deal_cards()
                ans = input(f'Hit or Stand? ').lower()

                if ans == 'hit':
                    clear_output()
                    player_1.hit(card1)
                    player_1.reveal()
                    print('====================')
                    print(player_1.tally_total())
                    print('====================')
                    dealer.show()
                    print('====================')
                    print(dealer.tally_d())

                    #print(player_1.tally_total())
                elif ans == 'stand':
                    #clear_output()
                    #clear_output()
                    #player_1.reveal()
                    #print('====================')
                    #print(player_1.tally_total())
                    #print('====================')
                    #dealer.show()

                    #print(dealer.tally_d())
                    #print('====================')

                    #lear_output()

                    p_total = player_1.tally_total()
                    d_total = dealer.tally_total()
                    #print(f'Player Score:{p_total}')
                    #print(f'Dealer Score:{d_total}')
                   # clear_output()
                    while dealer.tally_total() < 17:
                        dealer.hit(card1)
                        if dealer.tally_total() <= 17:
                            pass
                    if dealer.tally_total() < 22 and dealer.tally_total() > p_total:
                        clear_output()
                        player_1.reveal()
                        print('====================')
                        print(p_total)
                        print('====================')
                        dealer.reveal()
                        print('====================')
                        print(dealer.tally_total())
                        pa = input(
                            'Sorry, you lost! Would you like to play again? Y/N ').lower()
                        clear_output()
                        if pa == 'y':
                            playing = False
                        elif pa == "n":
                            print(
                                f'Thanks for playing! Come back for a game anytime.')
                            playing = False
                            game_over = True

                    elif dealer.tally_total() < 22 and dealer.tally_total() == p_total:
                        clear_output()
                        player_1.reveal()
                        print('====================')
                        print(p_total)
                        print('====================')
                        dealer.reveal()
                        print('====================')
                        print(dealer.tally_total())
                        pa = input(
                            'It\'s a tie! Would you like to play again? Y/N ').lower()
                        clear_output()
                        if pa == 'y':
                            playing = False
                        elif pa == "n":
                            print(
                                f'Thanks for playing! Come back for a game anytime.')
                            playing = False
                            #done = False
                            game_over = True

                    elif dealer.tally_total() >= 17 and dealer.tally_total() < p_total:
                        clear_output()
                        player_1.reveal()
                        print('====================')
                        print(p_total)
                        print('====================')
                        dealer.reveal()
                        print('====================')
                        print(dealer.tally_total())
                        pa = input(
                            'You Win! Would you like to play again? Y/N ').lower()
                        clear_output()
                        if pa == 'y':
                            playing = False
                        elif pa == "n":
                            print(
                                f'Thanks for playing! Come back for a game anytime.')
                            playing = False
                            #done = False
                            game_over = True

                    elif dealer.tally_total() > 21:
                        clear_output()
                        player_1.reveal()
                        print('====================')
                        print(p_total)
                        print('====================')
                        dealer.reveal()
                        print('====================')
                        print(dealer.tally_total())
                        pa2 = input(
                            "Dealer BUSTED! You Win! Play again? Y/N ").lower()

                        if pa2 == 'y':
                            playing = False
                        elif pa2 == "n":
                            clear_output()
                            print(
                                f'Thanks for playing! Come back for a game anytime.')
                            playing = False


Game.main()
