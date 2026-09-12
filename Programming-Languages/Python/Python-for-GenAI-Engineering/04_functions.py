"""
Module 04: Functions
Learn: def, parameters, defaults, *args, **kwargs, lambda

In the advanced courses, you'll see:
    def calculate_similarity(v1, v2): ...
    def execute_tool(name: str, args: dict) -> str: ...
    results.sort(key=lambda x: x[1], reverse=True)
"""

# --- Basic function ---
def greet(name):
    return f"Hello, {name}!"

print(greet("Ancil"))

# --- Default parameters ---
def create_message(content, role="user"):
    return {"role": role, "content": content}

print(create_message("What are top products?"))
print(create_message("You are helpful.", role="system"))

# --- Multiple return values ---
def analyze_text(text):
    words = text.split()
    return len(words), len(text)

word_count, char_count = analyze_text("Hello world from Python")
print(f"Words: {word_count}, Characters: {char_count}")

# --- *args and **kwargs ---
def log_event(*args, **kwargs):
    """Accepts any number of positional and keyword arguments."""
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

log_event("query", "SQL", user="Ancil", score=5)
# Args: ('query', 'SQL')
# Kwargs: {'user': 'Ancil', 'score': 5}

# --- Lambda functions (small inline functions) ---
# Used in sorting — very common in AI code
results = [("Quinoa Bowl", 0.88), ("Mac & Cheese", 0.53), ("Tofu Tacos", 0.71)]

results.sort(key=lambda x: x[1], reverse=True)
print("Ranked results:")
for dish, score in results:
    print(f"  [{score:.2f}] {dish}")
    
items = [("a", 5), ("b", 3), ("c", 7)]
new_items = sorted(items, key=lambda x: x[1])
print(new_items)
items.sort(key=lambda x: x[1], reverse=True)
print(items)

# --- Functions calling functions ---
def get_score(item):
    return item[1]

# Same result, different style
results.sort(key=get_score, reverse=True)

# --- Useful built-in functions ---
token_counts = [150, 320, 85, 210, 475]

print(f"Total tokens: {sum(token_counts)}")      # 1240
print(f"Min tokens: {min(token_counts)}")         # 85
print(f"Max tokens: {max(token_counts)}")         # 475

# sorted() returns a new sorted list (doesn't modify the original)
print(f"Sorted: {sorted(token_counts)}")
print(f"Top 3: {sorted(token_counts, reverse=True)[:3]}")
