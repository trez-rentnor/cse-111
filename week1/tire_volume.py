"""
CSE 111 Week 1

Author: Randy Jones

Prompts the user for a tire size and calculates the volume of the tire
To exceed requirements, this program parses the standard tire notation to get the size values
and stores the phone number of users who would like to purchase
"""

from math import pi
from datetime import datetime
import re

SIZE_REGEX = r'(\d+)/(\d+)R(\d+)'

# Prompt the user for the tire size
match = None
while not match:
    size = input("Enter the tire size (ex 205/60R15): ")
    match = re.search(SIZE_REGEX, size)
    if not match:
        print(f"Invalid size {size}. Try again.")

# Get the phone number.  This does not validate phone numbers.
phone = input("Enter phone number if you would like to purchase: ")

# Extract dimensions from the tire size
width = int(match.group(1))
aspect_ratio = int(match.group(2))
diameter = int(match.group(3))

# Calculate volume
volume = (pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10_000_000_000

# Write to file
with open('volumes.txt', 'a') as output_file:
    print(f"{datetime.now():%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone}", file=output_file)

# Print result
print(f"The approximate volume is {volume:.2f} liters")
