"""
Module 05: File I/O & Context Managers
Learn: open(), read/write, context managers (with), pathlib

In the advanced courses, you'll see:
    content = safe_path(path).read_text()
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(content)
"""

"""
AI applications constantly read and write files: loading documents for RAG, saving generated code, reading configs. The with statement guarantees the file gets closed even if an error happens inside the block. Without it, a crash could leave the file locked. This pattern (called a context manager) is used for files, database connections, and any resource that needs cleanup.

The with statement ensures proper cleanup via the context manager protocol. Context managers handle resource cleanup. The with statement calls __enter__ on start and __exit__ on end, guaranteeing cleanup.
"""

# Writing a file with the "with" statement (context manager)
with open("my_file.txt", "w") as f:
    f.write("Line 1: Hello from Python!\n")
    f.write("Line 2: This is a test file.\n")
print("✅ File written")

# Reading a file
with open("my_file.txt", "r") as f:
    content = f.read()
print(content)

# Reading line by line
with open("my_file.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"  Line {i}: {line.strip()}")
        
"""
The with statement automatically closes the file when the block ends. "w" mode writes (overwrites), "r" mode reads. .read() gets the whole file, .readlines() gets a list of lines.
"""

"""
pathlib is the modern way to handle file paths in Python. Instead of string concatenation like "data/" + "file.txt", it provides an object-oriented API where paths are objects with helpful methods. Most AI agent code uses pathlib over raw strings.
"""

# pathlib: the modern way (used in AI agent code)
from pathlib import Path

# Create a path object
workdir = Path(".")
print(f"Working dir: {workdir.resolve()}")

# Write using pathlib
output_path = Path("sample_output.txt")
output_path.write_text("Written with pathlib! 🎉\n")
print(f"Wrote to: {output_path}")

# Read using pathlib
text = output_path.read_text()
print(f"Read back: {text}")

# Useful path operations
some_path = Path("data/reports/summary.csv")
print(f"Name: {some_path.name}")          # summary.csv
print(f"Parent: {some_path.parent}")      # data/reports
print(f"Suffix: {some_path.suffix}")      # .csv

# Create directories with parents (creates all intermediate dirs)
# Path("output/charts").mkdir(parents=True, exist_ok=True)

"""
pathlib provides an object-oriented API for file paths. .read_text() and .write_text() are one-liners. .name, .parent, and .suffix extract path components.
"""

# --- Cleanup ---
import os
for f in ["sample_output.txt", "my_file.txt"]:
    if os.path.exists(f):
        os.remove(f)
print("🧹 Cleaned up temp files")

# 🎯 Exercise: Write a function that reads a file and returns its line count
