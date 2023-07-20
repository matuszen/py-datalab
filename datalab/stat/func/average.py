from datalab.utils import *
from datalab.stat import sum, count

@overload
def arithmetic(*values: Union[int, float, bool]) -> float:
    """Calculate the arithmetic average of a sequence of values.

    This function accepts a variable number of arguments (int, float, or bool) and calculates
    their arithmetic average.

    Parameters
    ----------
    *values : Union[int, float, bool]
        The input values for which the arithmetic average is calculated.

    Returns
    -------
    float
        The arithmetic average of the input values.

    Raises
    ------
    ZeroDivisionError
        If no values are provided, a ZeroDivisionError is raised.

    Examples
    --------
    >>> arithmetic(1, 2, 3, 4)
    2.5

    >>> arithmetic(0, 0, 0, 0)
    0.0

    >>> arithmetic(True, False, True, True, False)
    0.6"""
    
    pass


@overload
def arithmetic(object: Iterable[Union[int, float, bool]]) -> float:
    """Calculate the arithmetic average of a sequence of values.

    This function accepts an iterable (e.g., list, tuple, or set) containing int, float, or bool
    values and calculates their arithmetic average.

    Parameters
    ----------
    values : Iterable[Union[int, float, bool]]
        The iterable containing the values for which the arithmetic average is calculated.

    Returns
    -------
    float
        The arithmetic average of the input values.

    Raises
    ------
    ValueError
        If the input iterable is empty, a ValueError is raised.

    Examples
    --------
    >>> arithmetic([1, 2, 3, 4])
    2.5

    >>> arithmetic((0, 0, 0, 0))
    0.0

    >>> arithmetic({True, False, True, True, False})
    0.6"""
    
    pass


def arithmetic(*arg: Iterable[Union[int, float, bool]]) -> float:
    if not arg:
        return 0.0
    
    try:
        return sum(arg) / count(arg)
    except TypeError:
        return sum(arg[0]) / count(arg[0])
