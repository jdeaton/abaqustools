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


def write_keyword_input_file(new_file, template_file, variables):
    """
    """
    with open(template_file, "r") as template:
        with open(new_file, "w") as input_file:
            for line in template:
                for var_name in variables.keys():
                    line = line.replace(var_name, repr(variables[var_name]))
                input_file.write(line)
              
def run_abaqus(input_file):
    to_shell = "abaqus job=" + input_file + " interactive ask_delete=OFF"
    subprocess.call(to_shell, shell=True)