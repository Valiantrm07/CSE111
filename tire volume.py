"""The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = 
π w2 aw a + 2,540 d
10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches."""

"""Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire."""


import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_wheel = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi * width **2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter_wheel) / math.pow(10,10)

print(f"The approximate volume is {volume:.2f} liters")