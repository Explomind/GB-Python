import user_interface as ui
import model_rational as mr

def start_calc():
    value_1 = ui.common_fraction_input()
    value_2 = ui.common_fraction_input()
    mr.init(value_1, value_2)
    result_sum = mr.fraction_simpl(mr.sum_fract())
    result_subtract = mr.fraction_simpl(mr.subtract())
    return (result_sum, result_subtract)

sum_1, sub_1 = start_calc()
print('Sum = {}\nSubtraction = {}'.format(sum_1, sub_1))