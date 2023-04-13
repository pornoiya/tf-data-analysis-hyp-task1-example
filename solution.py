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
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    z = (p1 - p2)/(p * (1-p) * ((1/x_cnt) + (1/y_cnt))) ** 0.5
    p_val = norm.sf(z)
    
    return p_val < alpha # Ваш ответ, True или False
