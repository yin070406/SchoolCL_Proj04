"""

* const name = require("Ng Tsz Yin")
* const { class } = require("./4B.json")
* const { class_number } = require("./12.json")

? module.exports = async () => {
  ? await name.connect(class, {
        classwork: false,
        assignment: true,
        date: 07/09/2022,
        Python: true,
        task1: true,
        task2: true,
        full_mark: undefined
?   });
?};

( I don't know am i correct on node.js, sorry if im wrong :D )
"""

#input

#The input of length & width of a rectangle
length = float(input("\nPlease Enter The Length of the Rectangle: "))
width = float(input("Please Enter The Width of the Rectangle: "))

#While True, Ask the user is the information correct or not
while True:
    sure = input("\nAre you sure about the Length and Width? (yes/no): ")

    if sure == "no":
        length = float(input("Please Enter The Length of the Rectangle Again: "))
        width = float(input("Please Enter The Width of the Rectangle Again: "))

    if sure == "yes":
        break

#process
area = length * width

#output
print(f"\nLength: {length}")
print(f"Width: {width}")
print(f"\nThe Area of the Rectangle is: {area}")
