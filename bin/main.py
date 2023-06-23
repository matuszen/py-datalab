from utils import *


class sheet:
    def __init__(
        self,
        shape: tuple[int, int],
        dtype: tuple = int,
    ) -> None:
        self.shape = shape
        self.dtype = dtype

        self._initialize_data()

    def __str__(self) -> str:
        max_element_length = max(
            len(str(value)) for row in self.__data for value in row
        )

        output = ""

        for row in self.__data:
            for value in row:
                if self.dtype == float:
                    formatted_value = (
                        f".{value:.0f}" if value % 1 == 0 else f"{value:.2f}"
                    )

                elif self.dtype == int:
                    formatted_value = f"{value:d}"

                elif self.dtype == bool:
                    formatted_value = str(value)

                else:
                    formatted_value = str(value)

                value_size = len(formatted_value)
                output += f"{formatted_value}{' ' * (max_element_length - value_size)} "

            output += "\n"

        return output

    def _initialize_data(self) -> None:
        if self.__dtype == float:
            init_data = 0.0

        elif self.__dtype == str:
            init_data = "''"

        elif self.__dtype == bool:
            init_data = False

        else:
            init_data = 0

        self.__data = [
            [init_data for _ in range(self.columns)] for _ in range(self.rows)
        ]

        self.__size = self.shape[0] * self.shape[1]

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, new_value: int) -> None:
        if isinstance(new_value, int):
            self.__columns = new_value
        else:
            raise ValueError("`dl.sheet.columns` property must be an integer")

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, new_value: int) -> None:
        if isinstance(new_value, int):
            self.__rows = new_value
        else:
            raise ValueError("`dl.sheet.rows` property must be an integer")

    @property
    def shape(self) -> tuple[int, int]:
        return self.__shape

    @shape.setter
    def shape(self, new_value: tuple[int, int]) -> None:
        if isinstance(new_value, tuple):
            self.__shape = new_value
            self.columns = new_value[0]
            self.rows = new_value[1]
        else:
            raise ValueError("`dl.sheet.shape` property must be an tuple of integers")

    @property
    def dtype(self) -> type:
        return self.__dtype

    @dtype.setter
    def dtype(self, new_value: type) -> None:
        if new_value in (int, float, str, bool):
            self.__dtype = new_value

        else:
            raise ValueError("`dl.sheet.dtype` property must be an type object")

    @property
    def size(self) -> int:
        return self.__size
