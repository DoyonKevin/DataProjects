#Kevin Doyon
#Week 1 python assignment

import yaml

#Saves csv data to yaml
def runyaml(data):
    with open("employ.yaml","wt") as file:
        yaml_data = yaml.dump(data,sort_keys=False)
        file.write(yaml_data)

if __name__ == "__main__":
    print("This is yamltool")