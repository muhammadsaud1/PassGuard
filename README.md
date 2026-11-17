# PassGuard

An interactive command-line password strength checker and generator, written in Python.

## Features

- Checks a password against length, character-variety, and common-pattern rules
- Scores strength with clear, color-coded feedback
- Generates random passwords of a chosen length with a balanced mix of character classes
- Simple menu-driven interface

## Requirements

- Python 3.8+
- `colorama`

## Install

```bash
pip install colorama
```

## Usage

```bash
python3 password_strength_checker.py
```

Follow the on-screen menu to check a password or generate a new one.

## Notes

Passwords are processed locally and are never written to disk or sent anywhere.
