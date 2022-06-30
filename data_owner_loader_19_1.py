import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 13


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):

        if value[1] != '' and value[2] == '' and value[3] == '':
            line = "INSERT INTO d_data_owner SELECT " \
                   "max(ddo.id) + 1, " \
                   "'" + value[0] + "', " \
                   "dw.id, " \
                   "null, " \
                   "null, " \
                   "'N', " \
                   "'EUR', " \
                   "null, " \
                   "null, " \
                   "null, " \
                   "'N', " \
                   "'Y', " \
                   "'N', " \
                   "'NEVER'" \
                   " from D_DATA_OWNER ddo, D_WAREHOUSE dw where dw.warehouse_code = '" + value[1] + "' GROUP BY dw.id;"
        elif value[1] == '' and value[2] != '' and value[3] == '':
            line = "INSERT INTO d_data_owner SELECT " \
                   "max(ddo.id) + 1, " \
                   "'" + value[0] + "', " \
                   "null, " \
                   "dwg.id, " \
                   "null, " \
                   "'N', " \
                   "'EUR', " \
                   "null, " \
                   "null, " \
                   "null, " \
                   "'N', " \
                   "'Y', " \
                   "'N', " \
                   "'NEVER'" \
                   " from D_DATA_OWNER ddo, D_WAREHOUSE_GROUP dwg where dwg.warehouse_group_code = '" + value[2] \
                   + "' GROUP BY dwg.id;"
        elif value[1] == '' and value[2] == '' and value[3] != '':
            line = "INSERT INTO d_data_owner SELECT " \
                   "max(ddo.id) + 1, " \
                   "'" + value[0] + "', " \
                   "null, " \
                   "null, " \
                   "dwsg.id, " \
                   "'N', " \
                   "'EUR', " \
                   "null, " \
                   "null, " \
                   "null, " \
                   "'N', " \
                   "'Y', " \
                   "'N', " \
                   "'NEVER'" \
                   " from D_DATA_OWNER ddo, d_warehouse_super_group dwsg where dwsg.name = '" + value[3] \
                   + "' GROUP BY dwg.id;"
        elif value[1] != '' and value[2] != '' and value[3] == '':
            line = "INSERT INTO d_data_owner SELECT " \
                   "max(ddo.id) + 1, " \
                   "'" + value[0] + "', " \
                   "dw.id, " \
                   "null, " \
                   "null, " \
                   "'N', " \
                   "'EUR', " \
                   "null, " \
                   "null, " \
                   "null, " \
                   "'N', " \
                   "'Y', " \
                   "'N', " \
                   "'NEVER'" \
                   " from D_DATA_OWNER ddo, d_warehouse dw, d_warehouse_group dwg" \
                   " where dwg.id = dw.warehouse_group_id and dw.warehouse_code = '" + value[1] + "'" \
                   " and dwg.warehouse_group_code = '" + value[2] + "'" \
                   " GROUP BY dw.id;"
        else:
            line = "ERROR!"
        all_lines.append(line)
    return all_lines
