import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 4


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if value[0].isdigit():
            return scripts_common.invalid_data(idx, value[0])
        if not value[1] in validators['vau_classes']:
            return scripts_common.invalid_data(idx, value[1])
        if re.search('[a-zA-Z\s]', value[2]) or value[2] == "":
            return scripts_common.invalid_data(idx, value[2])
        if value[3] not in validators['currencies']:
            return scripts_common.invalid_data(idx, value[3])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        line = "UPDATE d_pareto_vau " \
               "SET vau_boundary = " + value[2] + ", " \
               "vau_currency = '" + value[3] + "' " \
               "WHERE VAU_class = '" + value[1] + "' " \
               "AND inventory_policy_id = " \
               "(select id from d_pareto_sets where pareto_set = '" + value[0] + "');"
        all_lines.append(line)
    return all_lines
