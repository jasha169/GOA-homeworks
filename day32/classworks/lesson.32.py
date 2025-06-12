# ფუნქცია კვადრატის ფართობისა და პერიმეტრის დასათვლელად
def calculate_square(length=10):
    area = length * length
    perimeter = 4 * length
    return area, perimeter

# გამოძახება გადაცემული სიგრძით
square_area1, square_perimeter1 = calculate_square(6)

# გამოძახება არგუმენტის გარეშე (length = 10)
square_area2, square_perimeter2 = calculate_square()

# შედეგების დაბეჭდვა
print("1) გადაცემული სიგრძით:")
print("ფართობი:", square_area1)
print("პერიმეტრი:", square_perimeter1)

print("2) ნაგულისხმევი სიგრძით:")
print("ფართობი:", square_area2)
print("პერიმეტრი:", square_perimeter2)
