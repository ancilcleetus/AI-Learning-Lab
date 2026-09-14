"""
Module 06: Error Handling
Learn: try/except/else/finally, common exceptions

In the advanced courses, every API call and SQL execution is wrapped:
    try:
        cursor.execute(statement)
    except Exception as e:
        state["error"] = f"SQL Execution Error: {str(e)}"
"""

"""
Every AI API call can fail: network timeouts, rate limits, invalid responses. In production AI code, every external call is wrapped in try/except. Let us learn to handle errors gracefully.
"""

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Catching multiple exception types
def safe_parse_int(value):
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print(f"Could not parse '{value}': {e}")
        return None

print(safe_parse_int("42"))      # 42
print(safe_parse_int("hello"))   # None

"""
try runs the code. except catches specific errors. The "as e" captures the error message. You can catch multiple types with a tuple.
"""

"""
Catching broad Exception works for API calls where you want to handle any failure gracefully. But for logic errors, catch specific types so bugs are not silently hidden. The rule: be specific when you know the error, be broad when wrapping external calls.
"""

# The generic Exception catch (use sparingly)
def run_query(query):
    """Simulates what the text-to-sql agent does."""
    try:
        if "DROP" in query.upper():
            raise ValueError("Dangerous query blocked!")
        return f"Results for: {query}"
    except Exception as e:
        return f"Error: {e}"

print(run_query("SELECT * FROM orders"))
print(run_query("DROP TABLE orders"))

# try/except/finally
try:
    data = "some important data"
    # Simulate processing
    processed = data.upper()
    print(f"Processed: {processed}")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup always runs (close files, connections, etc.)")

# try/except/else/finally: the full pattern
def fake_api_call(should_fail=False):
    if should_fail:
        raise ConnectionError("Server unreachable")
    return {"status": "ok", "data": [1, 2, 3]}

try:
    result = fake_api_call(should_fail=False)
except ConnectionError as e:
    print(f"API error: {e}")
else:
    # Runs only if no exception occurred
    print(f"Success! Got {len(result['data'])} items")
finally:
    # Always runs, whether exception occurred or not
    print("Cleanup always runs")
    
"""
else runs only on success, so use it for code that should only execute when no error happened. finally always runs, making it perfect for cleanup like closing connections.
"""

"""
You can also create your own exceptions using raise, which is how AI agents enforce safety rules. If user input looks dangerous, raise an error before it reaches the LLM.
"""

# Raising your own exceptions
def safe_path(path):
    """From the Claude Code agent — blocks paths outside workspace."""
    if ".." in path:
        raise ValueError(f"Path escapes workspace: {path}")
    return path

try:
    safe_path("../../etc/passwd")
except ValueError as e:
    print(f"Blocked: {e}")
    
"""
raise lets you trigger a specific exception type you choose with a custom message. ValueError is used for invalid inputs. It is commonly used in AI guardrails to block unsafe operations & block unsafe inputs before they reach the LLM.
"""

"""
🎯 Exercise: Write a Python function called `safe_load_config` that reads a JSON config file and handles these specific errors gracefully:

1. FileNotFoundError: return default config dict
2. json.JSONDecodeError: log the error, return default config
3. KeyError: when accessing nested keys, return None for missing keys

Include type hints, docstring, and demonstrate usage with a try/except block that catches all three scenarios.

Notice how each exception type gets its own handler with appropriate recovery behavior. This pattern is essential for building resilient AI applications that handle API failures, malformed responses, and missing data.
"""
