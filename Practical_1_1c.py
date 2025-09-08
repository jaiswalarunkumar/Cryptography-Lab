def student_average_marks():
      print("--- Question 3: Student Average Marks ---")
    students = {
        'Alice': {'Maths': 85, 'Physics': 90, 'Chemistry': 78},
        'Bob': {'Maths': 92, 'Physics': 88, 'Chemistry': 95},
        'Charlie': {'Maths': 75, 'Physics': 80, 'Chemistry': 82}
    }
    
    subject_to_average = 'Maths'
    total_marks = 0
    student_count = 0
    
    for student, marks in students.items():
        if subject_to_average in marks:
            total_marks += marks[subject_to_average]
            student_count += 1
            
    if student_count > 0:
        average_mark = total_marks / student_count
        print(f"Student data: {students}")
        print(f"The average mark for {subject_to_average} is: {average_mark:.2f}")
    else:
        print(f"No marks found for the subject '{subject_to_average}'.")
    print("\n" + "-"*40 + "\n")