import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 7


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if value[2] not in validators['operators']:
            return scripts_common.invalid_data(idx, value[2])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        if value[6] == '':
            value[6] = 'null'
        if value[4] == '':
            value[4] = ' '
        line = "INSERT INTO d_category_filter_exp SELECT " \
               "ddo.id, " \
               + value[1] + ", " \
               "'" + value[2] + "', " \
               "'" + value[3] + "', " \
               "'" + value[4] + "', " \
               "'" + value[5] + "', " \
               "" + value[6] + " " \
               " from D_DATA_OWNER ddo where ddo.name = '" + value[0] \
               + "';"
        all_lines.append(line)
    return all_lines
