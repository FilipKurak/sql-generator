import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 6


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if re.search('[a-zA-Z\s]', value[2]) or value[2] == "":
            return scripts_common.invalid_data(idx, value[2])
        if value[3] not in validators['currencies']:
            return scripts_common.invalid_data(idx, value[3])
        if re.search('[a-zA-Z\s]', value[4]) or value[4] == "":
            return scripts_common.invalid_data(idx, value[4])
        if re.search('[a-zA-Z\s]', value[5]) or value[5] == "":
            return scripts_common.invalid_data(idx, value[5])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        line = "UPDATE d_warehouse_settings " \
               "SET ordering_cost = " + value[2] + ", " \
               "ordering_cost_currency = '" + value[3] + "', " \
               "interest_rate = " + value[4] + ", " \
               "stock_holding_cost_rate = " + value[5] + " " \
               "WHERE warehouse_id = (SELECT dw.id " \
               "from d_warehouse dw join d_warehouse_group dwg on dw.warehouse_group_id = dwg.id " \
               "WHERE dwg.warehouse_group_code = '" + value[0] + "'" \
               " and dw.warehouse_code = '" + value[1] + "');"
        all_lines.append(line)
    return all_lines
