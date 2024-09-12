# This is the input of Chinese, English and Maths marks
# Users may enter the value after they run the program
# /
# This is the input
Chinese = float(input("Enter the Chinese Marks: "))
English = float(input("Enter the English Marks: "))
Maths = float(input("Enter the Maths Marks: "))

# Printing the text where inside (“”)
print("Calculating the avergae mark...")

# This is the formula of calculating the mean
# Average is the variable and it is the process.
average = (Chinese + English + Maths)/3

# This is the output.
# It will show the value of average marks with two decimal places number.
print("Your Average Marks is %.2f " %average)