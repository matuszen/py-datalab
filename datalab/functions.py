from datalab.Matrix import Matrix
from datalab.Vector import Vector

from datalab.utils import *

@overload
def matrix(
    rows: int,
    columns: int,
    dtype: type = int,
    fill: Union[int, float, str, bool] = 0,
) -> Matrix:
    """Initializes a new matrix with the specified number of rows and columns.

    Parameters
    ----------
    rows : int
        The number of rows in the matrix.
    columns : int
        The number of columns in the matrix.
    dtype : type, optional
        The data type of the matrix elements (default: int).
    fill : Union[int, float, str, bool], optional
        The value used to fill the matrix elements (default: 0)"""

    pass

@overload
def matrix(
    shape: tuple[int, int],
    dtype: type = int,
    fill: Union[int, float, str, bool] = 0,
) -> Matrix:
    """Initializes a new matrix with the specified shape.

    Parameters
    ----------
    shape : tuple[int, int]
        The shape of the matrix, specified as a tuple (rows, columns).
    dtype : type, optional
        The data type of the matrix elements (default: int).
    fill : Union[int, float, str, bool], optional
        The value used to fill the matrix elements (default: 0)"""

    pass

@overload
def matrix(
    object: Iterable,
    dtype: type = IterableItemType,
) -> Matrix:
    """Initializes a new matrix from an iterable object.

    Parameters
    ----------
    object : Iterable
        An iterable object containing the matrix elements
    dtype : type, optional
        The data type of the matrix elements (default: element type from iterable object)"""

    pass

def matrix(
    arg1: Optional[Union[Iterable, tuple[int, int]]] = None,
    arg2: Optional[Union[int, type]] = None,
    dtype: Optional[type] = None,
    fill: Optional[Union[int, float, str, bool]] = 0,
) -> Matrix:
    return Matrix(arg1, arg2, dtype=dtype, fill=fill)

@overload
def vector(
    size: int,
    dtype: type = int,
    fill: Union[int, float, str, bool] = 0,
) -> Vector:
    """Initializes a vector with the specified size, data type, and fill value.

    Parameters
    ----------
    size : int
        Size of the vector.
    dtype : type, optional
        Data type of the vector elements. Default is int.
    fill : int or float or str or bool, optional
        Value used to fill the vector. Default is 0."""

    pass

@overload
def vector(
    object: Iterable,
    dtype: type = IterableItemType,
) -> Vector:
    """Initializes a vector from an iterable object.

    Parameters
    ----------
    object : Iterable
        Iterable object containing the data for the vector.
    dtype : type, optional
        Data type of the vector elements. Default is Iterable items type."""
    pass

def vector(
    arg1: Optional[Union[Iterable, int]],
    dtype: Optional[type] = None,
    fill: Optional[Union[int, float, str, bool]] = 0,
) -> Vector:
    return Vector(arg1, dtype=dtype, fill=fill)

@overload
def zeros_matrix(rows: int, columns: int, dtype: Union[int, float] = int) -> Matrix:
    """Creates a matrix filled with zeros of the specified shape

    Parameters
    ----------
    rows : int
        Number of rows in the matrix.
    columns : int
        Number of columns in the matrix.
    dtype : Union[int, float], optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The matrix filled with zeros of the specified shape"""

    pass


@overload
def zeros_matrix(shape: tuple[int, int], dtype: Union[int, float] = int) -> Matrix:
    """Creates a matrix filled with zeros of the specified shape

    Parameters
    ----------
    shape : Tuple[int, int]
        Shape of the matrix (number of rows, number of columns).
    dtype : Union[int, float], optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The matrix filled with zeros of the specified shape"""

    pass


def zeros_matrix(
    arg1: Optional[Union[int, tuple[int, int]]],
    arg2: Optional[int],
    dtype: Optional[Union[int, float]] = int,
) -> Matrix:
    if dtype not in (int, float):
        raise ValueError("dl.zeros_matrix() requires dtype integer or float")

    if isinstance(arg1, int) and isinstance(arg2, int):
        return Matrix(arg1, arg2, dtype=dtype, fill=0)

    elif isinstance(arg1, tuple):
        return Matrix(arg1, dtype=dtype, fill=0)

    raise ValueError("Wrong parameters in Matrix initialization")


@overload
def ones_matrix(rows: int, columns: int, dtype: Union[int, float] = int) -> Matrix:
    """Creates a matrix filled with ones of the specified shape

    Parameters
    ----------
    rows : int
        Number of rows in the matrix.
    columns : int
        Number of columns in the matrix.
    dtype : Union[int, float], optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The matrix filled with ones of the specified shape"""

    pass


@overload
def ones_matrix(shape: tuple[int, int], dtype: Union[int, float] = int) -> Matrix:
    """Creates a matrix filled with ones of the specified shape

    Parameters
    ----------
    shape : Tuple[int, int]
        Shape of the matrix (number of rows, number of columns).
    dtype : Union[int, float], optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The matrix filled with ones of the specified shape"""

    pass


def ones_matrix(
    arg1: Optional[Union[int, tuple[int, int]]],
    arg2: Optional[int],
    dtype: Optional[Union[int, float]] = int,
) -> Matrix:
    if dtype not in (int, float):
        raise ValueError("dl.ones_matrix() requires dtype integer or float")

    if isinstance(arg1, int) and isinstance(arg2, int):
        return Matrix(arg1, arg2, dtype=dtype, fill=1)

    elif isinstance(arg1, tuple):
        return Matrix(arg1, dtype=dtype, fill=1)

    raise ValueError("Wrong parameters in Matrix initialization")


def zeros_vector(
    size: int,
    dtype: Union[int, float] = int,
) -> Vector:
    """Creates a vector filled with zeros of the specified size

    Parameters
    ----------
    size : int
        Size of the vector.
    dtype : Union[int, float], optional
        Data type of the vector elements. Default is int.

    Returns
    -------
    Vector
        The vector filled with zeros of the specified size.

    Raises
    ------
    ValueError
        If the dtype is not int or float"""

    if dtype not in (int, float):
        raise ValueError("dl.zeros_vector() requires dtype integer or float")

    if isinstance(size, int):
        return Vector(size, dtype=dtype, fill=0)

    raise ValueError("Wrong parameters in Vector initialization")


def ones_vector(
    size: int,
    dtype: Union[int, float] = int,
) -> Vector:
    """Creates a vector filled with ones of the specified size

    Parameters
    ----------
    size : int
        Size of the vector.
    dtype : Union[int, float], optional
        Data type of the vector elements. Default is int.

    Returns
    -------
    Vector
        The vector filled with ones of the specified size.

    Raises
    ------
    ValueError
        If the dtype is not int or float"""

    if dtype not in (int, float):
        raise ValueError("dl.ones_vector() requires dtype integer or float")

    if isinstance(size, int):
        return Vector(size, dtype=dtype, fill=1)

    raise ValueError("Wrong parameters in Vector initialization")


@overload
def identity(size: int, dtype: Union[int, float] = int) -> Matrix:
    """Creates a square identity matrix with the specified size.

    Parameters
    ----------
    size : int
        Size of the identity matrix (number of rows = number of columns).
    dtype : int or float, optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The square identity matrix with the specified size.
        
    Raises
    ------
    TypeError
        If the provided dtype is not int or float, or if the arguments have invalid types for identity matrix creation.
    """

    pass


@overload
def identity(rows: int, columns: int, dtype: Union[int, float] = int) -> Matrix:
    """Creates an identity matrix with the specified dimensions.

    Parameters
    ----------
    rows : int
        Number of rows.
    columns : int
        Number of columns.
    dtype : int or float, optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The identity matrix with the specified shape.
        
    Raises
    ------
    TypeError
        If the provided dtype is not int or float, or if the arguments have invalid types for identity matrix creation.
    ValueError
        If the size of the identity matrix is not square (rows != columns).
    """
        
    pass


@overload
def identity(shape: tuple[int, int], dtype: Union[int, float] = int) -> Matrix:
    """Creates an identity matrix with the specified shape.

    Parameters
    ----------
    shape : tuple[int, int]
        Shape of the identity matrix (number of rows, number of columns).
    dtype : int or float, optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The identity matrix with the specified shape.
        
    Raises
    ------
    TypeError
        If the provided dtype is not int or float, or if the arguments have invalid types for identity matrix creation.
    ValueError
        If the size of the identity matrix is not square (rows != columns).
    """

    pass


def identity(
    arg1: Optional[Union[int, tuple[int, int]]],
    arg2: Optional[int] = None,
    dtype: Optional[Union[int, float]] = int,
) -> Matrix:
    """Creates an identity matrix of specified size and data type.
    
    The identity matrix is a square matrix with 1's on the main diagonal and 0's elsewhere. 
    It is created with either a single integer representing the number of rows and columns, or a tuple of two integers representing the size.
    If a dtype is specified, it sets the data type for the matrix elements. 
    If the provided size is not square, a ValueError is raised.

    Example
    -------
    >>> identity1 = identity(3)
    >>> print(identity1)
    │ 1 0 0 │
    │ 0 1 0 │
    │ 0 0 1 │

    >>> identity2 = identity((4, 4), dtype=float)
    >>> print(identity2)
    │ 1.0 0.0 0.0 0.0 │
    │ 0.0 1.0 0.0 0.0 │
    │ 0.0 0.0 1.0 0.0 │
    │ 0.0 0.0 0.0 1.0 │
    """
    
    if dtype not in (int, float):
        raise TypeError("Identity matrix requires dtype integer or float")

    if isinstance(arg1, int):
        if arg2 is not None and arg1 != arg2:
            raise ValueError("Identity matrix must have same rows and columns number")
        
        return Matrix(
            [[1 if i == j else 0 for j in range(arg1)] for i in range(arg1)],
            dtype=dtype,
        )

    elif isinstance(arg1, tuple) and all(isinstance(item, int) for item in arg1):
        rows, columns = arg1
        
        if rows != columns:
            raise ValueError("Identity matrix must have same rows and columns number")

        return Matrix(
            [[1 if i == j else 0 for j in range(rows)] for i in range(rows)],
            dtype=dtype,
        )

    else:
        raise TypeError("Wrong parameters in Matrix initialization")
