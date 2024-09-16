#Just a random shit
#input list exercise


score = [0, 0, 0, 0, 0, 0]


print("Hello o/")


score[0] = int(input("Chinese Marks: "))
score[1] = int(input("English Marks: "))
score[2] = int(input("Maths Marks: "))
score[3] = int(input("CS Marks: "))
score[4] = int(input("Elective01 Marks: "))
score[5] = int(input("Elective02 Marks: "))


average = (score[0] + score[1] + score[2] + score[3]/2 + score[4] + score[5]) / 5.5


while True:
    print("Please check whether your marks correct or not")
    for i in range(len(score)):
        print(score[i])
    ans = input("Yes or No? (y/n): ")


    if ans == "y":
        print("\n Alright!")
        break
    if ans == "n":
        score[0] = int(input("Chinese Marks: "))
        score[1] = int(input("English Marks: "))
        score[2] = int(input("Maths Marks: "))
        score[3] = int(input("CS Marks: "))
        score[4] = int(input("Elective01 Marks: "))
        score[5] = int(input("Elective02 Marks: "))


print("Calculating... \n")
for i in range(len(score)):
    print(score[i])
print(f"Your Average: {average}")

