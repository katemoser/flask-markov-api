import random


class MarkovMachine:
    """Make a markov machine out of a string

    Separate seeds must be separated by the "@" sign.

    """

    def __init__(self, text):
        # text_with_newlines = self.format_text(text)
        self.words = self.format_text(text).split()
        self.first_words = []
        self.chains = self.get_chains()

    def format_text(self, text):
        lines = text.splitlines()
        return 'newline '.join(lines)

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
            print(chains)
        return chains

    def get_text(self):
        """ get a randomly generated text from the stored chains"""

        # let starting word be a random selection from the first words
        current_word = random.choice(self.first_words)
        output = []
        while current_word is not None:
            output.append(current_word)
            current_word = random.choice(self.chains[current_word])

        # preserves newlines
        text = ' '.join(output)
        lines = text.split("newline")
        return '\n '.join(lines)


# Experimental configurable mm

class MegaMarkovMachine:
    """
    texts is a list of texts: ["text one", "text two"]

    config is a dict like:
    {
        ratio: [2,8] => meaning the second text will show up a lot more
    }
    """

    def __init__(self, texts, config):
        self.texts = self.format_texts(texts)
        self.config = config
        self.first_words = []
        self.chains = {}

        self.make_chains()
        print(self.chains)

    def format_texts(self, texts):
        formatted_texts = []
        for text in texts:
            formatted_texts.append('newline '.join(text.splitlines()))
        return formatted_texts

    def make_chains(self):
        """
        creates chains according to config with multiple texts
        """
        for idx, text in enumerate(self.texts):
            self.add_text_single(text, self.config["ratio"][idx])

    def add_text_single(self, text, amount):
        """
        add one text to chains, single link
        """

        # add first word to firstwords
        # create markov chains, with None at the end
        words = text.split()
        for x in range(amount):
            self.first_words.append(words[0])

        for idx, current_word in enumerate(words):
            if idx < len(words) - 1:
                next_word = words[idx + 1]
            # if it's the last word, add None to chain
            else:
                next_word = None

            if current_word not in self.chains:
                self.chains[current_word] = []
            # add word a number of times, to allow for words from one poem to
            # be used more often
            for x in range(amount):
                self.chains[current_word].append(next_word)

    def add_text_to_existing(self, text, amount):
        """
        add one text to chains, single link

        currently not in use
        """

        # add first word to firstwords
        # create markov chains, with None at the end
        words = text.split()
        # for x in range(amount):
        #     self.first_words.append(words[0])

        for idx, current_word in enumerate(words):
            if idx < len(words) - 1:
                next_word = words[idx + 1]
            # if it's the last word, add None to chain
            else:
                next_word = None

            if current_word not in self.chains:
                break
                # self.chains[current_word] = []
            # add word a number of times, to allow for words from one poem to
            # be used more often
            for x in range(amount):
                self.chains[current_word].append(next_word)

    def add_text_bigrams(words, amount):
        """
        add one text to chains with bigrams
        """
        ...

    def get_text(self):
        """ get a randomly generated text from the stored chains"""

        # let starting word be a random selection from the first words
        current_word = random.choice(self.first_words)
        output = []
        while current_word is not None:
            output.append(current_word)
            current_word = random.choice(self.chains[current_word])

        # preserves newlines
        text = ' '.join(output)
        print("TEXT BEFORE COLOR CODING", text)

        # if we there are seeds, color code it
        # TODO: We want to change this to a config option!
        if self.texts:
            text = self.color_code_text(text)

        print("TEXT after COLOR CODING", text)
        lines = text.split("newline")
        return '\n'.join(lines)

    def color_code_text(self, text):
        """
        color codes a text depending on which poems the text appears in

        TODO: update this so that any words that don't appear in the sets
        are not in span
        """

        def _color_code(words):
            # base case -- if no words, return empty string
            if not words:
                return ""

            label = _get_label(words[0])
            streak = []

            # let's get this working and then make it more performant
            for index, word in enumerate(words):
                if _get_label(word) == label:
                    streak.append(word)
                else:
                    rest = words[index:]
                    break

            #This is very cool -- you can give a for loop an else statement
            # if there is a break statement in the for loop.
            # the else clause will only execute if we run through the for loop
            # without encountering the break statement.
            else:
                rest = []

            #check if we are in the last streak (end of words list)
            # if so, empty words

            color_coded_streak = f"<span class='{label}' > {' '.join(streak)} </span>"

            return color_coded_streak + " " + _color_code(rest)


        def _get_label(word):
            if word in set1 and word in set2:
                return "both"
            elif word in set1:
                return "set1"
            elif word in set2:
                return "set2"
            else:
                return "none"

        set1 = set(self.texts[0].split(" "))
        set2 = set(self.texts[1].split(" "))

        print("SEED SETS BEFORE COLOR CODING")
        print("SET 1:", set1)
        print("SET 2:", set2)

        words = text.split(" ")

        color_coded_text = _color_code(words)

        print("COLOR CODED TEXT: ", color_coded_text)

        return color_coded_text

