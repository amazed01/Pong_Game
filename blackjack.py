import random


class Card:
    markers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'ace', 'jack', 'queen', 'king')
    suit = ('diamonds', 'clubs', 'hearts', 'spades')

    def __init__(self, place, suit):
        self.suit = suit
        self.place = place
        self.value = None
        if self.place in Card.markers[:9]:
            self.value = int(self.place)
        elif self.place in Card.markers[10:]:
            self.value = 10
        elif self.place == 'ace':
            self.value = 11

    def __str__(self):
        return self.place + ' of ' + self.suit

    def show_card(self):
        print(self.place, self.suit)


class Deck:
    def __init__(self):
        self.deck = list()
        for suit in Card.suit:
            for mark in Card.markers:
                self.deck.append(Card(mark, suit))

    def show_deck(self):
        for item in self.deck:
            item.show_card()

    def shuffle(self):
        random.shuffle(self.deck)

    def delete_cards(self):
        while len(self.deck) > 0:
            card = self.deck.pop()
            del card


class Player:
    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance

        self.betting_amount = None
        self.game_status = None
        self.hand = list()
        self.hand_worth = 0
        self.ace_appeared = 0

    def make_bet(self, bet):
        if self.balance >= bet:
            self.balance -= bet
            self.betting_amount = bet
            return True
        else:
            print('Insufficient Balance!!!')
            return False

    def update_balance(self):
        print('Amount in bet:: ', self.betting_amount)

        if self.game_status == 'win':
            self.balance = self.balance + (self.betting_amount * 2)
        elif self.game_status == 'tie':
            self.balance = self.balance + self.betting_amount
        else:
            self.betting_amount = None

    def update_hand(self, card):
        print('\n' + self.name, 'takes card from deck>>>>>>>>>>>>>\n')

        if card.place == 'ace':
            self.ace_appeared += 1
        self.hand_worth += card.value
        self.hand.append(card)
        while self.hand_worth > 21 and self.ace_appeared > 0:
            self.hand_worth -= 10
            self.ace_appeared -= 1
        if self.hand_worth > 21:
            self.game_status = 'bust'

    def show_hand(self):
        print('\n' + self.name, ' has hand as follows:::::\n')
        for item in self.hand:
            item.show_card()
        print('Current Hand Worth:\t', self.hand_worth)

    def show_balance_in_account(self):
        print('Current Balance in', self.name + "'s", 'account::   ', self.balance)
        print('Amount in bet:: ', self.betting_amount)


def get_valid_input(message):
    while True:
        valid_integer = input(message)
        try:
            valid_integer = int(valid_integer)
        except ValueError:
            print('Please enter a valid integer value')
        else:
            return valid_integer


def check_bust(player1, player2):
    if player1.game_status == 'bust':
        player2.game_status = 'win'
        print('\n\n' + player1.name, 'BUSTED!!!!!!!!!!!!!!!!!!!!!!\n')
        player1.show_hand()
        # print('Current Hand Worth:\t', human_player.hand_worth)
        return True
    else:
        return False


def results(tuple):
    player1, player2 = tuple
    print('\nRESULTS ARE AS FOLLOWS::\n')
    if player1.game_status == 'win':
        print(player1.name, 'wins')
    elif player2.game_status == 'win':
        print(player2.name, 'wins')
    elif player2.game_status == 'tie' == player1.game_status:
        print('GAME TIED')
    print('\n\nGAME OVER!!!!!!!!!!!!!!!!!!')
    del player1,player2


def start_game(player1, player2, playing_cards):
    player1.update_hand(playing_cards.deck.pop())
    player2.update_hand(playing_cards.deck.pop())
    player1.update_hand(playing_cards.deck.pop())
    c4 = playing_cards.deck.pop()
    player2.update_hand(c4)

    print(player2.name, ' has hand as follows::::')
    print('\nFACE', 'DOWN')
    c4.show_card()


def player_plays(human_player, dealer, playing_cards):
    while True:
        human_player.show_hand()
        action = input('\nDo you want to HIT or STAY ???\nPress "h" for HIT and "s" for STAY\t')

        if action == 'h':
            c = playing_cards.deck.pop()
            human_player.update_hand(c)
            c.show_card()

            busted = check_bust(human_player, dealer)
            if busted:
                return False
        elif action == 's':
            return True


def dealer_plays(dealer, human_player, playing_cards):
    print('\n\nTurn switch over to', dealer.name)

    while True:
        dealer.show_hand()

        if dealer.hand_worth == human_player.hand_worth == 21:
            dealer.game_status = human_player.game_status = 'tie'
            break
        elif dealer.hand_worth <= human_player.hand_worth:
            c = playing_cards.deck.pop()
            dealer.update_hand(c)
            c.show_card()

            busted = check_bust(dealer, human_player)
            if busted:
                break
        elif 21 >= dealer.hand_worth > human_player.hand_worth:
            dealer.game_status = 'win'
            break
        else:
            print('kuch kuch hua hai')
            break


def play_game(human_player, dealer):
    human_player.show_balance_in_account()

    switch_over = False

    playing_cards = Deck()
    playing_cards.shuffle()

    start_game(human_player, dealer, playing_cards)

    switch_over = player_plays(human_player, dealer, playing_cards)

    if switch_over:
        dealer_plays(dealer, human_player, playing_cards)

    playing_cards.delete_cards()
    del playing_cards


# BLACKJACK


def blackjack():
    human_player_name = input('Enter Player name\t')
    chips = get_valid_input('Enter your chips amount::  ')

    replay = True
    while replay:
        human_player = Player(human_player_name, chips)
        human_player.show_balance_in_account()

        bet = get_valid_input('Enter your betting amount::  ')
        sufficient_balance = human_player.make_bet(bet)

        if sufficient_balance:
            dealer = Player('Computer')

            play_game(human_player, dealer)
            results((human_player, dealer))

            human_player.update_balance()
            chips = human_player.balance
            human_player.show_balance_in_account()

            del human_player, dealer
        else:
            print('Quitting this session of game....')


        print('Do you want to replay??\nPress "y" for yes......')
        response = input()
        if response != "y":
            replay = False


blackjack()
