import select
import sys
import termios
import tty


def read_with_timeout(timeout: float) -> str | None:
    """Read one character from stdin without buffering, or timeout"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)

    rread, _, _ = select.select([sys.stdin], [], [], timeout)

    rc = None

    if rread:
        rc = rread[0].read(1)

    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return rc