.PHONY: part1 part2 run

# Default input file directory
INPUT_DIR = input
DAY ?= 01

# Targets
part1:
	python -m day$(DAY).part1

part2:
	python -m day$(DAY).part2

run: part1 part2
