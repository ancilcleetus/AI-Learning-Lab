"""
Module 01: Variables and Types
Learn: variables, data types, f-strings, print()

In the advanced courses, you'll see lines like:
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
    DB_PATH = "ecommerce.db"
This module teaches the building blocks behind those lines.
"""

# --- Variables: giving names to values ---
model_name = "gemini-2.0-flash"
temperature = 0.7
max_tokens = 8000
is_streaming = True

print(model_name)       # gemini-2.0-flash
print(type(model_name)) # <class 'str'>
print(type(temperature)) # <class 'float'>
print(type(max_tokens))  # <class 'int'>
print(type(is_streaming)) # <class 'bool'>

# --- Strings and f-strings ---
provider = "Google"
greeting = f"Using {model_name} from {provider}"
print(greeting)  # Using gemini-2.0-flash from Google

# String methods you'll use constantly
query = "  What are the top 5 products?  "
print(query.strip())          # removes whitespace
print(query.strip().lower())  # lowercase
print(query.strip().split())  # splits into list of words

# Multi-line strings (used for prompts and SQL)
system_prompt = """You are a helpful assistant.
Rules:
- Be concise
- Use tools over prose"""
print(system_prompt)

# --- len() — counting things ---
menu_items = "Mushroom Burger with Truffle Aioli"
print(f"Characters: {len(menu_items)}")  # 34

# --- More string methods ---
# .join() — critical for building prompts from chunks
chunks = ["You are a helpful assistant.", "Be concise.", "Use tools over prose."]
system_prompt_joined = "\n".join(chunks)
print(system_prompt_joined)

# .replace() — template substitution pattern
template = "Hello, {name}! Welcome to {course}."
filled = template.replace("{name}", "Param").replace("{course}", "Python for GenAI")
print(filled)

# 🎯 Exercise: Create a variable `your_name` and print "Hello, {your_name}! Welcome to Python."
your_name = "Ancil"
template_sentence = "Hello, {your_name}! Welcome to Python."
filled_sentence = template_sentence.replace("{your_name}", your_name)
print(filled_sentence)
