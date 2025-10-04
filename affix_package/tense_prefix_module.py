from .constants import Pronoun, Tense

CONSONANT_SHIFT_MAP = {
    "zh": "sh",
    "b": "p",
    "d": "t",
    "g": "k",
    "j": "ch",
    "z": "s"
}

TENSE_PREFIX_MAP = {
    Tense.CONDITIONAL: "daa-",
    Tense.FUTURE_DEFINITIVE: ("da-", "ga-"),
    Tense.FUTURE_DESIDERATIVE: "wii-",
    Tense.PAST: "gii-"
}

def consonant_shift(verb: str, tense: str) -> str:
    if tense in (Tense.FUTURE_DESIDERATIVE, Tense.PAST):
        for tense_prefix in CONSONANT_SHIFT_MAP:
            if verb.startswith(tense_prefix):
                replacement = CONSONANT_SHIFT_MAP[tense_prefix]
                return replacement + verb[len(tense_prefix):]
    return verb

def get_tense_prefix(verb_data: dict, pronoun: str, tense: str) -> str:
    """
    Accepts a dictionary containing 'root' and 'suffix'
    Applies consonant shifts (if applicable) to modify 'root'
    Adds 'tense' prefix and returns an updated dictionary
    """

    root = verb_data["root"]

    if tense == Tense.PRESENT:
        verb_data["root"] = root
        verb_data["tense"] = ""
    
    elif tense == Tense.CONDITIONAL:
        verb_data["root"] = consonant_shift(root, tense)
        verb_data["tense"] = TENSE_PREFIX_MAP[Tense.CONDITIONAL]

    elif tense == Tense.FUTURE_DEFINITIVE:
        verb_data["root"] = consonant_shift(root, tense)
        # if pronoun in (Pronoun.THIRD_SINGULAR_ANIMATE, Pronoun.THIRD_PLURAL_ANIMATE): <--- uncomment for vai
        #     verb_data["tense"] = TENSE_PREFIX_MAP[Tense.FUTURE_DEFINITIVE][0]
        # else:
        verb_data["tense"] = TENSE_PREFIX_MAP[Tense.FUTURE_DEFINITIVE][1]
    
    elif tense == Tense.FUTURE_DESIDERATIVE:
        verb_data["root"] = consonant_shift(root, tense)
        verb_data["tense"] = TENSE_PREFIX_MAP[Tense.FUTURE_DESIDERATIVE]
    
    elif tense == Tense.PAST:
        verb_data["root"] = consonant_shift(root, tense)
        verb_data["tense"] = TENSE_PREFIX_MAP[Tense.PAST]

    return verb_data