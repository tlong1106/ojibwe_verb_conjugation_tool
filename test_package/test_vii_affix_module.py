# Notes: from /ojibwe_verb_conjugation_tool, run: python -m pytest test_package/test_vii_affix_module.py

from affix_package.constants import Clause, Negation, Pronoun, Tense
from affix_package.models import ConjugationInput
from affix_package.vii_affix_module import get_vii_suffix

# --- VII 'D' Ending Tests ---

# --- Independent (True statement) ---

def test_d_end_ind_affirm_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanagad", "suffix": ""}

def test_d_end_ind_affirm_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanagad", "suffix": "ini"}

def test_d_end_ind_affirm_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanagad", "suffix": "oon"}

def test_d_end_ind_affirm_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanagad", "suffix": "iniwan"}

# --- Independent (False statement) ---

def test_d_end_ind_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sinoon"}

def test_d_end_ind_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sinini"}

def test_d_end_ind_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sinoon"}

def test_d_end_ind_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sininiwan"}

# --- Dependent (True statement) ---

def test_d_end_dep_pos_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "k"}

def test_d_end_dep_pos_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanagad", "suffix": "inig"}

def test_d_end_dep_pos_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "k"}

def test_d_end_dep_pos_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanagad", "suffix": "inig"}

# --- Dependent (False statement) ---

def test_d_end_dep_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sinog"}

def test_d_end_dep_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sininig"}

def test_d_end_dep_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sinog"}

def test_d_end_dep_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="zanagad",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "zanaga", "suffix": "sininig"}



# --- VII 'N' Ending Tests ---

# --- Independent (True statement) ---

def test_n_end_ind_affirm_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": ""}

def test_n_end_ind_affirm_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "ini"}

def test_n_end_ind_affirm_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "oon"}

def test_n_end_ind_affirm_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "iniwan"}

# --- Independent (False statement) ---

def test_n_end_ind_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zinoon"}

def test_n_end_ind_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zinini"}

def test_n_end_ind_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zinoon"}

def test_n_end_ind_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zininiwan"}

# --- Dependent (True statement) ---

def test_n_end_dep_pos_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "g"}

def test_n_end_dep_pos_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "inig"}

def test_n_end_dep_pos_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "g"}

def test_n_end_dep_pos_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "inig"}

# --- Dependent (False statement) ---

def test_n_end_dep_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zinog"}

def test_n_end_dep_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zininig"}

def test_n_end_dep_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zinog"}

def test_n_end_dep_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="bangisin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "bangisin", "suffix": "zininig"}



# --- VII 'Vowel' Ending Tests ---

# --- Independent (True statement) ---

def test_vowel_end_ind_affirm_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": ""}

def test_vowel_end_ind_affirm_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "ni"}

def test_vowel_end_ind_affirm_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "wan"}

def test_vowel_end_ind_affirm_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "niwan"}

# --- Independent (False statement) ---

def test_vowel_end_ind_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sinoon"}

def test_vowel_end_ind_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sinini"}

def test_vowel_end_ind_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sinoon"}

def test_vowel_end_ind_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sininiwan"}

# --- Dependent (True statement) ---

def test_vowel_end_dep_pos_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "g"}

def test_vowel_end_dep_pos_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "nig"}

def test_vowel_end_dep_pos_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "g"}

def test_vowel_end_dep_pos_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "nig"}

# --- Dependent (False statement) ---

def test_vowel_end_dep_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sinog"}

def test_vowel_end_dep_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sininig"}

def test_vowel_end_dep_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sinog"}

def test_vowel_end_dep_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="miskwaa",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "miskwaa", "suffix": "sininig"}

# --- VII 'Dummy N' Ending Tests ---

# --- Independent (True statement) ---

def test_dummy_n_end_ind_affirm_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagamin", "suffix": ""}

def test_dummy_n_end_ind_affirm_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "ni"}

def test_dummy_n_end_ind_affirm_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "wan"}

def test_dummy_n_end_ind_affirm_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "niwan"}

# --- Independent (False statement) ---

def test_dummy_n_end_ind_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sinoon"}

def test_dummy_n_end_ind_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sinini"}

def test_dummy_n_end_ind_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sinoon"}

def test_dummy_n_end_ind_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.INDEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sininiwan"}

# --- Dependent (True statement) ---

def test_dummy_n_end_dep_pos_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "g"}

def test_vowel_end_dep_pos_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "nig"}

def test_dummy_n_end_dep_pos_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "g"}

def test_vowel_end_dep_pos_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.AFFIRMATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "nig"}

# --- Dependent (False statement) ---

def test_dummy_n_end_dep_neg_0s():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sinog"}

def test_dummy_n_end_dep_neg_0s_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sininig"}

def test_dummy_n_end_dep_neg_0p():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sinog"}

def test_dummy_n_end_dep_neg_0p_obv():
    input_data = ConjugationInput(
                            verb_type="vii",
                            verb="dakaagamin",
                            verb_negation=Negation.NEGATIVE,
                            verb_clause=Clause.DEPENDENT_CLAUSE,
                            verb_pronoun=Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE,
                            verb_tense=Tense.PRESENT
                        )
    
    assert get_vii_suffix(input_data) == {"root": "dakaagami", "suffix": "sininig"}

