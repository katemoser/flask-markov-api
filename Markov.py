import random


class MarkovMachine:
    """Make a markov machine out of a string"""

    def __init__(self, text):
        self.words = text.split()
        # self.first_words = []
        self.chains = self.get_chains()
    
    def get_chains(self):
        chains = {}
        for idx, current_word in enumerate(self.words):
            if idx < len(self.words) - 1:
                next_word = self.words[idx + 1] 
            else:
                next_word = None

            if current_word not in chains:
                chains[current_word] = []
            chains[current_word].append(next_word)
        return chains

    def get_text(self):
        current_word = self.words[0]
        output = []
        while current_word is not None:
            output.append(current_word)
            randomIndex = random.randint(0, len(self.chains[current_word])-1)
            current_word = self.chains[current_word][randomIndex]
        return ' '.join(output)
