import re
import random
import string
import timeit

# Define the allowed characters for validation
ALLOWED_CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._!*(-)")


# Define the validation functions
def validate_with_regex(s):
    # Regular expression pattern to match allowed characters and length constraint
    pattern = r'^[a-zA-Z0-9._!*\-()]{6,255}$'
    return bool(re.match(pattern, s))

def validate_with_set(s):
    # Check length and allowed characters
    return 6 <= len(s) <= 255 and all(char in ALLOWED_CHARS for char in s)

# Generate a random string of a given length
def generate_random_string(length):
    return ''.join(random.choices(ALLOWED_CHARS, k=length))

# Performance test function
def performance_test_set():
    for _ in range(5000):
        length = random.randint(10, 250)
        test_string = generate_random_string(length)
        validate_with_set(test_string)

# Performance test function
def performance_test_regex():
    for _ in range(5000):
        length = random.randint(10, 250)
        test_string = generate_random_string(length)
        validate_with_regex(test_string)

# Measure performance
regex_time = timeit.timeit(performance_test_set, number=10)
print(f"Total time for 5000 tests with SET: {regex_time:.6f} seconds")

# Measure performance
regex_time = timeit.timeit(performance_test_regex, number=10)
print(f"Total time for 5000 tests with REGEX: {regex_time:.6f} seconds")
