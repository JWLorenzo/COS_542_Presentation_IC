## IC 1 ##
## Part 1
# What's the issue with the code below?

import requests

payload = {"username": "admin", "password": "letmein"}

response = requests.post(
    "https://httpbin.org/post",
    data=payload,
    headers={"Content-Type": "application/json"},
)

print(response.json())

## Part 2
# Fix the request so it sends actual JSON.

## Part 3
# Create a custom header.

# Add this to your headers:
# "X-Course": "COS 542"

# Use .text or .json() to print the full response
# and confirm your data and custom header were received.
