Batch PDF Security & Encryption Suite
A pair of high-performance Python utilities designed to automate the encryption and decryption of PDF documents at scale. These tools ensure data privacy by applying industry-standard security protocols to entire directories simultaneously.

💼 Business Case: Data Privacy & Compliance
In sectors like Finance, Healthcare, and Law, protecting "PII" (Personally Identifiable Information) is a legal requirement (e.g., GDPR, HIPAA).

Example Scenario: Financial Services Firm A firm needs to send out 1,000 individual tax statements via email. Sending these as "open" PDFs is a massive security breach.

The Manual Problem: A human employee would spend days manually setting passwords on 1,000 files, leading to burnout and inevitable human error.

The Python Solution: This script automates the process in seconds. It ensures that every document leaving the server is encrypted with a specific protocol, creating a standardized, "audit-ready" workflow that guarantees 100% compliance with data protection policies.

🛠 Features
🔒 Batch Encryption Tool
Folder-Level Processing: Scans an entire source directory for PDF files.

Automated Output Management: Saves secure versions to a dedicated output folder to maintain original file integrity.

Cleanup Logic: Includes an optional feature to securely delete unencrypted source files after successful processing.

🔓 Batch Decryption Tool
Recursive Scanning: Deep-scans folders and subfolders to locate locked documents.

Error Handling: Identifies files with incorrect passwords and prompts the user for action, preventing script crashes.

Streamlined Renaming: Automatically organizes and renames decrypted files for immediate professional use.

💻 Tech Stack
Language: Python 3.x

Libraries: PyPDF (standard for PDF manipulation).

OS Module: For complex file pathing and directory traversal.