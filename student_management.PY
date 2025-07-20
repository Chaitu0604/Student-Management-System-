import mysql.connector
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chaitu@0604",  # Replace with your MySQL password
    database="StudentManagement"
)

cursor = conn.cursor()

# 1. Bar Chart: Students per Department
def students_per_department():
    cursor.execute("SELECT Department, COUNT(*) FROM Students GROUP BY Department")
    data = cursor.fetchall()
    departments = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.figure(figsize=(8, 5))
    plt.bar(departments, counts, color='skyblue')
    plt.title("Number of Students per Department")
    plt.xlabel("Department")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# 2. Pie Chart: Gender Distribution
def gender_distribution():
    cursor.execute("SELECT Gender, COUNT(*) FROM Students GROUP BY Gender")
    data = cursor.fetchall()
    genders = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=genders, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightblue'])
    plt.title("Gender Distribution")
    plt.axis('equal')
    plt.show()

# 3. Line Plot: Students per Birth Year
def students_by_birth_year():
    cursor.execute("SELECT DOB FROM Students")
    dobs = cursor.fetchall()
    years = [dob[0].year for dob in dobs]
    year_counts = Counter(years)

    sorted_years = sorted(year_counts.items())
    years = [str(k) for k, v in sorted_years]
    counts = [v for k, v in sorted_years]

    plt.figure(figsize=(8, 5))
    plt.plot(years, counts, marker='o', linestyle='-', color='green')
    plt.title("Students per Birth Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Students")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run all visualizations
if __name__ == "__main__":
    students_per_department()
    gender_distribution()
    students_by_birth_year()

    cursor.close()
    conn.close()

