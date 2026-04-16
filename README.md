# Higher or Lower Card Game (Python Game)

## Description
A console-based card game where the player competes against the computer using a unique scoring system.

Each card has a value based on its number and suit. The player must decide whether to play their card or skip the round. The goal is to beat the computer’s card and earn points.

This project demonstrates Python fundamentals including functions, conditionals, loops, and file handling.

---

## How the Game Works

- You are given a random card (e.g., A♠)
- Each card has a calculated point value:
  - Numbers: face value (2–10)
  - J = 11, Q = 12, K = 13, A = 14
- Suits multiply the value:
  - ♠ = x4
  - ♥ = x3
  - ♣ = x2
  - ♦ = x1

### Example:
A♠ → 14 × 4 = **56 points**

---

## Gameplay

- Choose whether to:
  - **Play the card** → compete against the computer
  - **Skip** → no points gained/lost
- Outcomes:
  - Win → +1 point
  - Lose → -1 point
  - Draw → 0 points

- You can continue playing or end the game at any time

---

## Technologies Used
- Python
- Random module
- File handling (for leaderboard)
- Console-based interface

---

## Features

- Random card generation
- Custom card scoring system
- Computer opponent
- Score tracking system
- Leaderboard stored in a file (`score.txt`)
- Input validation for user choices

---

## Project Structure

- `intro()` → Displays game rules
- `card_number()` / `card_suit()` → Generates random cards
- `card_points()` → Calculates card value
- `card()` → Combines card + points
- `compare()` → Determines winner
- `main_game()` → Controls game flow
- `leaderboard()` → Stores and retrieves scores
- `user()` → Handles username input

---

## What I Learned
- Structuring programs using functions
- Handling user input and validation
- Working with randomness in Python
- Managing game state (score system)
- Reading and writing to files

---

## Limitations / Improvements
- No GUI (console only)
- Leaderboard file can grow without limit
- No sorting of leaderboard scores
- No difficulty levels or advanced gameplay

---

## How to Run

1. Make sure Python is installed
2. Download or clone the repository
3. Run the Python file
