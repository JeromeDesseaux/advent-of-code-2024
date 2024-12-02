import os
from .read_file import read_input_file

def calculate_total_distance(left_list, right_list):
    # Trier les deux listes
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculer la distance totale
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance


# Lire les listes à partir du fichier d'entrée
file_path = 'day01/input.txt'
left_list, right_list = read_input_file(file_path)

# Calcul de la distance totale
total_distance = calculate_total_distance(left_list, right_list)
print(f"Total distance: {total_distance}")