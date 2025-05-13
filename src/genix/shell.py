import subprocess


def execute_command(command: str) -> None:
    """Execute a shell command safely."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Command failed: {e}")
