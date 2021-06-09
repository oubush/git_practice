"""Модуль с вспомогательными функциями для решения задач линейной
алгебры.
"""
import numpy as np

def det(m):
    """Считает определитель матрицы с целыми элементами"""
    m = np.array(m)
    return round(np.linalg.det(m))

def det_float(m):
    """Считает определитель матрицы с любыми элементами"""
    m = np.array(m)
    return np.linalg.det(m)

def det_solve_2(m, b):
    """Решение системы c 2 неизвестными по методу Крамера"""
    m = np.array(m)
    det_1 = det(np.column_stack([b, m[:, 1]]))
    det_2 = det(np.column_stack([m[:, 0], b]))
        
    return (det_1 / det(m), det_2 / det(m))

def det_solve_3(m, b):
    """Решение системы c 3 неизвестными по методу Крамера"""
    m = np.array(m)
    det_1 = det(np.column_stack([b, m[:, 1], m[:, 2]]))
    det_2 = det(np.column_stack([m[:, 0], b, m[:, 2]]))
    det_3 = det(np.column_stack([m[:, 0], m[:, 1], b]))
        
    return (det_1 / det(m), det_2 / det(m), det_3 / det(m))
