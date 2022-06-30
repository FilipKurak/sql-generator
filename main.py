import load_item_notes
import order_cost
import load_inv_pol_values
import num_periods
import vau_boundaries
import bs_distribution
import load_coverage_buffer_stock
import newly_stocked_cells
import data_owner_loader_19_1
import item_criteria_loader_19_1
from argparse import ArgumentParser
import xlrd
import csv


def get_values_from_file(input_type):
    configuration = []

    if input_type == 'excel':
        input_file = 'csv_from_xls.csv'
    elif input_type == 'csv':
        input_file = 'INPUT_FILE'
    else:
        input_file = ''

    with open(input_file, 'r') as file:
        line = file.readline()
        while line:
            configuration.append(line.strip().split(';'))
            line = file.readline()
    return configuration


def choose_file_type(script_type):
    if script_type == 'load_inv_pol_values':
        return load_inv_pol_values
    elif script_type == 'num_periods':
        return num_periods
    elif script_type == 'vau_boundaries':
        return vau_boundaries
    elif script_type == 'bs_distribution':
        return bs_distribution
    elif script_type == 'load_coverage_buffer_stock':
        return load_coverage_buffer_stock
    elif script_type == 'order_cost':
        return order_cost
    elif script_type == 'load_item_notes':
        return load_item_notes
    elif script_type == 'newly_stocked_cells':
        return newly_stocked_cells
    elif script_type == 'data_owner_loader_19_1':
        return data_owner_loader_19_1
    elif script_type == 'item_criteria_loader_19_1':
        return item_criteria_loader_19_1
    else:
        return False


def remove_header(data_to_remove_header, remove_first_line):
    if remove_first_line == 'true':
        print('Removing header')
        del data_to_remove_header[0]
        return data_to_remove_header

    return data_to_remove_header


def write_to_file(output):
    # open file
    f = open(args.ticket_number + '_' + args.script_type + '.sql', 'w')
    # begin transaction
    f.write("BEGIN;\n")
    # add updates
    for item in output:
        f.write("%s\n" % item)
    # commit transaction and close file
    f.write("COMMIT;\n")
    f.close()


def csv_from_excel():
    wb = xlrd.open_workbook('INPUT_FILE')
    sheet_names = wb.sheet_names()
    sheet_name = args.sheet_name
    if sheet_name is None:
        sh = wb.sheet_by_name(sheet_names[0])
    else:
        sh = wb.sheet_by_name(sheet_name)
    your_csv_file = open('csv_from_xls.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_NONE, delimiter=';')

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


if __name__ == '__main__':
    # output for users
    print("********** End of boring technical stuff, script starts here ********** ")
    # parse arguments
    parser = ArgumentParser()
    parser.add_argument("--input_file", dest="input_file")
    parser.add_argument("--script_type", dest="script_type")
    parser.add_argument("--input_type", dest="input_type")
    parser.add_argument("--ticket_number", dest="ticket_number")
    parser.add_argument("--remove_header", dest="remove_header")
    parser.add_argument("--sheet_name", dest="sheet_name")
    args = parser.parse_args()

    # define values for validation purposes
    validators = {'pick_classes': ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12',
                                   'P13'],
                  'vau_classes': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12'],
                  'freq_classes': ['OnePickPeriod', 'MultPickPeriods'],
                  'currencies': ['AOA', 'AUD', 'BGN', 'BRL', 'BWP', 'CAD', 'CNY', 'DKK', 'EUR', 'GBP', 'JPY', 'LSL', 'MWK',
                                 'MZN', 'NAD', 'NOK', 'SEK', 'SLL', 'SZL', 'USD', 'ZAR'],
                  'yes_no': ['Y', 'N', 'Yes', 'No'],
                  'prefixes': ['AA', 'BE'],
                  'operators': ['=', '>', '>=', '<', '<=', '!=', 'BETWEEN', 'ISNULL', 'ISNOTNULL'],
                  'logicals': ['AND', 'OR', ' ']}

    # convert excel to csv
    if args.input_type == 'excel':
        csv_from_excel()

    # read the input file
    new_values = get_values_from_file(args.input_type)

    # set the script type
    chosen_file_type = choose_file_type(args.script_type)

    # remove header if exists
    new_values = remove_header(new_values, args.remove_header)

    # validate the input, write to file if success
    print("Validating input data")
    if chosen_file_type.validate_file(
            new_values, validators):
        print('Data validated correctly, creating script')
        write_to_file(chosen_file_type.create_updates(new_values))

    print('**********  End of script **********')

# --script_type=vau_boundaries --input_file=K030_SIMBD_VAU_Boundaries.xlsx --input_type=excel --ticket_number=TS1234
# --script_type=vau_boundaries --input_file=csv_from_xls.csv --input_type=csv --ticket_number=TEST1234
