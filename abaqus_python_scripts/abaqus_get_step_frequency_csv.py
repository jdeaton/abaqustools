""" Abaqus Python post-processing script for frequency analysis step.

System String Format:
`abaqus python abaqus_get_step_frequency.py`

Creates a .csv file containing the natural frequencies from a linear
perturbation frequency (normal modes) analysis step from an Abaqus
.odb output database file.

Copyright (c) 2018 Joshua Deaton. All Rights Reserved.
"""

# Abaqus Python imports.
from odbAccess import openOdb
from textRepr import *

# Python imports.
import sys
import csv


def main(argv):
    odb_file, step_key, out_file = process_command_line_input(argv)

    abaqus_odb = openOdb(odb_file)
    abaqus_frequency_step = abaqus_odb.steps[step_key]

    frequencies = get_frequencies(abaqus_frequency_step)

    write_csv(frequencies, out_file)


def process_command_line_input(argv):
    assert(len(argv) > 2)

    odb_file = argv[1]
    step_key = argv[2]

    if len(argv > 3):
        out_file = argv[3]
    else:
        out_file = "frequency.csv"

    return odb_file, step_key, out_file


def get_frequencies(frequency_step):
    frequencies = []
    for frame in frequency_step.frames:
        frequencies.append(frame.frequency)
    return frequencies


def write_csv(out_file, frequencies):
    with open(out_file, "w") as csv_file:
        for freq in frequencies:
            csv.writer(csv_file, dialect='excel').writerows(frequencies)


if __name__ == "__main__":
    main(sys.argv)




