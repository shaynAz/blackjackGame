# blackjack.py: a simple blackjack game.
import random
import sys

# The main function of the game.


def main():
    round = round_begin()
    while True:
        player_round = p_round(round[0])
        host_round = h_round(round[1])
        round_result = win_condition(player_round, host_round)
        vault = result(round_result, round[2], round[3])
        play = input("Enter PLAY to go again, or nothing to quit: ")
        if play == "PLAY":
            round = round_begin(vault)
            continue
        else:
            print(f"Your vault was {round[2]}.")
            break
    print(f"Thanks for playing!")
    q = input("press enter to quit.")
    sys.exit()

# Calls for the function which asks for vault (if 0 or None) and wager, and the functions which draw the host's and player's hand.


def round_begin(v=0):
    vault, wager = wager_vault(v)
    vault -= wager
    host_hand = host_cards()
    player_hand = player_cards()
    return player_hand, host_hand, vault, wager

# Function that draws from the deck.


def deck_draw():
    deck = {
        "ace": 11,
        "king": 10,
        "queen": 10,
        "jack": 10,
        "ten": 10,
        "nine": 9,
        "eight": 8,
        "seven": 7,
        "six": 6,
        "five": 5,
        "four": 4,
        "three": 3,
        "two": 2,
        "one": 1
    }
    return random.choice(list(deck.values()))

# Function that draws host's hand.


def host_cards():
    host = [deck_draw(), deck_draw()]
    print(f"The host has drawn to cards. first one is {host[0]}")
    return host

# Function that draws player's hand.


def player_cards():
    player = [deck_draw(), deck_draw()]
    print(f"Your cards are {player[0]}, {player[1]}.")
    return player

# Function that asks for vault (if vault is 0/None) and the player's wager.


def wager_vault(vault=0):
    if not vault:
        vault = int(
            input("Welcome to a game of blackjack! Please enter your vault's value: "))
    wager = int(input("Enter your bet: "))
    while wager > vault:
        wager = int(input(
            "Your wager must be lower than or equal to your vault's value. Enter your bet: "))
    return vault, wager

# Function that asks for player's action: hit or stay. It also return True or False if the player busts or gets bj. Else it returns the new hand.


def p_round(hand):
    while True:
        player_choice = input("What would you like to do? (Hit/Stay) ").lower()
        while player_choice not in ["hit", "stay"]:
            player_choice = input(
                "Invalid choice. What would you like to do? (Hit/Stay) ").lower()
        if player_choice == "hit":
            hand.append(deck_draw())
            print(f"Your hand is: {hand}")
            if sum(hand) == 21:
                print(f"Blackjack!")
                return True
            elif sum(hand) > 21:
                print("Busted!")
                return False
        else:
            print(f"Player chooses to stay!")
            return hand

# Function that draws for host if sum of host's hand < 17 and returns True/False if host bjs or busts. Else returns the new hand.


def h_round(hand):
    print(f"Host's hand is: {hand}")
    while sum(hand) < 17:
        hand.append(deck_draw())
        print(f"Host draws {hand[-1]}. His cards: {hand}")
        if sum(hand) == 21:
            print(f"Host gets Blackjack!")
            return True
        elif sum(hand) > 21:
            print("Host is Busted!")
            return False
        else:
            continue
    return hand

# Checks for the winning/losing condition of the round. First checks player's bust/bj, then host's, then compares the sum of each hand and check for the winner.


def win_condition(player_round, host_round):
    if player_round == True:
        return True
    elif player_round == False:
        return False
    else:
        if host_round == True:
            return False
        elif host_round == False:
            return True
        else:
            if sum(host_round) > sum(player_round):
                return False
            elif sum(host_round) < sum(player_round):
                return True
            else:
                return None

# Updates the vault based on the result of the round,


def result(player_win, vault, wager):
    if player_win == True:
        vault += (wager*2)
        print(f"You've won this round! your vault is now {vault}")
    elif player_win == False:
        print(f"You've lost this round! your vault is now {vault}")
    else:
        vault += wager
        print(f"This round is a push! your vault is now {vault}")
    return vault


if __name__ == "__main__":
    main()
