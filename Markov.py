import random


class MarkovMachine:
    """Make a markov machine out of a string
    
    Separate seeds must be separated by the "@" sign.
    
    """

    def __init__(self, text):
        self.words = text.split()
        self.first_words = []
        self.chains = self.get_chains()
    
    def get_chains(self):
        chains = {}
        # add first word to first words
        self.first_words.append(self.words[0])
        for idx, current_word in enumerate(self.words):
            if idx < len(self.words) - 1:
                if self.words[idx + 1] == "@":
                    # this is a terminal word. 
                    # we want to push None to the chain
                    # put the word after the @ into first words
                    # push the index forward
                    next_word = None
                    self.first_words.append(self.words[idx + 2])
                    idx += 1
                else:
                    next_word = self.words[idx + 1] 
            else:
                next_word = None

            if current_word not in chains:
                chains[current_word] = []
            chains[current_word].append(next_word)
        return chains

    def get_text(self):
        # let starting word be a random selection from the first words
        current_word = random.choice(self.first_words)
        output = []
        while current_word is not None:
            output.append(current_word)
            # TODO: Change this random stuff to random.choice()
            # randomIndex = random.randint(0, len(self.chains[current_word])-1)
            current_word = random.choice (self.chains[current_word])
        return ' '.join(output)
