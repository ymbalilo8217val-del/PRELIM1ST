

print("\nACTIVITY #2")

letters = "ABCDE"

for i in range(5):
    print(letters[i])


# =========================
# ACTIVITY #3
# Multiple of 5
# =========================

print("\nACTIVITY #3")

number = int(input("Enter a multiple of 5 between 1 and 100: "))

if number >= 1 and number <= 100 and number % 5 == 0:
    print("The number is valid.")
else:
    print("The number is invalid.")


# =========================
# ACTIVITY #4
# Payment and Change
# =========================

print("\nACTIVITY #4")

item1 = float(input("Enter the cost of the first item: "))
item2 = float(input("Enter the cost of the second item: "))

total = item1 + item2

print(f"Total cost: ${total:.2f}")

payment = float(input("Enter your payment: "))

if payment < total:
    owe = total - payment
    print(f"You still owe ${owe:.2f}.")
else:
    change = payment - total
    print("Thank you for your payment!")
    print(f"Your change is ${change:.2f}.")


# =========================
# ACTIVITY #5
# Last Alphabetically
# =========================

print("\nACTIVITY #5")

def last_word():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    word3 = input("Enter the third word: ")

    last = max(word1, word2, word3)

    print("The word that comes last alphabetically is:", last)

last_word()


# =========================
# ACTIVITY #6
# Grade Program
# =========================

print("\nACTIVITY #6")

score = float(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# =========================
# ACTIVITY #7
# Arithmetic Program
# =========================

print("\nACTIVITY #7")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero."
