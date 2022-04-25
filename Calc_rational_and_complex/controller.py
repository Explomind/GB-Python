import user_interface as ui
import model_rational as mr
import model_complex as mc
import logger


def start_calc():
    num_type = ui.menu()
    if num_type == '1':
        value_1 = ui.common_fraction_input()
        operation = ui.operation_input()
        value_2 = ui.common_fraction_input()
        result = mr.calculation(value_1, value_2, operation)
        result_str = '{} {} {} = {}'.format(value_1, operation, value_2, result)
        # print(result_str)
        # logger.write_log(result_str)
    elif num_type == '2':
        value_1 = ui.complex_num_input()
        operation = ui.operation_input()
        value_2 = ui.complex_num_input()
        result = mc.calculation(value_1, value_2, operation)
        result_str = '{} {} {} = {}'.format(value_1, operation, value_2, result)
    print(result_str)
    logger.write_log(result_str)
