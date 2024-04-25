#Task 1: 


def calculate_average_grade(grades):
    if not grades:
        return 0
    total = sum(grades)
    return total / len(grades)




#Task 2:


def find_highest_and_lowest(grades):
    if not grades:
        return None, None
    highest = max(grades)
    lowest = min(grades)
    return highest, lowest


#Task 3: 


def categorize_grades(grades):
    if not grades:
        return {}
    letter_grades = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades:
        for letter, cutoff in letter_grades.items():
            if grade >= cutoff:
                grade_counts[letter] += 1
                break
    return grade_counts

grades = [85, 92, 78, 65, 90]
average_grade = calculate_average_grade(grades)
highest_grade, lowest_grade = find_highest_and_lowest(grades)
grade_distribution = categorize_grades(grades)

print("Average Grade:", average_grade)
print("Highest Grade:", highest_grade)
print("Lowest Grade:", lowest_grade)
print("Grade Distribution:", grade_distribution)
