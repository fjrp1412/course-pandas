import numpy as np

if __name__ == '__main__':
    np_array = np.array([1, 2, 3, 4, 5])  # Array de numpy
    array = [1, 2, 3, 4, 5]  # Array de python
    print(np_array)
    print(array)
    print(array + [10])
    print(np_array + 10)
    np_array = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
    print(np_array.shape)
    print(np_array[0])

