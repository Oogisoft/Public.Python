ShowMap: CLI-to-Browser Workflow Accelerator
ShowMap is a lightweight Command Line Interface (CLI) utility that bridges the gap between terminal-based workflows and web-based geographic services. It allows users to trigger precise Google Maps searches instantly without manual browser navigation.

💼 Business Case: Reducing "UI Friction"
In roles like Logistics Coordination, Real Estate Analysis, or Field Service Dispatching, workers often handle addresses inside databases, spreadsheets, or terminal-based CRM systems.

Example Scenario: Logistics Dispatcher A dispatcher is reviewing a list of 50 delivery addresses in a terminal or text file.

The Manual Problem: For every address, the user must: Open a browser → Navigate to Google Maps → Click the search bar → Paste the address → Hit Enter. This creates UI Friction, where the constant switching between keyboard and mouse slows down the core task.

The ShowMap Solution: The user simply highlights the address and types showmap [address] directly in their terminal.

The Result: By eliminating 4-5 manual steps per search, a power user saves several minutes of "micro-tasking" time every hour, keeping their focus on the data rather than the browser UI.

🛠 Features
Instant Browser Injection: Uses Python’s webbrowser controller to launch the default system browser and pass search parameters directly to the Google Maps URL engine.

CLI Integration: Designed to be added to the system PATH, allowing for global execution from any directory.

Smart String Handling: Automatically formats and encodes multi-word addresses (e.g., "123 Main St, New York") into URL-safe strings.

💻 Tech Stack
Language: Python 3.x

Core Module: webbrowser (Standard Library)

CLI Logic: sys.argv for handling command-line arguments.