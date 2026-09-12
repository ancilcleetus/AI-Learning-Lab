"""
Module 02: Data Structures
Learn: lists, dicts, nested structures

In the advanced courses, you'll see patterns like:
    messages = [{"role": "user", "content": "Hello"}]
    results.append({"type": "tool_result", "tool_use_id": tc.id, "content": output})
This module teaches you how those structures work.
"""

# --- Lists: ordered collections ---
menu_items = [
    "Avocado Toast with Chili Flakes",
    "Quinoa Power Bowl",
    "Creamy Cashew Mac & Cheese",
]
print(menu_items[0])          # first item
print(menu_items[-1])         # last item
print(len(menu_items))        # 3

menu_items.append("Spicy Tofu Tacos")  # add to end
print(menu_items)

# Slicing
print(menu_items[1:3])  # items at index 1 and 2

# --- Dictionaries: key-value pairs ---
agent_config = {
    "role": "SQL Expert",
    "system_prompt": "You are a senior SQL developer.",
    "temperature": 0,
}
print(agent_config["role"])            # SQL Expert
print(agent_config.get("model", "gpt-4o-mini"))  # "model" key doesn't exist, so returns the default

# Dict iteration methods — used constantly for config and response handling
for key, value in agent_config.items():
    print(f"  {key}: {value}")

print(f"Keys: {list(agent_config.keys())}")
print(f"Values: {list(agent_config.values())}")

# --- Nested structures (the #1 pattern in AI code) ---
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What are the top products?"},
]
# Accessing nested data
print(messages[1]["content"])  # What are the top products?

# Adding to the conversation
messages.append({"role": "assistant", "content": "Here are the top products..."})
print(f"Conversation has {len(messages)} messages")

# --- Tuples: immutable lists (used for return values) ---
coordinates = (40.7128, -74.0060)
lat, lng = coordinates  # unpacking
print(f"Lat: {lat}, Lng: {lng}")

# --- Sets: unique values ---
categories = {"electronics", "clothing", "electronics", "food"}
print(categories)  # {'electronics', 'clothing', 'food'} — duplicates removed

# --- None and Truthiness ---
# None is Python's "no value" — you'll see it as default returns and missing keys
result = None
print(f"result is None: {result is None}")  # True

# Falsy values: None, 0, "", [], {}, False
# Truthy: everything else
error_message = ""
if not error_message:
    print("No error (empty string is falsy)")

# Use `is None` when you need to distinguish None from other falsy values
count = 0
if count is not None:
    print(f"Count exists: {count}")  # prints even though 0 is falsy
