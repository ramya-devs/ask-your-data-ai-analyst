
# AskYourData - AI Analyst

An AI-powered data analysis application that allows users to ask questions about sales data using natural language.

## Project Overview

AskYourData converts a natural-language question into a SQL query using Google Gemini, executes the query against a local SQLite database, and displays the result through a Streamlit interface.

## Workflow

User Question
↓
Google Gemini
↓
Generated SQL
↓
SQLite Database
↓
Query Result
↓
Streamlit Interface

## Example

Question:

"What is the total revenue?"

Generated SQL:

```sql
SELECT SUM(quantity * price) AS total_revenue
FROM sales;
````

Result:

2,750,577

## Features

* Natural-language data queries
* AI-generated SQL
* SQLite database
* Streamlit interface
* Query result display
* Simple data visualization

## Technologies

* Python
* SQL
* SQLite
* Google Gemini API
* Streamlit
* Pandas

## Dataset

The project uses a synthetic retail sales dataset.

The dataset contains fields such as:

* Order ID
* Date
* Category
* Area
* Quantity
* Price
* Payment Mode
* Profit

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Create the SQLite database:

```bash
python setup_db.py
```

Set the Gemini API key as an environment variable.

Windows Command Prompt:

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

## Example Questions

* What is the total revenue?
* What is the revenue by category?
* Which area has the highest profit?
* What is the average order value by payment mode?
* Show revenue by month.

## Security

API keys should never be hardcoded into the source code or committed to GitHub.

The local SQLite database and environment files are excluded through `.gitignore`.

## Learning Outcomes

This project provided practical experience with:

* Natural-language-to-SQL
* SQL query generation
* SQLite
* API integration
* Streamlit application development
* Data analysis
* AI-assisted data querying

## Author

**Ramya S**

B.Tech Artificial Intelligence and Data Sciennce

Then we can push it to GitHub.
