""" Abaqus Python post-processing script for steady state dynamics step.

System String Format:
`abaqus python abaqus_get_step_steady_state_dynamics.py`

Creates a .csv file containing the data contained in a specific variable from
a specified history output region in a steady state dynamics from an Abaqus
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
    odb_file, step_key, hist_reg, var_name, out_file = \
        process_command_line_input(argv)

    abaqus_odb = openOdb(odb_file)
    abaqus_ss_dynamics_step = abaqus_odb.steps[step_key]
    abaqus_history_region = abaqus_ss_dynamics_step.historyRegions[hist_reg]
    history_data = abaqus_history_region.historyOutputs[var_name].data

    write_csv(out_file, history_data)


def process_command_line_input(argv):
    assert(len(argv) > 4)

    odb_file = argv[1]
    step_key = argv[2]
    hist_reg = argv[3]
    var_name = argv[4]

    if len(argv) > 5:
        out_file = argv[5]
    else:
        out_file = "steady_state_dynamics.csv"

    return odb_file, step_key, hist_reg, var_name, out_file


def write_csv(out_file, history_data):
    with open(out_file, "wb") as csv_file:
            csv.writer(csv_file, dialect='excel').writerows(history_data)


if __name__ == "__main__":
    main(sys.argv)




