#Program to calculate grade.
#created by manav patni.

#input function for the user to input the marks and calculate the grade.
marks = float(input("Enter your marks here- "))

#logic for the program to give grade according to the input given by the user 
if marks > 95:
    print("Congratulations your grade is A+")
elif marks >= 90 or marks == 95:
     print("Congratulations your grade is A")
elif marks >= 75 or marks == 89:
     print("Congratulations your grade is B")
elif marks >= 60 or marks == 74:
     print("Your grade is C")
elif marks >= 50 or marks == 59:
     print("Your grade is D")
elif marks >= 33 or marks == 49:
     print("Your grade is E")
else:
    print("Oops...your Are Fail in the examination", "\n", "Better luck next time")
    
