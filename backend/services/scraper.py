import time

def read_local_data():
    with open("../database/sample_data.txt", "r") as f:
        return f.read()