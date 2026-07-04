# 🧮 2048

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/filipebteixeira98/2048?color=edcc63&style=flat-square">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/filipebteixeira98/2048?color=edcc63&style=flat-square">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/filipebteixeira98/2048?color=edcc63&style=flat-square">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/filipebteixeira98/2048?color=edcc63&style=flat-square">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/filipebteixeira98/2048?color=edcc63&style=flat-square">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/filipebteixeira98/2048?color=edcc63&style=flat-square">
  <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/filipebteixeira98/2048?color=edcc63&style=flat-square">
</p>

<p align="center">
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-layout">Layout</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=edcc63&labelColor=808090">
</p>

<p align="center">
  <img alt="2048" src=".github/mockup.png" width="250px">
</p>

This project is a sleek, Python-based clone of the popular sliding tile puzzle game **2048**, built using the **Pygame** library. The game is played on a 4×4 grid where players use the arrow keys or WASD to slide numbered tiles. When two tiles with the same number touch, they merge into one with double the value. The objective is to combine tiles strategically until you reach the elusive **2048** tile without running out of empty spaces or valid moves.

## 💻 Technologies

- Python 3.11.2
- PyGame
- Git
- Ruff

## 🎮 Features

- **Classic Sliding Mechanics:** Authentic tile-shifting, merging, and spawning logic mimicking the original web game.
- **Smooth Visuals & Animations:** Fluid grid sliding and pop-up merge scaling effects for polished gameplay.
- **Score & High Score Tracking:** Live score counter along with local file persistence to save your all-time high score.
- **Responsive UI:** Minimalistic, modern design utilizing custom fonts, optimized palettes, and clear Game Over/Victory screen overlays.
- **State Management:** Immediate game restart functionality (`R` key) and a responsive pause mechanic (`P` key).

## 🛠️ Prerequisites

Before running the game, ensure you have Python installed (version 3.8 or higher recommended).

## 📦 Installation & Setup

```bash
# Clone the Flappy Bird repository from GitHub to your local machine
git clone https://github.com/filipebteixeira98/2048

# Move into the project's root directory
cd 2048

# Create a virtual environment named '.venv' to isolate project dependencies
python -m venv .venv

# Activate the virtual environment (use '.venv\Scripts\activate' if on Windows)
source .venv/bin/activate

# Install all development and project dependencies listed in the requirements file
pip install -r requirements-dev.txt

# Run the main script to start the Flappy Bird game
python main.py
```

## 🫶 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is under the MIT license.

<p align="center">
  Made with ♥ by me
</p>
