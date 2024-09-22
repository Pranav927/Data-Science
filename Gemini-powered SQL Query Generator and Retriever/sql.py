import sqlite3

#Connect to database
connection = sqlite3.connect("student.db")

#Create a cursor to insert record, retrieve and create table
cursor = connection.cursor()

#Create Table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#Inseert Some more records

cursor.execute("Insert Into STUDENT values('Krish', 'Data Science', 'A', 90)")
cursor.execute("Insert Into STUDENT values('Sudhanshu', 'Data Science', 'A', 100)")
cursor.execute("Insert Into STUDENT values('Darius', 'Data Science', 'A', 86)")
cursor.execute("Insert Into STUDENT values('Vikash', 'DevOps', 'B', 50)")
cursor.execute("Insert Into STUDENT values('Dipesh', 'DevOps', 'C', 15)")
cursor.execute("Insert Into STUDENT values('Sara', 'Machine Learning', 'A', 95)")
cursor.execute("Insert Into STUDENT values('Anjali', 'Cloud Computing', 'B', 75)")
cursor.execute("Insert Into STUDENT values('Rahul', 'DevOps', 'C', 40)")
cursor.execute("Insert Into STUDENT values('Ritika', 'Data Science', 'A', 85)")
cursor.execute("Insert Into STUDENT values('Aniket', 'AI', 'B', 65)")
cursor.execute("Insert Into STUDENT values('John', 'Data Science', 'B', 70)")
cursor.execute("Insert Into STUDENT values('Peter', 'Cybersecurity', 'A', 88)")
cursor.execute("Insert Into STUDENT values('Mike', 'DevOps', 'C', 55)")
cursor.execute("Insert Into STUDENT values('Isha', 'AI', 'A', 92)")
cursor.execute("Insert Into STUDENT values('Karan', 'Cloud Computing', 'B', 67)")
cursor.execute("Insert Into STUDENT values('Meera', 'Data Science', 'A', 93)")
cursor.execute("Insert Into STUDENT values('Rohit', 'Machine Learning', 'B', 77)")
cursor.execute("Insert Into STUDENT values('Suresh', 'Cybersecurity', 'C', 53)")
cursor.execute("Insert Into STUDENT values('Vani', 'AI', 'A', 99)")
cursor.execute("Insert Into STUDENT values('Geeta', 'Data Science', 'B', 82)")
cursor.execute("Insert Into STUDENT values('Arjun', 'Machine Learning', 'A', 96)")
cursor.execute("Insert Into STUDENT values('Nisha', 'Cloud Computing', 'B', 71)")
cursor.execute("Insert Into STUDENT values('Pranav', 'Cybersecurity', 'C', 45)")
cursor.execute("Insert Into STUDENT values('Sonia', 'AI', 'A', 89)")
cursor.execute("Insert Into STUDENT values('Divya', 'DevOps', 'C', 42)")
cursor.execute("Insert Into STUDENT values('Vishal', 'Data Science', 'B', 68)")
cursor.execute("Insert Into STUDENT values('Akash', 'Machine Learning', 'A', 91)")
cursor.execute("Insert Into STUDENT values('Ravi', 'Cloud Computing', 'B', 74)")
cursor.execute("Insert Into STUDENT values('Sneha', 'Cybersecurity', 'A', 85)")
cursor.execute("Insert Into STUDENT values('Amit', 'AI', 'C', 58)")
cursor.execute("Insert Into STUDENT values('Neha', 'Data Science', 'A', 87)")
cursor.execute("Insert Into STUDENT values('Manish', 'Machine Learning', 'B', 72)")
cursor.execute("Insert Into STUDENT values('Pooja', 'DevOps', 'C', 47)")
cursor.execute("Insert Into STUDENT values('Gaurav', 'Cybersecurity', 'B', 78)")
cursor.execute("Insert Into STUDENT values('Rina', 'AI', 'A', 94)")
cursor.execute("Insert Into STUDENT values('Sahil', 'Cloud Computing', 'C', 50)")
cursor.execute("Insert Into STUDENT values('Kavya', 'Data Science', 'A', 98)")
cursor.execute("Insert Into STUDENT values('Rajesh', 'DevOps', 'B', 62)")
cursor.execute("Insert Into STUDENT values('Suman', 'Machine Learning', 'A', 90)")
cursor.execute("Insert Into STUDENT values('Monica', 'Cybersecurity', 'C', 49)")
cursor.execute("Insert Into STUDENT values('Yash', 'Cloud Computing', 'B', 64)")
cursor.execute("Insert Into STUDENT values('Priya', 'AI', 'A', 88)")
cursor.execute("Insert Into STUDENT values('Naveen', 'DevOps', 'B', 69)")
cursor.execute("Insert Into STUDENT values('Tarun', 'Data Science', 'A', 80)")
cursor.execute("Insert Into STUDENT values('Harsh', 'Machine Learning', 'C', 54)")
cursor.execute("Insert Into STUDENT values('Leena', 'Cybersecurity', 'B', 81)")
cursor.execute("Insert Into STUDENT values('Rakesh', 'AI', 'A', 97)")
cursor.execute("Insert Into STUDENT values('Shreya', 'DevOps', 'C', 39)")
cursor.execute("Insert Into STUDENT values('Anup', 'Cloud Computing', 'B', 73)")

#Display all the records
print("The inserted recoeds are:")
data = cursor.execute('''Select * From Student''')

for row in data:
    print(row)

#close the connection
connection.commit()
connection.close()