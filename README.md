# Ojibwe Verb Conjugator
This project is an Ojibwe verb conjugator app for the **Southwestern Ojibwe dialect**.

It is designed to take a user-submitted verb, compare it to vocabulary gathered from the Ojibwe People's Dictionary, and return a properly conjugated verb — according to clause, pronoun, negation, and tense inputs.

# Description
This app aims to extend the Ojibwe People's Dictionary by algorithmically generating conjugated verb forms, which are too numerous to be hard-coded. **The current version supports Verb Intransitive Inanimate (VII) only**. For an introduction to Ojibwe verb types, see: [Ojibwe Verb Types (YouTube)](https://www.youtube.com/watch?v=gWHISlFpZtU&t=20s).

The app uses variables such as clause, pronoun, negation, and tense to generate accurate conjugated forms. By doing so, it helps address the morphological richness of Ojibwe, creating a scalable solution for expanding the language’s digital lexicon.

This foundational work also supports downstream tools such as:
- Tokenizers
- Grammar checkers
- Translators
- Language learning apps

Ultimately, this enhances both the accessibility and preservation of the Southwestern Ojibwe dialect.

# Table of Contents
- [1. Installation](#installation)
- [2. Usage](#usage)
- [3. Features](#features)
- [4. Contributing](#contributing)
- [5. License](#license)
- [6. Contact](#contact)
- [7. Acknowledgements](#acknowledgements)
- [8. Change Log](#change-log)
- [9. Road Map](#road-map)

# 1. Installation

### Download the repository
Clone this repository to your local machine using Git: `git clone https://github.com/tlong1106/ojibwe_verb_conjugation_tool.git`

### Verify the file structure
Ensure the repository folder (`ojibwe_verb_conjugation_tool`) contains the following main directories:
- `affix_package`
- `gui_package`
- `test_package`

### Run the application
Navigate to the repository folder in your terminal or command prompt, then run the GUI module with: `python -m gui_package.vii_ui_module`

# 2. Usage
(A screenshot and explanation will be added in a future update.)

## 3. Features

- **Modular design**: The codebase is organized into three primary packages:
  - `affix_package`: Handles the generation of verb affixes.
  - `gui_package`: Manages the user interface.
  - `test_package`: Contains unit tests to ensure correctness.

- **Pure Python implementation**: Built using only the Python standard library — no third-party dependencies required.

- **Lightweight and portable**: Easy to set up and run across different environments without additional installation steps.

- **Extensible architecture**: Designed to support additional verb types and features in future releases.

# 4. Contributing
Thank you for considering contributing to this project! Your help is always welcome.

### How to contribute

- **Report bugs or suggest features**. See [Contact](#contact) section
- **Submit code changes** via pull requests to help improve functionality or fix issues 
- **Improve documentation** to help others use the project

### Getting started

1. Fork the repository
2. Clone your fork locally
3. Install dependencies and set up your environment (see [Installation](#installation) section)
4. Create a new branch for your feature or bug fix
5. Commit your changes with clear messages
6. Push your branch and open a pull request

### Code style

Follow the existing coding style and include tests for any new logic.

### Reporting issues

When reporting issues, please include:
- Steps to reproduce the issue
- Your environment (operating system, Python version, etc.)
- Any error messages
- Screenshots (if applicable)

# 5. License
This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

This means you are free to use, modify, and distribute the software, provided that:
- Any modified version you distribute (or use to provide a service) must also be open-sourced under the same license.

# 6. Contact
- This code base is developed and maintained by Tyler Long
- Email: tyler.derek.long@gmail.com
- [LinkedIn](https://www.linkedin.com/in/tyler-long-tech/)

# 7. Acknowledgements
I gratefully acknowledge the following non-profit organizations whose resources were essential to the development of this app:

- [The Ojibwe People's Dictionary](https://ojibwe.lib.umn.edu/): Provided extensive vocabulary and definitions foundational to this project.
- [Cultural Language Arts Network](https://www.maicnet.org/clan/): A part of the Minneapolis American Indian Center, whose grammar classes informed the conjugation logic used in the app.
- [IndigeNash](https://www.indigenash.org/): A multimedia arts and cultural festival that offered a platform to debut this app to the public.

If you appreciate this work, please consider supporting these organizations through donations to help sustain their invaluable efforts.

# 8. Change Log
This section will be updated with version history and key changes in future releases.

# 9. Road Map
Planned features include:
- Support for additional verb types:
    * Verb Animate Intransitive (VAI)
    * Verb Transitive Inanimate (VTI)
    * Verb Transitive Animate (VTA)
    * For more information, please refer to: [Ojibwe Verb Types](https://www.youtube.com/watch?v=gWHISlFpZtU&t=20s)
- Practice mode:
    * Feature to randomize verb and variables
    * The user inputs a response, which is compared to the algorithm output
    * Correct and incorrect responses are categorized according to [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) principles