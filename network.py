import subprocess

def resolve_hostname(alias: str) -> str:
    try:
        out = subprocess.check_output(
            ["ssh", "-G", alias],
            text=True,
            stderr=subprocess.DEVNULL
        )
        for line in out.splitlines():
            if line.startswith("hostname "):
                return line.split()[1]
    except subprocess.CalledProcessError:
        pass
    return alias


def has_established_ssh(host_ip: str) -> bool:
    cmd = f'lsof -n -iTCP@{host_ip}:22 -sTCP:ESTABLISHED -a -c ssh'
    return subprocess.call(
        cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ) == 0
