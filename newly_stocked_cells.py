import scripts_common

EXPECTED_NUMBER_OF_PARAMETERS = 4


def validate_file(data_to_validate, validators):
    for idx, value in enumerate(data_to_validate):
        if len(value) != EXPECTED_NUMBER_OF_PARAMETERS:
            return scripts_common.invalid_number_of_parameters(EXPECTED_NUMBER_OF_PARAMETERS, len(value), idx)
        if value[0].isdigit():
            return scripts_common.invalid_data(idx, value[0])
        if value[1] not in validators['freq_classes']:
            return scripts_common.invalid_data(idx, value[1])
        if value[2] not in validators['pick_classes']:
            return scripts_common.invalid_data(idx, value[2])
        if value[3] not in validators['vau_classes']:
            return scripts_common.invalid_data(idx, value[3])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        line = "UPDATE d_inventory_policy_cell " \
               "SET STOCKED = 'Y' " \
               "WHERE VAU_CLASS = '" + value[3] + "' " \
               "AND PIC_CLASS = '" + value[2] + "' " \
               "AND FRE_CLASS = '" + value[1] + "' " \
               "AND inventory_policy_id = (select id from d_pareto_sets where PARETO_SET = '" + value[0] + "');"
        all_lines.append(line)
    return all_lines
