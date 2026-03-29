import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_sql(user_query, schema):

    prompt = f"""
You are an expert SQL generator.

STRICT RULES:
- Return ONLY SQL query (no explanation)
- NEVER use SELECT * unless user asks for ALL data
- If user asks for names → SELECT name
- If user asks for salary → SELECT salary
- If user asks for department → SELECT department
- Use WHERE for filtering
- Use ORDER BY for sorting
- Use LIMIT for top queries

Examples:

User: show employee names
SQL: SELECT name FROM employees;

User: show salary
SQL: SELECT salary FROM employees;

User: show all employees
SQL: SELECT * FROM employees;

User: top 2 employees
SQL: SELECT * FROM employees ORDER BY salary DESC LIMIT 2;

User: names sorted by salary
SQL: SELECT name FROM employees ORDER BY salary DESC;

Schema:
{schema}

User Query:
{user_query}

ONLY RETURN SQL:
"""

    response = requests.post(OLLAMA_URL, json={
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    })

    print("LLM RAW:", response.text)

    try:
        data = response.json()
        sql = data.get("response", "").strip()

        if not sql:
            return "ERROR"

        # Clean formatting
        if "```" in sql:
            sql = sql.split("```")[1]

        sql = sql.replace("Here is your SQL:", "").strip()

        # 🔥 FORCE FIX (VERY IMPORTANT)
        query_lower = user_query.lower()

        if "name" in query_lower and "SELECT *" in sql.upper():
            sql = "SELECT name FROM employees;"

        if "salary" in query_lower and "SELECT *" in sql.upper():
            sql = "SELECT salary FROM employees;"

        if "department" in query_lower and "SELECT *" in sql.upper():
            sql = "SELECT department FROM employees;"

        return sql

    except Exception as e:
        print("LLM ERROR:", e)
        return "ERROR"





