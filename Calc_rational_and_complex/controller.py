import user_interface as ui
import model_rational as mr


def start_calc():
    num_type = ui.menu()
    if num_type == '1':
        value_1 = ui.common_fraction_input()
        operation = ui.operation_input()
        value_2 = ui.common_fraction_input()
        result = mr.calculation(value_1, value_2, operation)
        print('{} {} {} = {}'.format(value_1, operation, value_2, result))
    elif num_type == '2':
        print('Complex model')

start_calc()
