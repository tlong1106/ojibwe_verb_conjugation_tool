# # Notes: from /ojibwe_verb_conjugation_tool, run: python -m gui_package.vii_ui_module

import pandas as pd
import tkinter as tk
from tkinter import font
from tkinter import ttk

from affix_package.models import ConjugationInput
from affix_package.constants import Clause, Negation, Pronoun, Tense
from affix_package.vii_affix_module import get_vii_suffix
from affix_package.tense_prefix_module import get_tense_prefix

# --- 1. Load Lexicon and Helpers ---

# Load and filter lexicon for VII verbs
lexicon = pd.read_csv("C:/Users/tyler/Documents/DA7/ojibwe-projects/ojibwe_verb_conjugation_tool/gui_package/ojibwe-dict.csv")
lexicon = lexicon[lexicon["part of speech"] == "vii"]
dataframe = lexicon[["part of speech", "ojibwe word", "definition"]]

# Function to retrieve definition for a verb
def get_pos_definition(df, user_input):
    for i, word in enumerate(df["ojibwe word"]):
        if word == user_input:
            pos_definition = {
                "part of speech": df["part of speech"].iloc[i],
                "definition": df["definition"].iloc[i]
            }
            return pos_definition
    return None

# Function to conjugate verb and show colored output + definition
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
            definition_widget.delete("1.0", tk.END)
            return

        # Map string values to Enums
        negation_enum = Negation.AFFIRMATIVE if negation == "Affirmative" else Negation.NEGATIVE
        clause_enum = next(c for c in Clause if c.value == clause)
        pronoun_enum = next(p for p in Pronoun if p.value == pronoun)
        tense_enum = next(t for t in Tense if t.value == tense)

        input_data = ConjugationInput(verb_type, verb, negation_enum, clause_enum, pronoun_enum, tense_enum)
        result = get_vii_suffix(input_data)
        result = get_tense_prefix(result, pronoun, tense)

        root_part = result["root"]
        suffix_part = result["suffix"]
        tense_part = result["tense"]

        # Clear previous text
        text_widget.config(state="normal")
        text_widget.delete("1.0", tk.END)

        # Dynamic color configuration
        suffix_font = "normal" if clause_enum == Clause.INDEPENDENT_CLAUSE else "italic"
        suffix_color = "red" if negation_enum == Negation.NEGATIVE else "black"
        text_widget.tag_configure("suffix_tag", foreground=suffix_color, font=("Helvetica", 24, suffix_font))

        # Insert conjugated verb
        text_widget.insert(tk.END, tense_part, "tense_tag")
        text_widget.insert(tk.END, root_part, "root_tag")
        text_widget.insert(tk.END, suffix_part, "suffix_tag")
        text_widget.config(state="disabled")

        # Get and display definition
        definition_widget.config(state="normal")
        definition_widget.delete("1.0", tk.END)
        definition = get_pos_definition(dataframe, verb)
        if definition:
            definition_text = f"({definition['part of speech']}) {definition['definition']}"
            definition_widget.insert(tk.END, definition_text, "definition_tag")
            definition_widget.config(state="disabled")
        else:
            definition_widget.insert(tk.END, "Definition not found. App only supports VII verbs.", "not_found_tag")
            definition_widget.config(state="disabled")

    except Exception as e:
        text_widget.config(state="normal")
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, f"Error: {str(e)}", "error_tag")
        definition_widget.delete("1.0", tk.END)
        definition_widget.insert(tk.END, "An error occurred.", "not_found_tag")
        text_widget.config(state="disabled")

# --- 2. Main Window ---

root = tk.Tk()
root.title("Southwestern Ojibwe Verb Conjugation App")
root.geometry("750x350")

# Frame for input fields
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10)

custom_font = ("Helvetica", 11)

# User input for verb
ttk.Label(input_frame, text="Verb:", font=custom_font).grid(row=0, column=0, sticky="w", padx=5, pady=2)
verb_entry = ttk.Entry(input_frame, width=40, font=custom_font, justify="center")
verb_entry.grid(row=0, column=1, padx=5, pady=2)

# Text widget for definition
definition_widget = tk.Text(root, height=3, width=80)
definition_widget.pack(pady=(0, 10))
definition_widget.tag_configure("definition_tag", foreground="black", font=("Helvetica", 24), justify="center")
definition_widget.tag_configure("not_found_tag", foreground="gray", font=("Helvetica", 24), justify="center")

# User input for clause
clause_var = tk.StringVar(value="Independent")
ttk.Label(input_frame, text="Clause:", font=custom_font).grid(row=1, column=0, sticky="w", padx=5, pady=2)
clause_menu = ttk.OptionMenu(input_frame, clause_var, "Independent", "Independent", "Dependent")
clause_menu.grid(row=1, column=1, sticky="w", padx=5, pady=2)

# User input for negation
negation_var = tk.StringVar(value="Affirmative")
ttk.Label(input_frame, text="Negation:", font=custom_font).grid(row=2, column=0, sticky="w", padx=5, pady=2)
negation_menu = ttk.OptionMenu(input_frame, negation_var, "Affirmative", "Affirmative", "Negative")
negation_menu.grid(row=2, column=1, sticky="w", padx=5, pady=2)

# User input for pronoun
pronoun_var = tk.StringVar(value="Third Person Singular Inanimate")
ttk.Label(input_frame, text="Pronoun:", font=custom_font).grid(row=3, column=0, sticky="w", padx=5, pady=2)
pronoun_options = [
    "Third Person Singular Inanimate",
    "Third Person Singular Inanimate Obviate",
    "Third Person Plural Inanimate",
    "Third Person Plural Inanimate Obviate"
]
pronoun_menu = ttk.OptionMenu(input_frame, pronoun_var, pronoun_var.get(), *pronoun_options)
pronoun_menu.grid(row=3, column=1, sticky="w", padx=5, pady=2)

# User input for tense
tense_var = tk.StringVar(value="Present")
ttk.Label(input_frame, text="Tense:", font=custom_font).grid(row=4, column=0, sticky="w", padx=5, pady=2)
tense_options = [
    "Conditional",
    "Future Definitive",
    "Future Desiderative",
    "Past",
    "Present"
]
tense_menu = ttk.OptionMenu(input_frame, tense_var, tense_var.get(), *tense_options)
tense_menu.grid(row=4, column=1, sticky="w", padx=5, pady=2)

# Text widget for conjugated verb
text_widget = tk.Text(root, height=3, width=80)
text_widget.pack(pady=10)

# Tags for color, font style in conjugated verb
text_widget.tag_configure("root_tag", foreground="black", font=("Helvetica", 24, "normal"), justify="center")
text_widget.tag_configure("tense_tag", foreground="blue", font=("Helvetica", 24, "normal"), justify="center")
text_widget.tag_configure("error_tag", foreground="gray", font=("Helvetica", 24, "normal"), justify="center")

# Button to conjugate and show
btn = ttk.Button(root, text="Conjugate and Show", command=show_colored_verb)
btn.pack()

# Run GUI
root.mainloop()