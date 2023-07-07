# py-datalab

This project provides classes for working with data in python. Actually there are two classes: Matrix and Vector.

## Prerequisites

Before running this script, make sure you have the following requirements fulfilled:

- Python 3.10 or higher

## Installation

To work in your python project you only need to install it via pip:

```shell
pip install py-datalab
```

Or, to work on repository on your local machine:

```shell
git clone https://github.com/matuszen/Python-DataLab.git
```

Depend on your python version you need to install typing_extensions package

## Usage

The Matrix class represents a matrix and provides various operations and methods to work with matrices. Here are the main features of the Matrix class:

### Import

```python
import datalab as dl
```

### Initialization

To create a new matrix, you need to provide the shape (number of rows and columns) and an optional data type. The default data type is int. Here's an example of creating a matrix:

```python
matrix = dl.Matrix(3, 3, dtype=int)
matrix = dl.Matrix((3, 3), dtype=int)
matrix = dl.Matrix([[1, 2, 3], [5, 3], [2, 5, 3]])
# Lib validates shape correctly, regardless of the size of the all lists

vector = dl.Vector(4, dtype=float)
vector = dl.Vector([1, 2, 3, 4, 5])
```

### Setting and Getting Elements

You can set and get individual elements of the matrix using the square bracket notation. The indices are zero-based.

```python
# Set an element
matrix[0][0] = 1
matrix[0, 0] = 1

vector[1] = 3.0

# Get an element
element = matrix[0][0]
element = matrix[0, 0]

element = vector[1]
```

### Changing Data Type

You can change the data type of the matrix using the change_dtype method. The new data type must be one of the supported types: int, float, str, or bool.

```python
matrix.change_dtype(bool)
vector.change_dtype(int)

# Or make it via property
matrix.dtype = bool
vector.dtype = int
```

### Change size, and reshaping

You can change the shape of the matrix using the reshape method. It takes a tuple (rows, columns) as the new shape.

```python
matrix.reshape((2, 4))
matrix.reshape(2, 4)

vector.size = 5

# You can also modify shape using `rows`, `columns` and `size` property
matrix.columns += 1
matrix.rows += 1

vector.size -= 2
```

### Converting to List or Tuple

You can convert the matrix to a nested list or a tuple using the to_list and to_tuple methods, respectively.

```python
matrix_list = matrix.to_list()
matrix_tuple = matrix.to_tuple()

vector_list = vector.to_list()
vector_tuple = vector.to_tuple()
```

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code as per the terms of the license.
