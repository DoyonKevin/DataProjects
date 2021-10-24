#Kevin Doyon
#Week 1 python assignment

import csv

#Stores csv data
def storecsv(employees:list):
    try:
        with open("employ.csv",'wt') as file:
            writer = csv.DictWriter(file,["first","last","birth","department","salary"])
            writer.writeheader()
            writer.writerows(employees)

    except FileNotFoundError:
        print("The file could not be found")

#Gets csv data
def getcsv():
    with open("employ.csv","rt") as file:
        reader = csv.DictReader(file)
        employee = []
        for row in reader:
            employee.append(row)
    data= employee
    return data


if __name__ == "__main__":
    print("This is entercsv")