s_name = input("Name: ")
python_score = int(input("Python Score: "))
english_score = int(input("English Score: "))
maths_score=float(input("Mathematics Score: "))

avg = (python_score + english_score + maths_score)/3

print("="*50)
print(f"{'STUDENT RESULT':^50}")
print("="*50)
print(" "*50)
print(f"Student: {s_name}")
print(f"Python: {python_score}")
print(f"English: {english_score}")
print(f"Mathematics: {maths_score}")

print("-"*50)
print(f"Average: {avg}")
print("="*50)