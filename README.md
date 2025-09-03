# SSH-Sentinel
This is a simple Python tool that monitors your active SSH sessions in real time.

## Features
- Monitors an SSH alias (configured in `config.py`).
- Plays a sound when the connection is lost.

## Usage
- Put the ssh information in config.py
- Link to the server first and then run this tool locally.
- It will ring once at the begining to test the sound.
- When disconnected, it will keep ringing untill manully stopped.
