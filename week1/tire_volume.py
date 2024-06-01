"""
CSE 111 Week 1

Author: Randy Jones
"""

from math import pi

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10_000_000_000

print(f"The approximate volume is {volume:.2f} liters")
