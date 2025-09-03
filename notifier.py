import time
import subprocess

# this is just to test the sound at the begining
def play_once(sound_path: str):
    subprocess.call(["afplay", sound_path])

# this keeps the sound ring when disconnected
def play_sound_loop(sound_path: str, interval: float = 1.0):
    print("SSH disconnected (Press Ctrl+C to stop)")
    try:
        while True:
            subprocess.call(["afplay", sound_path])
            time.sleep(interval)
    except KeyboardInterrupt:
        print("done")
