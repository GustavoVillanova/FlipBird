# README

## About the Project
This project is a *Flappy Bird*-style game called **FlipBird**, developed in **Python** using the **Pygame** library. The goal is to control the bird and navigate it through the pipes without colliding. The current version allows manual gameplay. This is the **first phase** of the project, with the next phase focusing on developing an **artificial intelligence** to play the game autonomously.

---

## Repository
The project is hosted on GitHub: [FlipBird](git@github.com:GustavoVillanova/FlipBird.git)

---



### How to Play
- **Starting the Game:** The game starts automatically when executed.
- **Controls:**
- - Press the space bar to make the bird jump.
- - **Objective:** Guide the bird through the pipes without colliding. If a collision occurs, the game restarts automatically.

---

### Next Steps
The project will progress in two phases:

1. **Manual Gameplay (current phase):**

- Players control the bird manually.
- Serves as the base for understanding the game mechanics.

2. **Artificial Intelligence (next phase):**

- AI will be developed using reinforcement learning techniques.
- The AI will autonomously learn to play the game, avoiding collisions and maximizing the score.

---

### Contribution
Contributions are welcome! Feel free to open issues, suggest improvements, or submit pull requests.

---

### Technologies Used
- Python
- Pygame

---

## Code Quality and Static Analysis

### Configuring Pylint
This project uses **Pylint** for static code analysis to ensure code quality and standardization.

### Steps to Configure and Run Pylint

1. **Install Pylint**
   Make sure `pylint` is installed in your virtual environment:
   ```bash
   pip install pylint
2. **Generate and Configure the .pylintrc File.**
   If the `.pylintrc` file is not present in the repository, you can generate it:
   ```bash
    pylint --generate-rcfile > .pylintrc
- The `.pylintrc` file **is already included** in the repository for your convenience. It contains custom rules for the project.

3. **Run Pylint**
To check the code quality:
    ```bash
    pylint --generate-rcfile > .pylintrc
---
## Configuring and Running the Hooks
1. **Install Pre-Commit**
Install the `pre-commit` library in your virtual environment:
    ```bash
    pip install pre-commit
2. **Create the Configuration File**
A `.pre-commit-config.yaml` file **is already included** in this repository. It defines the pylint hook for static analysis. The content of the file is as follows:
    ```bash
    repos:
    - repo: https://github.com/pre-commit/mirrors-pylint
        rev: v2.15.10
        hooks:
        - id: pylint
3. **Install the Hooks**
Run the following command to install the pre-commit hooks in the repository:
    ```bash
    pre-commit install
4. **Running Pre-Commit Hooks**
The hooks will run automatically before every git commit.
---
## Generating Documentation

### Prerequisites
1. **Sphinx**: Ensure Sphinx is installed in your environment:
   ```bash
   pip install sphinx
### Steps to Generate Documentation
1. **Navigate to the Project Directory:**
Make sure you are in the project's root directory.
2. **Generate Documentation Source Files:**
Run the following command to generate the source .rst files from the code:
    ```bash
    sphinx-apidoc -o docs/source .
3. **Build the Documentation:**
Generate the documentation in HTML format using:
    ```bash
    sphinx-build -b html docs/source docs/build
4. **View the Documentation:**
Open the file docs/build/index.html in your browser to view the generated documentation.
