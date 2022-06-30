import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 2


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if value[0].isdigit():
            return scripts_common.invalid_data(idx, value[0])
        if re.search('[a-zA-Z\s]', value[1]) or value[1] == "":
            return scripts_common.invalid_data(idx, value[1])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        line = "UPDATE d_pareto_sets " \
               "SET class_calc_leng = " + value[1] + " " \
               "WHERE pareto_set = '" + value[0] + "';"
        all_lines.append(line)
    return all_lines
