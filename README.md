# Flappy Bird Clone (Work in Progress)

An incomplete Flappy Bird game built in Python using the `pygame` library. I am hosting it here to collaborate, track my updates, and get help debugging the code.

## 🛠️ Current Issue / Help Needed
The game code is partially complete, but I am currently fixing the core gameplay loop inside `main.py`. Specifically, I need help with:
* Verifying the pipe collision logic.
* Managing how old pipes are removed (`upperPipe.pop(0)`) so the game doesn't crash.

## 🚀 How to Run the Game
If you want to look at the code or test it locally on your machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install requirements:
   Make sure you have Python installed, then install the Pygame library:
   ```bash
   pip install pygame
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Folder Contents
* `main.py` - The main game loop and logic definitions.
* `/sprites` - Image assets for the bird, pipes, background, and UI score digits.
* `/music` - Sound effects for jumping, scoring, and falling.
