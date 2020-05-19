import zadanie as zad

person = zad.Person()
print(person)

student = zad.Student()
student.put_field_of_study("Mechanik")
student.PutStudentGrades()
print(student)


worker = zad.Employee()
worker.set_job_title("Informatyk")
worker.set_skills()
print(worker)
