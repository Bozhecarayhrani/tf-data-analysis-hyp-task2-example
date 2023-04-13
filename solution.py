import pandas as pd
import numpy as np
from scipy import stats


chat_id = 740849508 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return stats.anderson_ksamp([x, y])[1] > 0.05 # Ваш ответ, True или False
