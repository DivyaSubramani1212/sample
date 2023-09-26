student_scores={
    "John": 85,
    "Alice": 92,
    "Michael": 78,
    "Emma": 95,
    "Daniel": 88
}
total_scores=0
num_students=len(student_scores)
for score in student_scores.values():
    total_scores += score
    average_score = total_scores/num_students
    print("Average score:", average_score)


