# Copyright (c) 2018 Joshua Deaton. All Rights Reserved.

import subprocess
import csv
import os.path as path


ABAQUS_SCRIPTS_DIR = path.abspath(path.join(path.dirname(__file__),
                                            "..", "abaqus_python_scripts"))


def get_frequencies(odb_name, stepname):
    system_string = "abaqus python " + \
                    path.join(ABAQUS_SCRIPTS_DIR, "abaqus_get_step_frequency_csv.py") + \
                    " " + odb_name + " " + stepname
    subprocess.Popen(system_string, shell=True)

    with open("frequency.csv") as csv_file:
        frequencies = [row[0] for row in csv.reader(csv_file)]

    return frequencies
