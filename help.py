#! /usr/bin/env python

# This is a test script to read a help file.

file_path = 'help.txt'

try:
    with open(file_path, 'r') as file:
        file_content = file.read()
        print("Help File:\n", file_content)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
