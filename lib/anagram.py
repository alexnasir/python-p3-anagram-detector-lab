# your code goes here!


class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)
    
    def match(self, possible_anagrams):
        return [word for word in possible_anagrams if sorted(word) == self.sorted_word]
