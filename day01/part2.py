import os
from collections import Counter
from .read_file import read_input_file

def calculate_similarity_score(left_list, right_list):
    right_counter = Counter(right_list)
    similarity_score = sum(left * right_counter[left] for left in left_list)
    return similarity_score

def read_input_file(file_path):
    left_list = []
    right_list = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

# Lire les listes à partir du fichier d'entrée
file_path = 'day01/input.txt'
left_list, right_list = read_input_file(file_path)

# Calcul du score de similarité
similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity score: {similarity_score}")