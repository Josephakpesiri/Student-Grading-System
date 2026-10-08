print("======= STUDENT GRADING SYSTEM =======")

#collect user's details (examination score)
print()

print("======= Welcome! =======")
print()

score = int(input("Please enter your score: "))

print()

if score >= 70:
    print(f"Your score is {score}. \nYour grade is A.")

elif score >= 60:
    print(f"Your score is {score}. \nYour grade is B.")

elif score >= 50:
    print(f"Your score is {score}. \nYour grade is C.")

elif score >= 45:
    print(f"Your score is {score}. \nYour grade is D.")

else:
    print(f"Your score is {score}. \nYour grade is F.")
