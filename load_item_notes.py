import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 5


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if value[0].isdigit():
            return scripts_common.invalid_data(idx, value[0])
        if value[2] not in validators['prefixes']:
            return scripts_common.invalid_data(idx, value[2])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        line = "UPDATE d_item " \
               "SET notes = '" + value[4] + "' " \
               "WHERE item_code = '" + value[1] + "' AND local_prefix ='" + value[2] + "' " \
               "AND warehouse_id=(SELECT w.id from d_warehouse w " \
               "JOIN d_warehouse_group wg ON w.warehouse_group_id=wg.id " \
               "WHERE wg.warehouse_group_code = '" + value[0] + "' AND w.warehouse_code='" + value[3] + "');"
        all_lines.append(line)
    return all_lines
