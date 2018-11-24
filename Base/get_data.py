import os, yaml

class Get_Data:
    def __init__(self):
        pass
    def get_yaml_data(self,file_name):
        with open("./data" + os.sep + file_name, "r", encoding="utf-8") as f:
            return yaml.load(f)