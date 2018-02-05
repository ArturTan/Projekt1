#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import re
from collections import Counter


class Hackerman():

    """Auxiliary class that uses method of counting powers"""

    def __init__(self, hack):

        self.hack = hack
        self.letters = {"a": 1, "b": 2, "c": 3}
        self.phrases = {"ba": 10, "baa": 20}

    def letter_power_counter(self):

        """Counting power of letters
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

        """Counting power of phrases"""

        # Due to the fact that we have only two phrases in the set of phrases
        # the regex pattern should be enough to achieve the goal of the program.
        # Regex pattern will recognize first all "baa" which have more power than "ba".

        # For more advanced solution with customized_hack_power

        pattern = re.compile("(baa|ba)")
        results = pattern.findall(self.hack)
        count = Counter(results)

        return sum([self.phrases[key] * count[key] for key in count.keys()])


def hack_calculator(hack="", letters={}, phrases={}):
    """Return the maximal power of the hack phrase.

    Computes the power of the given hack phrase on basis of 
    the dictionary of letters and phrases having assigned values:

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

    hackbreaker = Hackerman(hack)
    letter_power = hackbreaker.letter_power_counter()

    if not letter_power:
        power = 0
    else:
        power = int(letter_power + hackbreaker.phrase_power_counter())

    print("Power:\t", power)
    return power

if __name__ == "__main__":
    hack_calculator(hack="advantage")

