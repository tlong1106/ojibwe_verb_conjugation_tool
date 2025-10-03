# This file defines the data structure used to hold information about conjugation inputs (form, verb, pronoun, negation, tense).
# Defines structured data using a dataclass.
# Makes input passing cleaner, consistent, and self-documenting.
# May later grow to include validation or more model types.

from dataclasses import dataclass

@dataclass
class ConjugationInput:
    
    # Required when creating an instance.
    verb_type: str
    verb: str
    verb_negation: bool
    
    # Optional when creating an instance. If not passed, will default automatically.
    verb_clause: str = None # <--- change to 'order'?
    verb_pronoun: str = None
    verb_tense: str = None