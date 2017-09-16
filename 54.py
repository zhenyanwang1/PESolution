from collections import Counter


def val_to_int(card):
    trans = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    return trans[card]


def RF(hand):
    return hand.pattern([10, 11, 12, 13, 14]) and hand.same_suit(), None


def SF(hand):
    if not hand.same_suit():
        return False, None
    ret = hand.pattern(list(range(hand[0].value, hand[0].value + 4 + 1)))
    if ret:
        return ret, hand[4]
    return False, None


def FK(hand):
    for item in dict(Counter(hand)).items():
        if item[1] == 4:
            return True, item[0]
    return False, None


def FH(hand):
    counts = dict(Counter(hand))
    if not 2 in counts.values():
        return False, None
    for item in counts.items():
        if item[1] == 3:
            return True, item[0]
    return False, None


def F(hand):
    return hand.same_suit(), hand[0]


def S(hand):
    ret = hand[1] - hand[0] == 1 and hand[2] - hand[1] == 1 and hand[3] - hand[2] == 1 and hand[4] - hand[3] == 1
    if ret:
        return ret, hand[4]
    return False, None


def TK(hand):
    for item in dict(Counter(hand)).items():
        if item[1] == 3:
            return True, item[0]
    return False, None


def TP(hand):
    pair_count = 0
    pairs = []
    for item in dict(Counter(hand)).items():
        if item[1] == 2:
            pair_count += 1
            pairs.append(item[0])
    if pair_count == 2:
        return True, max(pairs)
    return False, None


def OP(hand):
    for item in dict(Counter(hand)).items():
        if item[1] == 2:
            return True, item[0]
    return False, None


def HC(hand):
    return True, hand[4]


def classify(hand):
    conds = [("RF", 10), ("SF", 9), ("FK", 8), ("FH", 7), ("F", 6), ("S", 5), ("TK", 4), ("TP", 3), ("OP", 2), ("HC", 1)]
    for cond in conds:
        ret = eval("{cond}(hand)".format(cond=cond[0]))
        if ret[0]:
            return cond, ret[1]


class Card:
    def __init__(self, s):
        print(s)
        self.value = val_to_int(s[0])
        self.suit = s[1]

    def __sub__(self, other):
        return self.value - other.value

    def __eq__(self, other):
        if type(other) == int:
            return self.value == other
        return self.value == other.value

    def __int__(self):
        return self.value

    def __hash__(self):
        return self.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return str(self.value) + self.suit


class Rank:
    conv = []

    def __init__(self, hand):
        self.rank, self.card = classify(hand)

    def __str__(self):
        return self.rank[0] + str(self.rank[1]) + " " + str(self.card)

    def __lt__(self, other):
        if self.rank[1] == other.rank[1]:
            return self.card < other.card
        return self.rank[1] < other.rank[1]

    def __gt__(self, other):
        if self.rank[1] == other.rank[1]:
            return self.card > other.card
        return self.rank[1] > other.rank[1]

    def __eq__(self, other):
        if self.rank[1] == other.rank[1]:
            return self.card == other.card
        return self.rank[1] == other.rank[1]


class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, key=lambda card: card.value)
        self.rank = Rank(self)

    def __getitem__(self, item):
        return self.cards[item]

    def pattern(self, pat):
        for t in zip(self.cards, pat):
            if t[0].value != t[1]:
                return False
        return True

    def partial_pattern(self, pat):
        for startpos in range(len(self.cards) - len(pat) + 1):
            return [card.value for card in self.cards[startpos:startpos + len(pat)]] == pat

    def same_suit(self):
        return self.cards[0].suit == self.cards[1].suit == self.cards[2].suit == self.cards[3].suit == self.cards[4].suit

    def __str__(self):
        return " ".join([str(card) for card in self.cards]) + " [" + str(self.rank) + "]"

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank


def determine(hand1, hand2):
    vals1 = sorted(hand1, key=lambda card: card.value, reverse=True)
    vals2 = sorted(hand2, key=lambda card: card.value, reverse=True)
    for pos in range(0, 5):
        if vals1[pos] > vals2[pos]:
            return 1
        if vals1[pos] < vals2[pos]:
            return 2
        if vals1[pos] == vals2[pos]:
            continue
    return 0


def d(hand1, hand2):
    h1c = classify(hand1)
    h2c = classify(hand2)
    print(hand1, hand2)
    if h1c > h2c:
        return 1
    elif h1c < h2c:
        return 2
    else:
        dv = determine(hand1, hand2)
        if dv == 0:
            raise Exception
        else:
            if dv == 1:
                return 1
            elif dv == 2:
                return 2


if __name__ == "__main__":
    tie1 = 0
    tie2 = 0
    w1 = 0
    w2 = 0
    for l in open("poker.txt"):
        l = l[0:-1]
        hand = l.split(" ")
        p1 = hand[0:5]
        p2 = hand[5:10]
        h1 = Hand([Card(s) for s in p1])
        h2 = Hand([Card(s) for s in p2])
        if h1 > h2:
            w1 += 1
        elif h1 < h2:
            w2 += 1
        else:
            print("Tie!")
            print(h1, h2)
    print(w1, w2)

    # The hands
    # 3S 5D 5H 6D 7C [OP2 5D] 2H 3D 5C 5S 11C [OP2 5C]
    # ties.
