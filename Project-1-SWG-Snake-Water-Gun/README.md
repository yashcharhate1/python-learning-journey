# Project 1 — Snake, Water, Gun

A command-line implementation of the Snake-Water-Gun game (a 3-way variant of Rock-Paper-Scissors), played against the computer.

## How it works
- The computer's choice is randomly selected using Python's `random` module.
- Player input and the win/draw/lose logic are handled using dictionary lookups instead of long `if`/`elif` chains, mapping choices to values and back to readable labels.

## Files
- `main.py` — main implementation
- `main_shortened.py` — a condensed alternative version of the same logic

## Run it
```bash
python3 main.py
```

## Concepts applied
Dictionaries, conditionals, the `random` module, and user input — drawing on Chapters 2, 5, and 6.
