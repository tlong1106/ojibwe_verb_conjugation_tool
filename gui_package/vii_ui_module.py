# Notes: from /ojibwe_verb_conjugation_tool, run: python -m gui_package.vii_ui_module

import tkinter as tk
from tkinter import ttk

from affix_package.models import ConjugationInput
from affix_package.constants import Clause, Negation, Pronoun, Tense
from affix_package.vii_affix_module import get_vii_suffix
from affix_package.tense_prefix_module import get_tense_prefix


# --- 1. Helpers ---

def show_colored_verb():
    try:
        verb_type = "vii"
        verb = verb_entry.get().strip().lower()
        clause = clause_var.get()
        negation = negation_var.get()
        pronoun = pronoun_var.get()
        tense = tense_var.get()

        if not verb:
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, "Please enter a verb.", "error_tag")
            return

        # Map string values to Enums
        negation_enum = Negation.AFFIRMATIVE if negation == "Affirmative" else Negation.NEGATIVE
        clause_enum = next(c for c in Clause if c.value == clause)
        pronoun_enum = next(p for p in Pronoun if p.value == pronoun)
        if pronoun_enum is None:
            raise ValueError(f"Invalid pronoun value: {pronoun}")
        print(f"user-selected pronoun: {pronoun_enum}")
        tense_enum = next(t for t in Tense if t.value == tense)

        input_data = ConjugationInput(verb_type, verb, negation_enum, clause_enum, pronoun_enum)
        print(f"input_data: {input_data}")
        result = get_vii_suffix(input_data)
        print(f"get_vii_suffix() output: {result}")
        result = get_tense_prefix(result, pronoun, tense) 
        print(f"get_tense_prefix() output: {result}")

        root_part = result["root"]
        suffix_part = result["suffix"]
        tense_part = result["tense"] 

        # Clear previous text
        text_widget.delete("1.0", tk.END)

        # Dynamic color configuration
        suffix_font = "normal" if clause_enum == Clause.INDEPENDENT_CLAUSE else "italic"
        suffix_color = "green" if negation_enum == Negation.AFFIRMATIVE else "red"
        text_widget.tag_configure("suffix_tag", foreground=suffix_color, font=("Helvetica", 32, f"{suffix_font}"))
        

        # Insert with color tags
        text_widget.insert(tk.END, tense_part, "tense_tag")
        text_widget.insert(tk.END, root_part, "root_tag")
        text_widget.insert(tk.END, suffix_part, "suffix_tag")
        
    except Exception as e:
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, f"Error: {str(e)}", "error_tag")

# --- 2. Main Window ---

root = tk.Tk()
root.title("Southwestern Ojibwe Verb Conjugation App")

# User input for verb
ttk.Label(root, text="Verb:").pack()
verb_entry = ttk.Entry(root, width=40, justify="center")
verb_entry.pack()

# User input for clause
clause_var = tk.StringVar(value="Independent")
ttk.Label(root, text="Clause:").pack()
clause_menu = ttk.OptionMenu(root, clause_var, "Independent", "Independent", "Dependent")
clause_menu.pack()

# User input for negation
negation_var = tk.StringVar(value="Affirmative")
ttk.Label(root, text="Negation:").pack()
negation_menu = ttk.OptionMenu(root, negation_var, "Affirmative", "Affirmative", "Negative")
negation_menu.pack()

# User input for pronoun
pronoun_var = tk.StringVar(value="Third Person Singular Inanimate")
ttk.Label(root, text="Pronoun:").pack()
pronoun_options = [
    "Third Person Singular Inanimate",
    "Third Person Singular Inanimate Obviate",
    "Third Person Plural Inanimate",
    "Third Person Plural Inanimate Obviate"
]
pronoun_menu = ttk.OptionMenu(root, pronoun_var, pronoun_var.get(), *pronoun_options)
pronoun_menu.pack()

# User input for tense
tense_var = tk.StringVar(value="Present")
ttk.Label(root, text="Tense:").pack()
tense_options = [
    "Conditional",
    "Future Definitive",
    "Future Desiderative",
    "Past",
    "Present"
]
pronoun_menu = ttk.OptionMenu(root, tense_var, tense_var.get(), *tense_options)
pronoun_menu.pack()

# Text widget output
text_widget = tk.Text(root, height=2, width=40, font=("Helvetica", 32))
text_widget.pack(pady=10)

# Tags for color, font style
text_widget.tag_configure("root_tag", foreground="black", font=("Helvetica", 32, "normal"), justify="center")
text_widget.tag_configure("tense_tag", foreground="blue", font=("Helvetica", 32, "normal"), justify="center")
text_widget.tag_configure("error_tag", foreground="orange", font=("Helvetica", 32, "italic"), justify="center")

# Conjugate button
btn = ttk.Button(root, text="Conjugate and Show", command=show_colored_verb)
btn.pack()

# Run GUI
root.mainloop()