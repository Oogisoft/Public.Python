#!/usr/bin/env python3
"""
extract_sent_emails.py
----------------------
Parses a Google Takeout Gmail .mbox file and copies only your sent emails
into a new .mbox file.

Usage:
    python extract_sent_emails.py <input.mbox> [output.mbox]

Google Takeout mbox files are typically named:
    "All mail Including Spam and Trash.mbox"

Requirements:
    Python 3.6+  —  no third-party packages needed (uses stdlib only)
"""

import mailbox
import sys
import os
import argparse
from datetime import datetime

#my stuff
path1 = 'D:\Dev\Python\Public.Python\Parse Mbox'
output1 = 'D:\Dev\Python\Public.Python\Parse Mbox\Output'

def is_sent_email(message):
    """
    Returns True if the email is a sent message.

    Google Takeout tags sent emails with 'Sent' in the X-Gmail-Labels header.
    Falls back to checking common Sent folder indicators.
    """
    # Primary check: Gmail label header
    gmail_labels = message.get("X-Gmail-Labels", "")
    if gmail_labels:
        labels = [label.strip().lower() for label in gmail_labels.split(",")]
        if "sent" in labels:
            return True

    # Fallback: some exports use X-GM-LABELS or Status headers
    gm_labels = message.get("X-GM-LABELS", "")
    if gm_labels and "sent" in gm_labels.lower():
        return True

    return False


def extract_sent_emails(input_path, output_path):
    print(f"\n{'='*55}")
    print(f"  Google Takeout — Sent Email Extractor")
    print(f"{'='*55}")
    print(f"  Input : {input_path}")
    print(f"  Output: {output_path}")
    print(f"{'='*55}\n")

    if not os.path.exists(input_path):
        print(f"[ERROR] Input file not found: {input_path}")
        sys.exit(1)

    input_size_mb = os.path.getsize(input_path) / (1024 * 1024)
    print(f"  File size: {input_size_mb:.1f} MB")
    print(f"  Reading mailbox (this may take a moment for large files)...\n")

    try:
        inbox = mailbox.mbox(input_path, create=False)
    except Exception as e:
        print(f"[ERROR] Could not open mbox file: {e}")
        sys.exit(1)

    outbox = mailbox.mbox(output_path, create=True)
    outbox.lock()

    total = 0
    sent_count = 0
    errors = 0

    try:
        for key, message in inbox.items():
            total += 1

            if total % 500 == 0:
                print(f"  ...processed {total} emails, found {sent_count} sent so far")

            try:
                if is_sent_email(message):
                    outbox.add(message)
                    sent_count += 1
            except Exception as e:
                errors += 1
                if errors <= 5:  # Only show first few errors to avoid spam
                    print(f"  [WARN] Skipping message #{total} due to error: {e}")

    finally:
        outbox.flush()
        outbox.unlock()
        inbox.close()

    output_size_mb = os.path.getsize(output_path) / (1024 * 1024) if os.path.exists(output_path) else 0

    print(f"\n{'='*55}")
    print(f"  Done!")
    print(f"{'='*55}")
    print(f"  Total emails scanned : {total:,}")
    print(f"  Sent emails extracted: {sent_count:,}")
    if errors:
        print(f"  Skipped (errors)     : {errors:,}")
    print(f"  Output file size     : {output_size_mb:.1f} MB")
    print(f"  Saved to             : {output_path}")
    print(f"{'='*55}\n")

    if sent_count == 0:
        print("  [NOTE] No sent emails were found.")
        print("  Make sure your .mbox file is from Google Takeout and includes")
        print("  'All Mail' (not just Inbox). The file should contain emails")
        print("  with an 'X-Gmail-Labels' header containing 'Sent'.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Extract sent emails from a Google Takeout Gmail .mbox file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python extract_sent_emails.py "All mail Including Spam and Trash.mbox"
  python extract_sent_emails.py takeout.mbox my_sent_emails.mbox
        """
    )
    parser.add_argument(
        "input",
        help='Path to your Google Takeout .mbox file'
    )
    parser.add_argument(
        "output",
        nargs="?",
        help='Output .mbox file path (default: sent_emails_YYYYMMDD.mbox)',
        default=None
    )

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output or f"sent_emails_{datetime.now().strftime('%Y%m%d')}.mbox"

    # Avoid overwriting the input file
    if os.path.abspath(input_path) == os.path.abspath(output_path):
        print("[ERROR] Input and output paths are the same. Please choose a different output name.")
        sys.exit(1)

    # Warn if output already exists
    if os.path.exists(output_path):
        answer = input(f"  Output file '{output_path}' already exists. Overwrite? [y/N]: ").strip().lower()
        if answer != "y":
            print("  Aborted.")
            sys.exit(0)
        os.remove(output_path)

    extract_sent_emails(input_path, output_path)


if __name__ == "__main__":
    main()
