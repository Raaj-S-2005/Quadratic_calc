#importing modules (math)
import math

#Asking for the fist number
number_a = float(input("What is numerb a: "))

#Spacing
print("")
print("")

#Asking for the second number
number_b = float(input("What is numerb b: "))

#Spacing
print("")
print("")

#Asking for the third number
number_c = float(input("What is numerb c: "))

#Spacing
print("")
print("")

#Doing the inside of the square root
answer_before_square_root = number_b ** 2 - (4 * number_a * number_c)

#Suare rooting 
answer_after_square_root = math.sqrt(answer_before_square_root)

#Doing the -b +/- the quare root
final_answer_adding_before_divide = (-(number_b) + answer_after_square_root) 
final_answer_substact_before_divide = (-(number_b) - answer_after_square_root) 

#Calculating the 2 different answers
fianl_answer_add = final_answer_adding_before_divide / (2 * number_a)
final_answer_subtract = final_answer_substact_before_divide / (2 * number_a)

#Adding answer
print(f"The fist answer: {fianl_answer_add:.3f}")

#Spacing
print("")

#Subtracing answer
print(f"The second answer: {final_answer_subtract:.3f}")