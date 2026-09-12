"""
Module 03: Control Flow
Learn: if/else, for loops, while loops, comprehensions

In the advanced courses, you'll see:
    if response.stop_reason != "tool_use":
        return messages
    results.sort(key=lambda x: x[1], reverse=True)
    sql_statements = [s.strip() for s in sql.split(';') if s.strip()]
"""

# --- if / elif / else ---
review_score = 4

if review_score >= 4:
    print("Great review! ⭐")
elif review_score >= 2:
    print("Average review")
else:
    print("Poor review")

# Checking membership with `in`
dangerous_commands = ["rm -rf /", "sudo", "shutdown"]
user_command = "ls -la"

if any(d in user_command for d in dangerous_commands):
    print("Blocked!")
else:
    print(f"Safe to run: {user_command}")

# --- range() — generating sequences of numbers ---
for i in range(3):
    print(f"Attempt {i}")  # 0, 1, 2

# range(start, stop, step)
for i in range(1, 6, 2):
    print(i)  # 1, 3, 5

# --- Ternary expression (inline if/else) ---
# Common for setting defaults: x if condition else y
api_key = ""
status = "configured" if api_key else "missing"
print(f"API key: {status}")

# --- for loops ---
menu = ["Avocado Toast", "Quinoa Bowl", "Mac & Cheese"]

for item in menu:
    print(f"- {item}")

# enumerate gives you index + value
for i, item in enumerate(menu):
    print(f"{i + 1}. {item}")

# --- while loops (the agent loop pattern!) ---
iteration = 0
max_retries = 3

while iteration < max_retries:
    print(f"Attempt {iteration + 1}")
    iteration += 1
    if iteration == 2:
        print("Success! Breaking early.")
        break  # exit the loop immediately
else:
    # This runs only if the loop completed without break
    print("All attempts exhausted")

# continue — skip current iteration
print("\nSkipping even numbers:")
for i in range(5):
    if i % 2 == 0:
        continue  # skip to next iteration
    print(f"  {i}")

# --- List comprehensions (used everywhere in AI code) ---
scores = [3, 5, 1, 4, 2, 5, 3]

# Filter: keep only high scores
high_scores = [s for s in scores if s >= 4]
print(f"High scores: {high_scores}")  # [5, 4, 5]

# Transform: from the text-to-sql agent
sql_query = "SELECT * FROM orders; SELECT * FROM items; "
statements = [s.strip() for s in sql_query.split(";") if s.strip()]
print(f"SQL statements: {statements}")

# Dict comprehension
names = ["alice", "bob"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'alice': 5, 'bob': 3}

# 🎯 Exercise: Given a list of numbers, create a new list with only the even ones
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
