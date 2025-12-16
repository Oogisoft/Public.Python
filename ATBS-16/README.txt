Meal & Ingredient Relational Database Manager
A Python-based CRUD (Create, Read, Update, Delete) application that manages complex many-to-many relationships between meals and their components using an SQLite backend.

🚀 Business Case: Why This Matters
In a professional environment, this script represents a Product Lifecycle Management (PLM) or Inventory Control system.

Example Scenario: Commercial Kitchen or Meal-Prep Startup A business needs to manage 500+ recipes. Without this script, they face several risks:

Supply Chain Disruption: If the price of "Cumin" spikes, the business needs to know instantly every single meal that uses it to adjust pricing or find substitutes.

Allergen Tracking: If a customer reports a nut allergy, the business must be able to query the database to filter out every recipe containing that specific ingredient.

Scalability: Manual spreadsheets fail as the menu grows. This SQL-driven approach ensures data integrity, prevents duplicate entries, and allows for rapid searching that scales to thousands of entries.

🛠 Features
Dynamic Data Entry: Add new meals and their specific ingredients into a relational structure.

Reverse Lookup: Search for meals based on a single ingredient (e.g., "What can I make with Chicken?").

Ingredient Extraction: Query a meal to return a complete list of required ingredients.

Data Persistence: Uses SQLite to ensure data remains saved even after the program closes.

💻 Tech Stack
Language: Python 3.x

Database: SQLite3

Logic: Parameterized SQL queries for security (preventing SQL injection).