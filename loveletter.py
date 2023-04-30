import numpy as np
from random import choice

# blank guard priest baron maid prince king countess princess
# cardcounts = [0, 5, 2, 2, 2, 2, 1, 1, 1]
deck1 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
deck = deck1


def draw(alist):
    temp = choice(alist)
    alist.remove(temp)
    return temp


def countupdater(alist):
    '''
    turns cardlist into cardcounts
    '''
    return [0, alist.count(1), alist.count(2), alist.count(3), alist.count(4), alist.count(5), alist.count(6), alist.count(7), alist.count(8)]


class hand:  # actions are deterministic
    win_counter = 0

    def __init__(self, card1, card2, maid, oppcard, rem, known):
        self.cards = [np.min([card1, card2]), np.max([card1, card2])]
        self.maid = maid  # opponent immune?
        self.oppcard = oppcard  # opponent card
        self.rem = rem  # remaining cards INCLUDING cards currently in hand
        self.known = known  # is opponent's card known?
        self.rem[card1] = self.rem[card1] - 1  # updating remaining
        self.rem[card2] = self.rem[card2] - 1
        print('cards:', card1, card2, self.cards)

    def guardguess(self):
        if not self.known:
            guesslist = self.rem
            guesslist[1] = 0  # cannot guess guard
            return np.argmax(self.guesslist)
        elif self.oppcard != 1:
            return self.oppcard
        else:
            return 0  # guess when opponent has a guard

    def play(self):
        if 8 in self.cards:  # never play princess
            # print('a:', self.cards[0], '\n')
            return self.cards[0]
        if self.cards[0] == self.cards[1]:  # trivial case
            # print('b:', self.cards[0], '\n')
            return self.cards[0]
        if self.cards[1] == 7 & self.cards[0] >= 5:  # countess rules
            return 7
        if self.maid:
            if 4 in self.cards:  # maid still works
                return 4
            else:
                # print('c:', self.cards[0], '\n')
                return self.cards[0]
        else:
            # definite wins
            if self.known:  # if known
                if self.cards[0] == 1 & self.oppcard != 1:  # guard win
                    return 1
                temp = self.cards
                temp.remove(3)
                if 3 in self.cards & self.oppcard < temp[0]:  # baron win
                    return 3
                if self.oppcard == 8 & 5 in self.cards:  # prince win
                    return 5
            if 3 in self.cards:
                temp = self.cards
                temp.remove(3)
                if np.max(np.nonzero(self.rem)) < temp[0]:
                    return 3  # if remaining cards are lower than !baron

            # baron probable win
            if 3 in self.cards:
                other = self.cards
                other.remove(3)[0]
                prob = sum(self.rem[0:other]) / sum(self.rem)
                if prob > .6:
                    return 3

            if 2 in self.cards:
                return 2
            if 1 in self.cards:
                return 1
            if 4 in self.cards:
                return 4
            # print('d:', self.cards[0], '\n')
            return self.cards[0]


def resolution(hand1, hand2):
    global deck, realdeck
    played = hand1.play()
    owncard = hand1.cards
    owncard.remove(played)
    print('owncard', owncard)
    owncard = owncard[0]
    print(hand1.oppcard)
    _maid = 0
    _known = hand1.known
    _oppcard = hand1.oppcard
    if played == 8:
        hand2.win_counter += 1
        return 0  # end
    if played == 4:
        _maid == 1
    if not hand1.maid:
        if played == 1:
            if hand1.guardguess == hand1.oppcard:
                hand1.win_counter += 1
            return 0  # end
        if played == 2:
            _known == 1
        if played == 3:
            if owncard > hand1.oppcard:
                hand1.win_counter += 1
                return 0  # end
            elif owncard < hand1.oppcard:
                hand2.win_counter += 1
                return 0  # end
            else:
                _known == 1
        if played == 5 & hand1.oppcard == 8:
            hand1.win_counter += 1
            return 0  # end
        if played == 5:
            deck.remove(hand1.oppcard)
            _known == 0
            _oppcard = draw(realdeck)
        if played == 6:
            _oppcard == owncard
            owncard == hand1.oppcard
            _known == 1
            hand2.known == 1
    # print(deck)
    # print(realdeck)
    print('played', played)
    deck.remove(played)
    hand2.__init__(_oppcard, 0, hand2.maid, owncard, countupdater(deck), hand2.known)
    hand1.__init__(owncard, 0, _maid, _oppcard, countupdater(deck), _known)


def game():
    global deck, realdeck
    realdeck = deck
    hidden = draw(realdeck)
    print(hidden, 'set aside')
    p1start = draw(realdeck)  # current card of p1
    p2start = draw(realdeck)  # current card of p2

    p1 = hand(p1start, 0, 0, p2start, countupdater(deck), 0)
    p2 = hand(p2start, 0, 0, p1start, countupdater(deck), 0)
    _tic = 0

    while len(realdeck) > 0:
        _tic += 1
        newcard = draw(realdeck)
        if _tic % 2 == 0:
            print('p2cards', p2.cards)
            p2.__init__(p2.cards[np.nonzero(p2.cards)[0][0]], newcard, p2.maid, p2.oppcard, p2.rem, p2.known)
            resolution(p2, p1)
        else:
            print('p1cards', p1.cards)
            p1.__init__(p2.cards[np.nonzero(p1.cards)[0][0]], newcard, p1.maid, p1.oppcard, p1.rem, p1.known)
            resolution(p1, p2)
        if p1.win_counter == 1:
            print('p1 wins')
            break
        if p2.win_counter == 1:
            print('p2 wins')
            break
    if len(realdeck) == 0:
        print('ran outta cards')


game()
