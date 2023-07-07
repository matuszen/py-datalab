from datalab.utils import *
from datalab.Matrix import Matrix
from datalab.Vector import Vector


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
