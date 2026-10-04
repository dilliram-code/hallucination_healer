students = {
    101: {
        "name": "Ram",
        "age": 22,
        "course": "BSc Physics",
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "BSc Computer Science",
    },
}

def get_student_info(student_id):
  """Return information about a student"""
  
  student = students.get(student_id)
  
  if student is None:
    return "Student not found"
  
  return (
        f"Name: {student['name']}\n"
        f"Age: {student['age']}\n"
        f"Course: {student['course']}"
    )
  