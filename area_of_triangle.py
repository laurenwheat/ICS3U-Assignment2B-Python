#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: April 2021
# This program calculates the area of a triangle
# where the user gets to enter the length and width in mm

import math


def main():
    # main function
    print("We will be calculating the area of a triangle. ")
    # input
    height = int(input("Enter the height (mm): "))
    base = int(input("Enter the base (mm): "))
    # process
    area = (height * base)/2
    # output
    print("Area is {} mm2".format(area))


if __name__ == "__main__":
    main()
