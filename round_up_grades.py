#rounding up grades to the next multiple of 5 based on a few params

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        if grade > 37:
            #floor each grade, add 1 and multiply by 5 to get next multiple of 5.
            next_of_five = (grade//5 + 1) * 5
            if next_of_five - grade < 3:    
                rounded_grades.append(next_of_five)
            else:
                rounded_grades.append(grade)
    return rounded_grades