"""Automation script that opens SteamDB free packages page, waits, clicks, and exits."""

from __future__ import annotations

import sys
import time
import webbrowser

try:
    import pyautogui
except ImportError as exc:  # pragma: no cover - runtime guard for missing dependency
    raise SystemExit(
        "PyAutoGUI is required. Install it with `pip install pyautogui`."
    ) from exc


URL = "https://steamdb.info/freepackages/"
CLICK_COORDS = (658, 650)
EXIT_CLICK_COORDS = (1802, 20)
WAIT_SECONDS = 5
MOVE_DURATION_SECONDS = 0.8


def open_page(url: str) -> None:
    """Open the given URL in the default browser."""
    opened = webbrowser.open(url, new=2)  # new=2 -> open in new tab if possible
    if not opened:
        raise SystemExit(f"Kon de webpagina {url!r} niet openen.")


def main() -> None:
    """Open the target page, wait, click, and exit."""
    # Disable PyAutoGUI's failsafe for this short automated action to avoid aborting.
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.1

    open_page(URL)
    time.sleep(WAIT_SECONDS)

    for x, y in (CLICK_COORDS, EXIT_CLICK_COORDS):
        pyautogui.moveTo(x, y, duration=MOVE_DURATION_SECONDS)
        pyautogui.click(x, y)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pragma: no cover - top level exception handler
        # Print nothing if running under pythonw (no console), but ensure process exits.
        sys.stderr.write(f"Automatiseringsfout: {error}\n")
        raise
