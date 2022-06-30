import scripts_common
import re

EXPECTED_NUMBER_OF_PARAMETERS = 7


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
        if value[4].isdigit():
            return scripts_common.invalid_data(idx, value[4])
        if re.search('[a-zA-Z]', value[6]):
            return scripts_common.invalid_data(idx, value[6])
    return True


def create_updates(data_to_transform):
    all_lines = []
    for idx, value in enumerate(data_to_transform):
        if value[4] == '':
            value[4] = 'null'
        if value[5] == '':
            value[5] = 'null'
        if value[6] == '':
            value[6] = 'null'

        if value[4] == 'null':
            line = "UPDATE d_inventory_policy_cell " \
                   "SET fcst_coverage_base=" + value[4] + ", " \
                   "min_bs_coverage_days=" + value[5] + ", " \
                   "max_bs_coverage_days=" + value[6] + "  " \
                   "where fre_class='" + value[1] + "' " \
                   "AND pic_class='" + value[2] + "' " \
                   "AND vau_class='" + value[3] + "' " \
                   "AND inventory_policy_id = (select id from d_pareto_sets where pareto_set='" + value[0] + "');"
        else:
            line = "UPDATE d_inventory_policy_cell " \
                   "SET fcst_coverage_base='" + value[4] + "', " \
                   "min_bs_coverage_days=" + value[5] + ", " \
                   "max_bs_coverage_days=" + value[6] + "  " \
                   "where fre_class='" + value[1] + "' " \
                   "AND pic_class='" + value[2] + "' " \
                   "AND vau_class='" + value[3] + "' " \
                   "AND inventory_policy_id = (select id from d_pareto_sets where pareto_set='" + value[0] + "');"
        all_lines.append(line)
    return all_lines
