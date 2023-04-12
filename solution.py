import pandas as pd
import numpy as np
from scipy.stats import kstes


chat_id = 740849508 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return kstest(x, y)[1] > 0.05 # Ваш ответ, True или False
