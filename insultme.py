from random import randint


class InsultGenerator:
    def __init__(self):
        with open('adjectives.txt') as f:
            self.adjectives = f.read().splitlines()
        with open('nouns1.txt') as f:
            self.nouns1 = f.read().splitlines()
        with open('nouns2.txt') as f:
            self.nouns2 = f.read().splitlines()

    def insult_me(self):
        adj = self.adjectives[randint(0, len(self.adjectives))-1]
        noun1 = self.nouns1[randint(0, len(self.nouns1))-1]
        noun2 = self.nouns2[randint(0, len(self.nouns2))-1]
        c = adj[0]
        if c in ['a', 'e', 'i', 'o', 'u']:
            cn = 'an '
        else:
            cn = 'a '
        return 'You\'re just ' + cn + adj + ' ' + noun1 + ' ' + noun2 + '!'


if __name__ == '__main__':
    i = InsultGenerator()
    r = 'y'
    while r[0] != 'q':
        print(i.insult_me())
        r = input() + ' '
