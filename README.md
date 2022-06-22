


# ACME Payment System by Cristhian Ferreira

## Topic 

This is a script built for Acment Payment System as an assignment for Python Developer position in Ioet using python scripting language and its standard library.

## Tools 
+ re (regex) for string validation
+ datetime for manage times 
+ Exception class for build custom classes
+ unittest for make Unit Tests


## Getting Started 

+ First make sure you have python3 installed 
+ Run ``python3 test.py`` to run test cases
+ Populate a file `payment_records.txt` with payment records.
+ run ``python3 main.py`` how magic works


## Overview 

To carry out this assignment, I used a functional programming paradign, it is an approach that uses functions to solve problems. The most important part of FP are the pure functions, I made sure that the functions are pure in the body of the script, that is to say that they take a value, return a value and do not mutate states external to it.

My flow is the following:
+  Extract records from .txt file
+ Validate that the records have the correct format.
+ Extract name and list of ranges of hours worked.
+ Validate the ranges have the valid format
+ Make the calculations of the ranges of hours.
+ Add everything.
+ Return a detail of the hours worked.

I used a TDD approach, where I first wrote the test cases for the functions to pass, then I wrote the test cases to validate when they failed.

The first thing I emphasized was to validate the strings of the records, to do this I used the format XX00:00-00:00 and with a regex I validated that the format is valid in case it was not, raise an Exception.

Another point that I made sure was with the input string which has the format NAME=XX00:00-00:00,XX00:00-00:00,XX00:00-00:00, I also used a regex to validate it and raise an exception when encountering a string that is not valid.

The difficult parts were working with the dates and ranges. For carry out this part of the problem I used datetime, a module from python standard library used for work with dates and times. The calculation was like stealing a candy to a baby. A tricky part was working with 00:00:00 (midnight). In some operations I used brute force when the input was 00:00:00. 

## Assignment

Exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday

TU: Tuesday

WE: Wednesday

TH: Thursday

FR: Friday

SA: Saturday

SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

Once you have finished the exercise, please upload the solution to GitHub and send us the link. Don’t forget to include a README.md file. Your README should include an overview of your solution, an explanation of your architecture, an explanation of your approach and methodology and instructions on how to run the program locally.

We evaluate many aspects, including how well your code is structured, applied pattern designs, testing, and the quality of your solution.

When submitting your exercise, be sure to avoid including compiled files as this could be considered malware. Please include the proper instructions to compile your project in the README file.