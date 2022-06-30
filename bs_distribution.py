import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 5


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if value[0].isdigit():
            return scripts_common.invalid_data(idx, value[0])
        if value[1] not in validators['yes_no']:
            return scripts_common.invalid_data(idx, value[1])
        if re.search('[a-zA-Z\s]', value[2]) or value[2] == "":
            return scripts_common.invalid_data(idx, value[2])
        if re.search('[a-zA-Z\s]', value[3]) or value[3] == "":
            return scripts_common.invalid_data(idx, value[3])
        if re.search('[a-zA-Z\s]', value[4]) or value[4] == "":
            return scripts_common.invalid_data(idx, value[4])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        if value[1] == 'Yes':
            value[1] = 'Y'
        if value[1] == 'No':
            value[1] = 'N'
        line = "UPDATE d_pareto_sets " \
               "SET use_legacy_dmd_type_mapping = '" + value[1] + "', " \
               "disp_limit_for_normal_dist = " + value[2] + ", " \
               "fcst_over_ol_cvr_normal_dist = " + value[3] + ", " \
               "vmr_limit_for_poisson_dist = " + value[4] + " " \
               "WHERE pareto_set = '" + value[0] + "';"
        all_lines.append(line)
    return all_lines
