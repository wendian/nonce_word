#Wendi An
#Project 1

class Random:
    def __init__(self, seed):
        self.number = seed
    def next(self, range):
        self.number = ((7**5 * self.number) % (2**31 -1))
        return (self.number % range)
    def choose(self, objects):
        return objects[self.next(len(objects))]

class Nonce:
    def __init__(self, seed):
        self.first= []
        self.follow = {}
        self.random = Random(seed)
    def add(self, word):
        self.first += [word[0]]
        for i in range(0, len(word) - 1):
            if word[i] not in self.follow:
                self.follow.update({word[i]: []})
            self.follow[word[i]] += [word[i+1]]
    def make(self, size):
        werd = ""
        werd += self.random.choose(self.first)
        for j in range(0, size -1):
            if werd[j] in self.follow:
                werd += self.random.choose(self.follow[werd[j]])
            else:
                werd += self.random.choose(self.first)
        return werd

nw = Nonce(101) 
nw.add('ada') 
nw.add('algol') 
nw.add('bliss') 
nw.add('ceylon') 
nw.add('clojure') 
nw.add('curl') 
nw.add('dart') 
nw.add('eiffel') 
nw.add('elephant') 
nw.add('elisp') 
nw.add('falcon') 
nw.add('fortran') 
nw.add('go') 
nw.add('groovy') 
nw.add('haskell') 
nw.add('heron') 
nw.add('intercal') 
nw.add('java') 
nw.add('javascript') 
nw.add('latex') 
nw.add('lisp') 
nw.add('mathematica') 
nw.add('nice') 
nw.add('oak') 
nw.add('occam') 
nw.add('pascal') 
nw.add('postscript') 
nw.add('prolog') 
nw.add('python') 
nw.add('ruby') 
nw.add('scala') 
nw.add('scheme') 
nw.add('self') 
nw.add('snobol') 
nw.add('swift') 
nw.add('tex') 
nw.add('wolfram')
print(nw.make(5))  #>>> malgo
print(nw.make(5))  #>>> tisce
print(nw.make(5))  #>>> obyti
print(nw.make(5))  #>>> niffa
print(nw.make(5))  #>>> curca
print(nw.make(5))  #>>> ascex
print(nw.make(5))  #>>> blolc
print(nw.make(5))  #>>> spthe
print(nw.make(5))  #>>> pytis
print(nw.make(5))  #>>> sphem
print(nw.make(5))  #>>> padas
print(nw.make(5))  #>>> pylal
print(nw.make(5))  #>>> screl
print(nw.make(5))  #>>> gocal
print(nw.make(5))  #>>> folon
print(nw.make(5))  #>>> falis
print(nw.make(5))  #>>> selav
print(nw.make(5))  #>>> wocem
print(nw.make(5))  #>>> ogrif
print(nw.make(5))  #>>> heife

#With a seed of 101, the output for this code is the same as the given example output
