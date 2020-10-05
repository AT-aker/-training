import csv
import os.path

if os.path.isfile('student.csv') == False:
	with open('student.csv', 'w', newline='') as f:
		header_list = ['Name', 'Sename', 'Age']
		csv_writer = csv.writer(f)
		csv_writer.writerow(header_list)
		name = input('Name: ')
		sename = input('Sename: ')
		age = input('Age: ')
		csv_writer.writerow([name, 
							sename, 
							age])
		
else:	
	with open('student.csv', 'a', newline='') as file:
		csv_writer = csv.writer(file)
		name = input('Name: ')
		sename = input('Sename: ')
		age = input('Age: ')
		csv_writer.writerow([name, 
							sename, 
							age])
			