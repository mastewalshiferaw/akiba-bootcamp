def validate_score(score):
    if score >= 0 and score <=100:
        return True
    else:
        return False

def calculate_grade(score):
    if score >=90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
            return "C"
    elif score >=60:
            return "D"
    
    else:
         return "F"

def calculate_average(students):
     
    for student in students:
        total=0
        count=0
        total+=student["score"]
        count+=1

    if count == 0:
        return 0
    
    average=total/count

    return average


def calculate_highest_lowest(students):
     highest = students[0]["score"]
     lowest = students[0]["score"]
     
     for student in students:

        if student["score"]>highest:
             highest=student["score"]

        if student["score"]<lowest:
             lowest=student["score"]

     return  highest, lowest

def passed_failed(students):
     passed=0
     failed=0
     for student in students:
        if student["score"]>60:
            passed+=1
        else:
             failed+=1

     return passed, failed


def generate_report(students):
    if len(students) == 0:
        print("No students available.")
        return

    
    for student in students:
        if not validate_score(student["score"]):
            print("Invalid score for", student["name"])
            return

  
    average = calculate_average(students)
    highest, lowest = calculate_highest_lowest(students)
    passed, failed = passed_failed(students)

   
    print("===== CLASS REPORT =====")

    for student in students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        print(name, "- Score:", score, "- Grade:", grade)

    print("------------------------")
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Passed:", passed)
    print("Failed:", failed)


        
               
   