#!/usr/bin/env python3
"""Render an HTML file to A4 PDF with local headless Chrome/Chromium.

usage: render_pdf.py input.html output.pdf
"""
import os
import shutil
import subprocess
import sys

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    shutil.which("google-chrome"),
    shutil.which("chromium"),
    shutil.which("chromium-browser"),
]


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: render_pdf.py input.html output.pdf")
    html, pdf = (os.path.abspath(a) for a in sys.argv[1:3])
    chrome = next((c for c in CANDIDATES if c and os.path.exists(c)), None)
    if not chrome:
        sys.exit("No Chrome/Chromium found. Open the HTML in a browser and print to PDF instead.")
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--print-to-pdf=" + pdf,
            "file://" + html,
        ],
        check=True,
        capture_output=True,
    )
    print("wrote " + pdf)


if __name__ == "__main__":
    main()
