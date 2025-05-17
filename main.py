import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(lst).reshape(3, 3)
    calculations = {
        'mean': [list(np.mean(arr, axis=0)), list(np.mean(arr, axis=1)), np.mean(arr).item()],
        'variance': [list(np.var(arr, axis=0)), list(np.var(arr, axis=1)), np.var(arr).item()],
        'standard deviation': [list(np.std(arr, axis=0)), list(np.std(arr, axis=1)), np.std(arr).item()],
        'max': [list(np.max(arr, axis=0)), list(np.max(arr, axis=1)), np.max(arr).item()],
        'min': [list(np.min(arr, axis=0)), list(np.min(arr, axis=1)), np.min(arr).item()],
        'sum': [list(np.sum(arr, axis=0)), list(np.sum(arr, axis=1)), np.sum(arr).item()]
    }
    return calculations
