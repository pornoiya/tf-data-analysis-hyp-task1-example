import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import proportions_ztest


chat_id = 146155552 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    prop_control = x_success / x_cnt
    prop_test = y_success / y_cnt

    z_stat, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')

    return z_stat > 1.555
