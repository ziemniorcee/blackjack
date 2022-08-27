import random

bj = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
      '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


def loskart():
    """Returns a random card"""
    card, value = random.choice(list(bj.items()))
    return [card, value]


def points(cards):
    result = 0
    for card in cards:
        result += card[1]

    return result


def showcards(cards):
    result = ""
    x = 0
    for card in cards:
        result += card[0] + ", "
    return result


def aceis(cards):
    x = 0
    for card in cards:
        if card[0] == 'Ace':
            return 1
    return 0


def iface(cards):
    x = 0
    for card in cards:
        if card[0] == 'Ace':
            cards[x][1] = 1
        x += 1
    return cards


def player(play):
    while points(play) < 21:
        decision = input("Type 'y' to get another card, type 'n' to pass: ")
        if decision == 'y':
            play.append(loskart())
        else:
            break
        if points(play) > 21:
            if aceis(play) == 1:
                play = iface(play)
        print(f"Karty gracza: {showcards(play)}co daje {points(play)} punkty")
    return play


def dealer(deal):
    while points(deal) < 17:
        deal.append(loskart())

        if points(deal) > 21:
            if aceis(deal) == 1:
                deal.append(iface(deal))

        print(f"Krupier ma {showcards(deal)}co daje {points(deal)} punkty")
    return deal


def start():
    play = [loskart(), loskart()]

    print(f"Karty gracza: {showcards(play)}co daje {points(play)} punkty")

    deal = [loskart(), ]
    print(f"Krupier ma {showcards(deal)}co daje {points(deal)} punkty")
    return play, deal


def wynik(x, y):
    if y > 21:
        print("Busted. You Win")
    elif y == 21:
        print("Dealer BLACKJACK. You lose")
    elif 21 - x < 21 - y:
        print("You win!")
    elif 21 - x == 21 - y:
        print("Draw!")
    else:
        print("You lose!")


def blackjack():
    gracz, krupier = start()

    gracz = player(gracz)

    if points(gracz) > 21:
        print("Busted. You lost")
    elif points(gracz) == 21:
        print("BLACKJACK. You win")
    else:
        krupier = dealer(krupier)

        wynik(points(gracz), points(krupier))


blackjack()
