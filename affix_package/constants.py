from enum import Enum

class Clause(str, Enum):
    INDEPENDENT_CLAUSE = "Independent"
    DEPENDENT_CLAUSE = "Dependent"

class Consonants(tuple, Enum):
    SINGLE_CONSONANT = ("b", "d", "g", "h", "'", "j", "k", "m", "n", "p", "s", "t", "w", "y", "z")
    DOUBLE_CONSONANT = ("ch", "sh", "zh")

class Negation(str, Enum):
    AFFIRMATIVE = True
    NEGATIVE = False

class Pronoun(str, Enum):
    THIRD_SINGULAR_INANIMATE = "0s"
    THIRD_PLURAL_INANIMATE = "0p"
    THIRD_SINGULAR_INANIMATE_OBVIATE = "0's"
    THIRD_PLURAL_INANIMATE_OBVIATE = "0'p"

class Vowels(tuple, Enum):
    VOWEL = ("aa", "ii", "oo", "e", "a", "i", "o", "o")
    LONG_VOWEL = ("aa", "e", "ii", "oo")
    SHORT_VOWEL = ("a", "i", "o")

class VerbEndingVII(str, Enum):
    D = "d"
    N = "n"
    D_N = "d_n"
    VOWEL = "vowel"