#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import re

from collections import Counter

"""
Return the maximal power of the hack phrase 
with the hack_calculator function"""

class Hackerman(object):

    """
    Auxiliary class that uses method of counting powers
    """
    def __init__(self, hack):

        self.hack = hack
        self.letters = {"a": 1, "b": 2, "c": 3}
        self.phrases = {"ba": 10, "baa": 20}

    def letter_power_counter(self):

        """
        Counting power of letters
        """
        count = Counter(self.hack)
        # Does hack
        try:
            for letter in count.keys():
                import pdb
                n = count[letter]
                # We need to count sum of the all occurences of the given letter
                count[letter] = (n * (n + 1)) / 2 * self.letters[letter]
        except KeyError as e:
            print("KeyError: there is no letter named {} "
                  "in the letter / phrases dict".format(e))
            return 0

        return sum(count.values())

    def phrase_power_counter(self):

        """
        Counting power of phrases"""

        # Due to the fact that we have only two phrases in the set of phrases
        # the regex pattern should be enough to achieve the goal of the program.
        # Regex pattern will recognize first all "baa" which have more power than "ba".

        # For more advanced solution with customized_hack_power

        pattern = re.compile("(baa|ba)")
        results = pattern.findall(self.hack)
        count = Counter(results)

        return sum([self.phrases[key] * count[key] for key in count.keys()])


class RealHackerman(Hackerman):
    """
    Uses the universal approach that binds the possible 
    combinations of the phrases that build the hack
    """
    def __init__(self, hack, letters=None, phrases=None):

        super(RealHackerman, self).__init__(hack)
        if letters:
            self.letters = letters
        if phrases:
            self.phrases = phrases

    def phrase_power_counter(self):

        phrases_list = sorted(list(self.phrases.keys()))
        maximal_sum = count_possible = 0

        phrases_list += " "  # space for indication of letter

        # We excluding situation where the sequence consist solely from the spaces
        repeat = len(self.hack)

        # The entire product amount to phrase_list^repeat
        pools = [tuple(phrases_list)] * repeat

        # List with the sequences that will make up our hack
        shoots = []

        result = [[]]

        def hack_length_checker(x):
            try:
                return self.hack[len("".join(x))]
            except IndexError:
                return " "

        # Customization of the product from itertools library
        for pool in pools:
            result = [x + [y] for x in result for y in pool if (hack_length_checker(x) in y[0] or y == " ")]
            for num, sequence in enumerate(result):
                word = "".join(sequence)
                if len(word) > len(self.hack):
                    del result[num]
                else:
                    word_backup = list(word)
                    for space in re.finditer(" ", word):
                        word_backup[space.start()] = self.hack[space.start()]
                    if not "".join(word_backup) == self.hack[:len(word)]:
                        del result[num]
                    if "".join(word_backup) == self.hack:
                        shoots.append(list(sequence))
                        del result[num]

        for shoot in shoots:
            shoot = [notspace for notspace in shoot if notspace != " "]
            count = Counter(shoot)
            candidat = sum([self.phrases[key] * count[key] for key in count.keys()])
            if maximal_sum < candidat:
                count_possible = count
                maximal_sum = candidat

        if count_possible:
            return maximal_sum
        return 0


def hack_calculator(hack="",
                    letters={},
                    phrases={}):
    """"
    Return the maximal power of the hack phrase.

    Computes the power of the given hack phrase on basis of 
    the dictionary of letters and phrases having assigned values.
    
    The default dictionary is as follow:

    -  letters = {"a": 1, "b": 2,"c": 3},
    -  phrases = {"ba": 10, "baa": 20}

    Each repeated letter in a hack brings more power than its previous iteration. 
    First instance of a letter in a hack is worth base power (for “b” it is 2),
    second instance of the letter is worth 2 times its base power,
    third instance of a letter is worth 3 times its base power, etc.

    Hacks can also contain special phrases that contribute to the hack power

    Each hack uses the maximal power from letters and phrases. Letters
    always contribute to the hack power (even if they are part of a phrase)
    but power of phrases is exclusive (if phrases overlap 
    — only the non-overlapping phrases generate power).

    Parameters
    ---------
    hack: str
        The phrase that power will be calculated

    Returns
    -------
    int
        The number represents the power of hack

    Raises
    -------
    KeyError
        If the hack phrase contains a letter that is not included in
        the letters dictionary. 
    """

    if not isinstance(hack, str):
        raise TypeError("Remember that 'hack' should be a string")

    hackbreaker = RealHackerman(hack, letters, phrases)
    letter_power = hackbreaker.letter_power_counter()

    if not letter_power:
        power = 0
    else:
        power = int(letter_power + hackbreaker.phrase_power_counter())

    print("Power:\t", power)
    return power

if __name__ == "__main__":
    hack_calculator(hack="advantage",
        letters={'a': 1, 'd': 2, 'e': 5,
                 'g': 2, 'n': 1, 't': 4, 'v': 7},
        phrases={"ad": 10, "ant": 13, "age": 24,
                 "van": 13, "tag": 5})

