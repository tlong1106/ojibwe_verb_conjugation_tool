from enum import Enum

from .constants import Clause, Negation, Pronoun, Vowels, VerbEndingVII
from .models import ConjugationInput

# --- 1. Constants:

DUMMY_N = (
    "agaasademon",
    "akwamon",
    "animamon",
    "animipon",
    "azhashkiiwaagamin",
    "aazhawamon",
    "aazhawaandawemon",
    "aazhoomon",
    "babaamipon",
    "babigwaagamin",
    "babiikwadamon",
    "bagakaagamin",
    "bagamipon",
    "bakemon",
    "bakobiimon",
    "bakobiiyaabiigamon",
    "bakwebiigamin",
    "bangishimon",
    "bazagwaagamin",
    "baapaagadamon",
    "baashkadaawangamon",
    "bengopon",
    "bimamon",
    "bimaabiigamon",
    "bimidewaagamin",
    "bimipon",
    "biijipon",
    "biinaagamin",
    "biindigepon",
    "biinisaagamin",
    "biisipon",
    "biitewaagamin",
    "biiwipon",
    "boonipon",
    "boozaagamin",
    "dagon",
    "dagwaagin",
    "dakaagamin",
    "dakigamin",
    "dakipon",
    "dakwamon",
    "gibaakwadin",
    "gibichipon",
    "ginoomon",
    "gizhaagamin",
    "giiwitaamon",
    "giizhowaagamin",
    "giizhoogamin",
    "gopamon",
    "inamon",
    "inaabiigamon",
    "inaagamin",
    "inigokwademon",
    "ishkwaapon",
    "ishpi-dagwaagin",
    "izhipon",
    "jiigeweyaazhagaamemon",
    "jiikaagamin",
    "madaabiimon",
    "madaagamin",
    "makadewaagamin",
    "mamaangadepon",
    "mamaangipon",
    "mangademon",
    "mashkawaagamin",
    "maajipon",
    "maanadamon",
    "maanamon",
    "maanaagamin",
    "maazhimaagwaagamin",
    "minwamon",
    "minwaagamin",
    "miskwaagamin",
    "miskwiiwaagamin",
    "mishkawaagamin",
    "naazibiimon",
    "nibiiwaagamin",
    "ningwaagonemon",
    "niingidoomon",
    "niiskaajipon",
    "nookaagamin",
    "ogidaakiiwemon",
    "onaagoshin",
    "ondadamon",
    "ondamon",
    "onjipon",
    "ozhaashadamon",
    "ozhaashamon",
    "ozhaawashkwaagamin",
    "ozaawaagamin",
    "washkadamon",
    "waabishkaagamin",
    "waakamin",
    "wekwaamon",
    "wiinaagamin",
    "wiisagaagamin",
    "wiishkobaagamin",
    "zanagamon",
    "ziiwiskaagamin",
    "zoogipon",
    "zhakipon",
    "zhaagwaagamin",
    "zhiiwaagamin",
    "zhiiwitaaganaagamin"
)

VII_SUFFIX_MAP = {
    Clause.INDEPENDENT_CLAUSE: {
        Negation.AFFIRMATIVE: {
            VerbEndingVII.D: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "ini",
                Pronoun.THIRD_PLURAL_INANIMATE: "oon",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "iniwan"
            },
            VerbEndingVII.N: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "ini",
                Pronoun.THIRD_PLURAL_INANIMATE: "oon",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "iniwan"
            },
            VerbEndingVII.VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "ni",
                Pronoun.THIRD_PLURAL_INANIMATE: "wan",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "niwan"
            }
        },
        Negation.NEGATIVE: {
            VerbEndingVII.D: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "sinoon",
                Pronoun.THIRD_PLURAL_INANIMATE: "sinoon",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "sinini",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "sininiwan"
            },
            VerbEndingVII.N: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "zinoon",
                Pronoun.THIRD_PLURAL_INANIMATE: "zinoon",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "zinini",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "zininiwan"
            },
            VerbEndingVII.VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "sinoon",
                Pronoun.THIRD_PLURAL_INANIMATE: "sinoon",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "sinini",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "sininiwan"
            }
        }
    },
    Clause.DEPENDENT_CLAUSE: {
        Negation.AFFIRMATIVE: {
            VerbEndingVII.D_N: {
                VerbEndingVII.D: {
                    Pronoun.THIRD_SINGULAR_INANIMATE: "k",
                    Pronoun.THIRD_PLURAL_INANIMATE: "k"
                },
                VerbEndingVII.N: {
                    Pronoun.THIRD_SINGULAR_INANIMATE: "g",
                    Pronoun.THIRD_PLURAL_INANIMATE: "g",
                    Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "inig",
                    Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "inig"
                }
            },
            VerbEndingVII.VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "g",
                Pronoun.THIRD_PLURAL_INANIMATE: "g",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "nig",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "nig"
            }
        },
        Negation.NEGATIVE: {
            VerbEndingVII.D: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "sinog",
                Pronoun.THIRD_PLURAL_INANIMATE: "sinog",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "sininig",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "sininig"
            },
            VerbEndingVII.N: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "zinog",
                Pronoun.THIRD_PLURAL_INANIMATE: "zinog",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "zininig",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "zininig"
            },
            VerbEndingVII.VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "sinog",
                Pronoun.THIRD_PLURAL_INANIMATE: "sinog",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "sininig",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "sininig"
            }
        }
    }
}

# --- 2. Helpers:

def get_suffix(clause: str | Enum, negation: bool | Enum, verb_ending: str | Enum, pronoun: str, key = None) -> str:
    if key:
        return VII_SUFFIX_MAP.get(clause, {}).get(negation, {}).get(verb_ending, {}).get(key, {}).get(pronoun, "")
    return VII_SUFFIX_MAP.get(clause, {}).get(negation, {}).get(verb_ending, {}).get(pronoun, "")

def ends_with_d_or_n(verb: str) -> bool:
    return verb.endswith((str(VerbEndingVII.D.value), str(VerbEndingVII.N.value)))

def ends_with_vowel(verb: str) -> bool:
    return any(verb.endswith(v) for v in Vowels.VOWEL.value)

def remove_final_letter(verb: str) -> str:
    return verb[:-1]

# --- 3. Rule Interface and Implementation:

class DependentAffirmativeRule:
    def matches(self) -> bool:
        raise NotImplementedError

    def apply(self) -> tuple[str, str]:
        raise NotImplementedError
    
class DummyNDepAffirm(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb in DUMMY_N
    
    def apply(self, verb, pronoun):
        if pronoun in (Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE, Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE):
            return remove_final_letter(verb), get_suffix(Clause.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.VOWEL, pronoun)
        else:
            return remove_final_letter(verb), get_suffix(Clause.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.D_N, pronoun, key = VerbEndingVII.N)
    
class EndDDepAffirm1(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(VerbEndingVII.D) and pronoun in (Pronoun.THIRD_SINGULAR_INANIMATE, Pronoun.THIRD_PLURAL_INANIMATE)
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Clause.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.D_N, pronoun, key = VerbEndingVII.D)
    
class EndDDepAffirm2(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(VerbEndingVII.D) and pronoun in (Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE, Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE,VerbEndingVII.D_N, pronoun, key = VerbEndingVII.N)

class EndNDepAffirm(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(VerbEndingVII.N)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.D_N, pronoun, key = VerbEndingVII.N)

class EndVowelDepAffirm(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return ends_with_vowel(verb)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.VOWEL, pronoun)

# - - -

class DependentNegativeRule:
    def matches(self) -> bool:
        raise NotImplementedError
    
    def apply(self) -> tuple[str, str]:
        raise NotImplementedError
    
class DummyNDepNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb in DUMMY_N
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Clause.DEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.D, pronoun)
    
class EndDDepNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(VerbEndingVII.D)
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Clause.DEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.D, pronoun)

class EndNDepNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(VerbEndingVII.N)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.DEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.N, pronoun)
    
class EndVowelDepNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return ends_with_vowel(verb)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.DEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.VOWEL, pronoun)

# - - -

class IndependentAffirmativeRule:
    def matches(self) -> bool:
        raise NotImplementedError

    def apply(self) -> tuple[str, str]:
        raise NotImplementedError
    
class DummyNIndAffirm(IndependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb in DUMMY_N

    def apply(self, verb, pronoun):
        if pronoun == Pronoun.THIRD_SINGULAR_INANIMATE:
            return verb, get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.VOWEL, pronoun)
        return remove_final_letter(verb), get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.VOWEL, pronoun)
    
class EndDorNIndAffirm(IndependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return ends_with_d_or_n(verb)

    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.D, pronoun)
    
class EndVowelIndAffirm(IndependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return ends_with_vowel(verb)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, VerbEndingVII.VOWEL, pronoun)
    
#  - - -

class IndependentNegativeRule:
    def matches(self) -> bool:
        raise NotImplementedError

    def apply(self) -> tuple[str, str]:
        raise NotImplementedError
    
class DummyNIndNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb in DUMMY_N
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.D, pronoun)
    
class EndDIndNeg(IndependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(VerbEndingVII.D)
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.D, pronoun)
    
class EndNIndNeg(IndependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(VerbEndingVII.N)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.N, pronoun)
    
class EndVowelIndNeg(IndependentNegativeRule):
    def matches(self, verb, pronoun):
        return ends_with_vowel(verb)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Clause.INDEPENDENT_CLAUSE, Negation.NEGATIVE, VerbEndingVII.VOWEL, pronoun)

# --- 4. Rule Registry:

DEPENDENT_AFFIRMATIVE_RULES = [
    DummyNDepAffirm(),
    EndDDepAffirm1(),
    EndDDepAffirm2(),
    EndNDepAffirm(),
    EndVowelDepAffirm()
]

DEPENDENT_NEGATIVE_RULES = [
    DummyNDepNeg(),
    EndDDepNeg(),
    EndNDepNeg(),
    EndVowelDepNeg()
]

INDEPENDENT_AFFIRMATIVE_RULES = [
    DummyNIndAffirm(),
    EndDorNIndAffirm(),
    EndVowelIndAffirm()
]

INDEPENDENT_NEGATIVE_RULES = [
    DummyNIndNeg(),
    EndDIndNeg(),
    EndNIndNeg(),
    EndVowelIndNeg()
]

# --- 5. Main Logic Functions:

def handle_dependent(verb: str, negation: bool, pronoun: str) -> tuple[str, str]:
    if negation == Negation.AFFIRMATIVE:
        return handle_dependent_affirmative(verb, pronoun)
    else:
        return handle_dependent_negative(verb, pronoun)
    
def handle_dependent_affirmative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in DEPENDENT_AFFIRMATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def handle_dependent_negative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in DEPENDENT_NEGATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

# - - -

def handle_independent(verb: str, negation: bool, pronoun: str) -> tuple[str, str]:
    if negation == Negation.AFFIRMATIVE:
        return handle_independent_affirmative(verb, pronoun)
    else:
       return handle_independent_negative(verb, pronoun)
    
def handle_independent_affirmative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in INDEPENDENT_AFFIRMATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def handle_independent_negative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in INDEPENDENT_NEGATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def get_vii_suffix(input_data: ConjugationInput) -> dict:
    """
    Accepts verb with 'clause', 'negation' and 'pronoun' variables
    Modifies the verb (if necessary) to create a 'root' and determines 'suffix'
    Returns a dictionary that contains 'root' and 'suffix'
    """

    verb_type = "vii"
    verb = input_data.verb
    verb_clause = input_data.verb_clause
    verb_negation = input_data.verb_negation
    verb_pronoun = input_data.verb_pronoun

    if verb_type != "vii":
        verb_data = {"root": verb, "suffix": ""}
        return verb_data
    
    if verb_clause == Clause.DEPENDENT_CLAUSE:
        verb, suffix = handle_dependent(verb, verb_negation, verb_pronoun)
        verb_data = {"root": verb, "suffix": suffix}
        return verb_data
    elif verb_clause == Clause.INDEPENDENT_CLAUSE:
        verb, suffix = handle_independent(verb, verb_negation, verb_pronoun)
        verb_data = {"root": verb, "suffix": suffix}
        return verb_data
    else: # replace print() to log errors
        print("Neither Independent, Dependent Clause!")