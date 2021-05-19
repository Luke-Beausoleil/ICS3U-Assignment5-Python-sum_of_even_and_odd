#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program reads a set of integers
#     and prints the sums of the even and odd integers


def main():
    # this function receives the integers and finds the sums

    # variables
    loop_counter = 0
    even_sum = 0
    odd_sum = 0

    # input
    num_of_int_as_string = input("How many integers do you wish to input? ")

    # process & output
    try:
        num_of_int = int(num_of_int_as_string)
        if num_of_int > 0:
            while loop_counter < num_of_int:
                input_as_string = input("Enter an integer: ")
                integer = int(input_as_string)
                loop_counter += 1
                if integer % 2 == 0:
                    even_sum += integer
                else:
                    odd_sum += integer
            print("\nThe sum of the even integers is {0}".format(even_sum))
            print("The sum of the odd integers is {0}".format(odd_sum))
        elif num_of_int == 0:
            print("\nThe sum of the even integers is 0")
            print("The sum of the odd integers is 0")
        else:
            print("\nInvalid. You cannot enter a negative amount of integers")
    except (Exception):
        print("\nInvalid.")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
