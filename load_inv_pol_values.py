import scripts_common

EXPECTED_NUMBER_OF_PARAMETERS = 24


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if value[1].isdigit():
            return scripts_common.invalid_data(idx, value[1])
        if value[2] not in validators['freq_classes']:
            return scripts_common.invalid_data(idx, value[2])
        if value[3] not in validators['vau_classes']:
            return scripts_common.invalid_data(idx, value[3])
        if value[4] not in validators['pick_classes']:
            return scripts_common.invalid_data(idx, value[4])
        if value[5] != 'VDEFAULT':
            return scripts_common.invalid_data(idx, value[5])
        if value[7] not in validators['yes_no']:
            return scripts_common.invalid_data(idx, value[7])
        if value[20] not in validators['yes_no']:
            return scripts_common.invalid_data(idx, value[20])
        if value[21] not in validators['yes_no']:
            return scripts_common.invalid_data(idx, value[21])
        if value[22] not in validators['yes_no']:
            return scripts_common.invalid_data(idx, value[22])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        line = "UPDATE d_inventory_policy_cell " \
               "SET STOCKED = '" + value[7] + "', " \
               "TSL_SLOW = " + value[8] + ", " \
               "TSL_NORMAL = " + value[9] + ", " \
               "TSL_LUMPY = " + value[10] + ", " \
               "ORDERS_PER_YEAR = " + value[11] + ", " \
               "MIN_ECONOMIC_NUM_OOPY_ITEM = " + value[18] + ", " \
               "MAX_ECONOMIC_NUM_OOPY_ITEM = " + value[19] + ", " \
               "STK_OPT_NORMAL = '" + value[20] + "', " \
               "STK_OPT_SLOW = '" + value[21] + "', " \
               "STK_OPT_LUMPY = '" + value[22] + "' " \
               "WHERE VAU_CLASS = '" + value[3] + "' " \
               "AND PIC_CLASS = '" + value[4] + "' " \
               "AND FRE_CLASS = '" + value[2] + "' " \
               "AND VOL_CLASS = '" + value[5] + "' " \
               "AND inventory_policy_id = (select id from d_pareto_sets where PARETO_SET = '" + value[1] + "');"
        all_lines.append(line)
    return all_lines
