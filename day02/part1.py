import os
from .read_file import read_input_file

def is_safe_report(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))

# Lire les rapports à partir du fichier d'entrée
file_path = 'day02/input.txt'
reports = read_input_file(file_path)

# Compter le nombre de rapports sûrs
safe_reports_count = count_safe_reports(reports)
print(f"Number of safe reports: {safe_reports_count}")