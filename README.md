# 🎯 Guess Game – Color Edition

A simple color-based guessing game made with Python and Pygame. Inspired by the classic Mastermind-style logic game, players must guess a secret 4-color sequence within 10 tries using drag-and-drop mechanics.

---

## 🕹 Gameplay

- A random sequence of **4 colors** is generated at the start.
- The generated color sequence **can contain repeated colors**.
- You have **10 attempts** to guess the exact color sequence.
- After each guess, you'll receive **feedback dots**:
  - ⚫ **Black**: Correct color in the correct position.
  - ⚪ **White**: Correct color in the wrong position.
  - 🔘 **Gray**: Incorrect color.

---

## 🎨 Available Colors
- Yellow
- Red
- Green
- Blue
- Orange
- Purple

---

## 🧠 How to Play

1. Drag and drop 4 colored circles into the sockets.
2. Press **Enter** to lock in your guess.
3. Check the feedback dots to refine your next guess.
4. Win by matching the correct sequence — or run out of tries trying!

---

## 🛠 Requirements

- Python 3.x
- Pygame

Install Pygame:
```bash
pip install pygame
