# 1. student dictionary-ის შექმნა
student = {
    "name": "Nino",
    "age": 20,
    "major": "Computer Science",
    "GPA": 3.8
}

print("საწყისი ლექსიკონი:")
print(student)

# 2. .update() მეთოდის გამოყენება
student.update({"age": 21, "university": "TSU"})  # ასაკის განახლება და ახალი ველის დამატება
print("\nგანახლებული ლექსიკონი (update-ის შემდეგ):")
print(student)

# 3. .pop() მეთოდის გამოყენება
removed_item = student.pop("GPA")  # GPA ველის ამოღება
print("\nლექსიკონი pop-ის შემდეგ (მოხსნილია GPA):")
print(student)
print(f"მოხსნილი მნიშვნელობა: GPA = {removed_item}")

# 4. ელემენტის შეცვლა პირდაპირი მინიჭებით
student["major"] = "Artificial Intelligence"
print("\nლექსიკონი major ველის შეცვლის შემდეგ:")
print(student)
