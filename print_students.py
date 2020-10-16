import csv


def print_students(*args,**kwargs):
	with open('student.csv', 'r') as file:
		csv_reader = csv.reader(file)
		next(csv_reader)
		for student in csv_reader:
			print(student)


print_students()