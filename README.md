# Unclosed File Bug in Python

This repository demonstrates a common error in Python programming: forgetting to close a file properly.  This can lead to various problems, including resource leaks and data corruption.

The `bug.py` file shows the problematic code. The `bugSolution.py` demonstrates the correct way to handle file operations using context managers, which guarantees that the file is always closed, even if exceptions occur.

**How to Reproduce:**
1. Run `bug.py`. Observe that if an exception occurs within the function, it will not execute the `f.close()` method which can cause errors.
2. Run `bugSolution.py`. Observe that the exception is handled without causing a resource leak.