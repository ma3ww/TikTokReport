#!/usr/bin/env python3
"""
tiktok Reporting Helper (Safe & Compliant)

- Opens the official tiktok reporting flow for a profile
- Displays contact links (Telegram + GitHub)
- Logs actions locally for record-keeping
#
This tool does NOT automate reporting or interact with tiktok APIs.
It simply helps users navigate to the official report page.

Author: vrskyr.github.io
"""

import webbrowser
import datetime
import os
import sys

# ---- Your links (visible in CLI + used in display) ----
TELEGRAM_URL = "https://t.me/redsecure"
GITHUB_URL = "https://vrskyr.github.io"

# ---- Config ----
LOG_FILE = "report_log.txt"


def banner():
    print("=" * 60)
    print(" tiktok Reporting Helper (Safe Use)")
    print("=" * 60)
    print(f"GitHub : {GITHUB_URL}")
    print(f"Telegram: {TELEGRAM_URL}")
    print("-" * 60)
    print("This helper opens tiktok's official report flow.")
    print("It does NOT automate reporting or submit anything for you.")
    print("-" * 60)


def validate_username(username: str) -> bool:
    if not username:
        return False
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._")
    return all(c in allowed for c in username) and (1 <= len(username) <= 30)


def open_profile(username: str):
    # Opens the public profile page; user can access the in-app/web report option
    url = f"https://www.tiktok.com/@{username}/"
    print(f"[+] Opening profile: {url}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[!] Error opening browser: {e}")


def open_help_center():
    # Official help center for reporting guidance
    help_url = "https://help.tiktok.com/"
    print(f"[+] Opening help center: {help_url}")
    webbrowser.open(help_url)


def log_action(username: str):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts} | opened report flow for: {username}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception as e:
        print(f"[!] Could not write log: {e}")


def main():
    banner()

    if len(sys.argv) > 1:
        username = sys.argv[1].strip()
    else:
        username = input("Enter tiktok username to review/report: ").strip()

    if not validate_username(username):
        print("[!] Invalid username format.")
        sys.exit(1)

    print("\nOptions:")
    print("1) Open profile (report from profile menu)")
    print("2) Open tiktok Help Center")
    choice = input("Select an option (1/2): ").strip()

    if choice == "1":
        open_profile(username)
        log_action(username)
        print("[+] Done. Use tiktok's 'Report' option on the profile page.")
    elif choice == "2":
        try:
            open_help_center()
            print("[+] Help center opened.")
        except Exception as e:
            print(f"[!] Error opening help center: {e}")
    else:
        print("[!] Invalid choice.")
        sys.exit(1)

    print("\nStay compliant with platform rules. Use reporting responsibly.")
    print(f"Contact: {TELEGRAM_URL} | {GITHUB_URL}")


if __name__ == "__main__":
    main()