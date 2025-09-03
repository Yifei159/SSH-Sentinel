import time
import signal
from notifier import play_once, play_sound_loop
from network import resolve_hostname, has_established_ssh
from config import HOST_ALIAS, CHECK_INTERVAL, CONFIRM_FAILS, SOUND

def main():
    # ring once at the begining to test the sound
    play_once(SOUND)

    host_ip = resolve_hostname(HOST_ALIAS)
    print(f"Watching the SSH link of {HOST_ALIAS} ({host_ip})，check each {CHECK_INTERVAL}s. Press Ctrl+C to stop")

    fails = 0
    try:
        while True:
            if has_established_ssh(host_ip):
                fails = 0
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Still connecting {host_ip}")
            else:
                fails += 1
                print(f"Disconnected round {fails}")
                if fails >= CONFIRM_FAILS:
                    play_sound_loop(SOUND, 1.0)
                    fails = 0
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("done")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.default_int_handler)
    main()
