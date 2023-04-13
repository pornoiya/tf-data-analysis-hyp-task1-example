import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 146155552 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    mean1 = x_success/ x_cnt
    mean2 = y_success/ y_cnt
    return mean2-mean1 < alpha
