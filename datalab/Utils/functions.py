from datalab.Utils import *
from datalab.Matrix import Matrix
from datalab.Vector import Vector

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
def identity_matrix(shape: tuple[int, int], dtype: Union[int, float] = int) -> Matrix:
    """Creates an identity matrix with the specified shape

    Parameters
    ----------
    shape : Tuple[int, int]
        Shape of the identity matrix (number of rows, number of columns).
    dtype : Union[int, float], optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The identity matrix with the specified shape"""

    pass


@overload
def identity_matrix(size: int, dtype: Union[int, float] = int) -> Matrix:
    """Creates a square identity matrix with the specified size

    Parameters
    ----------
    size : int
        Size of the identity matrix (number of rows = number of columns).
    dtype : Union[int, float], optional
        Data type of the matrix elements. Default is int.

    Returns
    -------
    Matrix
        The square identity matrix with the specified size"""

    pass


def identity_matrix(
    arg1: Optional[Union[tuple[int, int], int]],
    dtype: Optional[Union[int, float]] = int,
) -> Matrix:
    if dtype not in (int, float):
        raise ValueError("dl.identity_matrix() requires dtype integer or float")

    if isinstance(arg1, int):
        return Matrix(
            [[1 if i == j else 0 for j in range(arg1)] for i in range(arg1)],
            dtype=dtype,
        )

    elif isinstance(arg1, tuple) and all(isinstance(sublist, int) for sublist in arg1):
        if arg1[0] != arg1[1]:
            raise ValueError("Identity matrix must have same rows and columns number")

        return Matrix(
            [[1 if i == j else 0 for j in range(arg1[0])] for i in range(arg1[0])],
            dtype=dtype,
        )

    else:
        raise ValueError("Wrong parameters in Matrix initialization")
