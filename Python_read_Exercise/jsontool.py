#Kevin Doyon
#Week 1 python assignment
 
import json

#Saves csv data to json
def runjson(data):
    data = json.dumps(data,indent=2)
    with open("employ.json","wt") as file:
        file.write(data)

if __name__ == "__main__":
    print("This is jsontool")