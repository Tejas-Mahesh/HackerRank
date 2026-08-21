from collections import namedtuple

n = int(input())

# Read column names
columns = input().split()

# Create a namedtuple using those column names
Student = namedtuple('Student', columns)

total = 0

for _ in range(n):
    data = input().split()
    student = Student(*data)
    total += int(student.MARKS)

print(f"{total / n:.2f}")
#how it works
#> from collections import namedtuple
#>>> Car = namedtuple('Car','Price Mileage Colour Class')
#>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
#>>> print xyz
#Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
#>>> print xyz.Class
#Y
