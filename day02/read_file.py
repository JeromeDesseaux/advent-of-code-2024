import os

def read_input_file(file_path):
    reports = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            reports.append(report)
    return reports