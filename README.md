# README

## About the Project
This project is a *Flappy Bird*-style game called **FlipBird**, developed in **Python** using the **Pygame** library. The goal is to control the bird and navigate it through the pipes without colliding. The current version allows manual gameplay. This is the **first phase** of the project, with the next phase focusing on developing an **artificial intelligence** to play the game autonomously.

---

## Repository
The project is hosted on GitHub: [FlipBird](git@github.com:GustavoVillanova/FlipBird.git)

---

## How to Use the Application

### Prerequisites
1. **Python 3.8+**: Make sure Python is installed on your system.
2. **Pygame**: Ensure the Pygame library is installed.

### Steps to Run the Game
1. **Clone the repository**:
   ```bash
   git clone git@github.com:GustavoVillanova/FlipBird.git
   cd FlipBird
2. **Install dependencies:** Use the requirements.txt file to install all necessary dependencies:

    ```bash
    pip install -r requirements.txt
3. **Verify media files:** Ensure the imgs folder contains these images:

- pipe.png (image of the pipes)
- base.png (image of the ground)
- bg.png (background image)
- bird1.png, bird2.png, bird3.png (images for the bird animation)

4. **Run the game:**

    ```bash
    python FlappyBird.py
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
