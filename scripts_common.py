def invalid_number_of_parameters(expected, received, line):
    print('*** Data validated correctly! ***')
    print('Invalid number of parameters on line ' + str(line + 1))
    print('Expected ' + str(expected) + ', got ' + str(received))


def invalid_data(line_number, invalid_data):
    print('*** Data validated incorrectly! ***')
    print('Value ' + str(invalid_data) + ' in line ' + str(line_number + 1) + ' did not pass validation')
    return False
