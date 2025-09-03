# SSH-Sentinel
This is a simple Python tool that monitors your active SSH sessions in real time.

---

## Features
- Monitors an SSH alias (configured in `config.py`).
- Plays a sound (`/System/Library/Sounds/Hero.aiff`) when the connection is lost.

---

## Project Structure
SSH-Sentinel/
├─ config.py      # Configuration constants
├─ network.py     # Hostname resolution & SSH connection check
├─ notifier.py    # Sound notifications
└─ watcher.py     # Main program
