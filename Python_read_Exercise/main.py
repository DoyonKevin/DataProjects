#Kevin Doyon
#Week 1 python assignment

import jsontool
import yamltool
import csvtool
import programtool


#Main program, runs all other programs
def main():
    """Calls other functions needed for the assignment"""
    employee_list = programtool.genemploy()
    csvtool.storecsv(employee_list)
    csv_data = csvtool.getcsv()
    yamltool.runyaml(csv_data)
    jsontool.runjson(csv_data)
    programtool.sortdata(csv_data)

    
if __name__ == "__main__":
    main()