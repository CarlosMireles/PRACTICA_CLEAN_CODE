"""
Created on Sun Feb 16 18:48:12 2025

@author: Carlos Mireles Rodríguez
"""


class Array1D:
    """
    A class representing a one dimensional array. 
    
    Attributes:
    
    array: list[int]
        A list of integers representing the array values.
    
    Methods:
    
    __init__(lower_bound: int = None, upper_bound: int = None, values: list[int] = None)
        Initializes the array using a range or a predefined list of values.
    
    _validate_upper_and_lower_bounds(upper_bound, lower_bound)
        Validates that lower_bound and upper_bound are non-negative and lower_bound < upper_bound.
    
    __add__(other)
        Returns a new Array1D instance with element-wise addition.
        
    __sub__(other)
        Returns a new Array1D instance with element-wise subtraction.
    
    difference(other)
        Returns a new Array1D instance with the absolute difference between elements.
    
    _validate_same_length(other)
        Checks if two arrays have the same length.
    
    __len__()
        Returns the length of the array.
    
    __str__()
        Returns the string representation of the array.
    
    mean()
        Returns the mean of the array elements.
    
    max()
        Returns the maximum value in the array.
    
    min()
        Returns the minimum value in the array.
    """
    
    
    def __init__(self, lower_bound: int = None, upper_bound: int = None, values: list[int] = None):
        if values is not None:
            self.array = values
        elif lower_bound is not None and upper_bound is not None:
            self._validate_upper_and_lower_bounds(upper_bound, lower_bound)
            self.array = [i for i in range(lower_bound, upper_bound)]
        else:
            raise ValueError("Se debe proporcionar un rango o una lista de valores.")
    
    def _validate_upper_and_lower_bounds(self, upper_bound, lower_bound):
        if lower_bound < 0 or upper_bound < 0:
            raise ValueError("Los limites no pueden ser negativos")
        elif lower_bound >= upper_bound:
            raise ValueError("El límite inferior debe ser menor que el límite superior.")
    
    def __add__(self, other):
        self._validate_same_length(other)
        return Array1D(values=[a + b for a,b in zip(self.array, other.array)])
    
    def __sub__(self, other):
        self._validate_same_length(other)
        return Array1D(values=[a - b for a,b in zip(self.array, other.array)])
    
    def difference(self, other):
        self._validate_same_length(other)
        return Array1D(values=[abs(a - b) for a,b in zip(self.array, other.array)])
    
    def _validate_same_length(self, other):
        if len(self) != len(other):
            raise ValueError("Los vectores tienen distintas longitudes.")
    
    def __len__(self):
        return len(self.array)
    
    def __str__(self):
        return str(self.array)
    
    def mean(self):
        return sum(self.array) / len(self.array)
    
    def max(self):
        return max(self.array)
    
    def min(self):
        return min(self.array)




vector_from_0_to_100 = Array1D(0, 100)
print(vector_from_0_to_100)

vector_from_100_to_200 = Array1D(100, 200)
print(vector_from_100_to_200)

sum_of_arrays = vector_from_0_to_100 + vector_from_100_to_200
print(sum_of_arrays)

difference_of_arrays = vector_from_0_to_100.difference(vector_from_100_to_200)
print(difference_of_arrays)

print("Mean of the first array: ", vector_from_0_to_100.mean())
print("Mean of the second array: ", vector_from_100_to_200.mean())

print("First array maximum: ", vector_from_0_to_100.max())
print("First array minimum: ", vector_from_0_to_100.min())

print("Mean of the array with the sum: ", sum_of_arrays.mean())
print("Mean of the array with the difference: ", difference_of_arrays.mean())

print("Second array maximum: ", vector_from_100_to_200.max())
print("Second array minimum: ", vector_from_100_to_200.min())

print("Maximum of the array with the sum: ", sum_of_arrays.max())
print("Minimum of the array with the sum: ", sum_of_arrays.min())

print("Maximum of the array with the difference: ", difference_of_arrays.max())
print("Minimum of the array with the difference: ", difference_of_arrays.min())


try:
    vector_lower_bound_negative = Array1D(-2, 3)
except ValueError as error:
    print(error)
    
try:
    vector_higher_bound_negative = Array1D(2, -3)
except ValueError as error:
    print(error)
    
try:
    vector_both_bounds_negative = Array1D(-2, -3)
except ValueError as error:
    print(error)

vector_from_0_to_50 = Array1D(0, 50)
vector_from_0_to_200 = Array1D(0,200)

try:
    sum_of_arrays = vector_from_0_to_50 + vector_from_0_to_200
except ValueError as error:
    print(error)

try:
    subtraction_of_arrays = vector_from_0_to_50 + vector_from_0_to_200
except ValueError as error:
    print(error)

try:
    difference_of_arrays = vector_from_0_to_50 + vector_from_0_to_200
except ValueError as error:
    print(error)
    
vector_from_8_to_13 = Array1D(8, 13)
vector_from_array = Array1D(values=[-2, 4, 5, 0, -8])

print(vector_from_8_to_13)
print(vector_from_array)

subtraction_of_arrays = vector_from_8_to_13 - vector_from_array
print(subtraction_of_arrays)