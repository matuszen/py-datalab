from datalab.utils import *

@overload
def arithmetic_average(*values: Union[int, float]) -> float:
    pass


@overload
def arithmetic_average(object: Iterable[Union[int, float]]) -> float:
    pass


def arithmetic_average(arg1: Optional[Iterable] = None) -> float:
    if arg1 is None:
        return 0.0

    pass
