from utils import *


class Matrix:
    def __init__(
        self,
        shape: tuple[int, int],
        dtype: type = int,
    ) -> None:
        self.__rows, self.__columns = shape
        self.__dtype = dtype

        self.__precision = 4

        self._initialize_data()

    def __str__(self) -> str:
        buffer = [[" " for _ in range(self.columns)] for _ in range(self.rows)]

        for i, row in enumerate(self.__data):
            for j, value in enumerate(row):
                if self.dtype == float:
                    splited_value = str(value).split(".")

                    if len(splited_value) == 1:
                        if splited_value[0] == "0":
                            formatted_value = f"0."

                        else:
                            formatted_value = f"{splited_value[0]}.0"

                    if len(splited_value) == 2:
                        if splited_value[0] == "0" and splited_value[1] == "0":
                            formatted_value = f"0."

                        elif splited_value[0] == "0" and splited_value[1] != "0":
                            if len(splited_value[1]) > self.__precision:
                                formatted_value = "{:.{}e}".format(
                                    value, self.__precision
                                )
                            else:
                                formatted_value = f"0.{splited_value[1]}"

                        else:
                            if len(splited_value[1]) > self.__precision:
                                formatted_value = "{:.{}e}".format(
                                    value, self.__precision
                                )
                            else:
                                formatted_value = (
                                    f"{splited_value[0]}.{splited_value[1]}"
                                )

                elif self.dtype == int:
                    formatted_value = str(value)

                elif self.dtype == bool:
                    formatted_value = str(value)

                else:
                    formatted_value = f"'{str(value)}'"

                buffer[i][j] = formatted_value

        max_element_lengths = tuple(
            max(len(str(row[i])) for row in buffer) for i in range(len(buffer[0]))
        )

        output = ""

        for row in buffer:
            output += "| "
            for value, max_length in zip(row, max_element_lengths):
                output += f"{value}{' ' * (max_length - len(value) + 1)}"

            output += "|\n"

        return output

    def __setitem__(self, index: int, value: object) -> None:
        if isinstance(index, tuple) and len(index) == 2:
            rows, columns = index
            if self.dtype == int:
                self.__data[rows][columns] = int(value)

            elif self.dtype == float:
                self.__data[rows][columns] = float(value)

            elif self.dtype == str:
                self.__data[rows][columns] = str(value)

            elif self.dtype == bool:
                self.__data[rows][columns] = bool(value)
        else:
            if self.dtype == int:
                self.__data[index] = int(value)

            elif self.dtype == float:
                self.__data[index] = float(value)

            elif self.dtype == str:
                self.__data[index] = str(value)

            elif self.dtype == bool:
                self.__data[index] = bool(value)

    def __getitem__(self, index: int) -> object:
        if isinstance(index, tuple) and len(index) == 2:
            rows, columns = index
            return self.__data[rows][columns]

        return self.__data[index]

    def _empty_element(self) -> int | float | str | bool:
        if self.dtype == float:
            return 0.0

        elif self.dtype == str:
            return ""

        elif self.dtype == bool:
            return False

        else:
            return 0

    def _initialize_data(self) -> None:
        init_item = self._empty_element()

        self.__data = [
            [init_item for _ in range(self.columns)] for _ in range(self.rows)
        ]

    def _adjust_dimensions(self) -> None:
        buffer = self.__data.copy()

        init_item = self._empty_element()

        self.__data = [
            [init_item for _ in range(self.columns)] for _ in range(self.rows)
        ]

        for i in range(self.rows):
            for j in range(self.columns):
                try:
                    self.__data[i][j] = buffer[i][j]
                except:
                    continue

    def _change_data_type(self, new_dtype: type) -> None:
        temp_fun = lambda x: new_dtype(x)

        for i in range(self.columns):
            for j in range(self.rows):
                self.__data[i][j] = temp_fun(self.__data[i][j])

    @property
    def size(self) -> int:
        return self.rows * self.columns

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @shape.setter
    def shape(self, new_shape: tuple[int, int]) -> None:
        if isinstance(new_shape, tuple):
            self.rows, self.columns = new_shape
        else:
            raise ValueError("`dl.Matrix.shape` property must be a tuple of integers")

    @property
    def dtype(self) -> type:
        return self.__dtype

    @dtype.setter
    def dtype(self, new_value: type) -> None:
        if new_value in (int, float, str, bool):
            self.__dtype = new_value
        else:
            raise ValueError("`dl.Matrix.dtype` property must be an type object")

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, new_value: int) -> None:
        if isinstance(new_value, int):
            self.__columns = new_value
            self._adjust_dimensions()
        else:
            raise ValueError("`dl.Matrix.columns` property must be an integer")

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, new_value: int) -> None:
        if isinstance(new_value, int):
            self.__rows = new_value
            self._adjust_dimensions()
        else:
            raise ValueError("`dl.Matrix.rows` property must be an integer")

    def change_dtype(self, new_dtype: type) -> str:
        self.dtype = new_dtype
        self._change_data_type(new_dtype)

    def set_precision(self, new_precision: int) -> None:
        if isinstance(new_precision, int):
            self.__precision = new_precision
        else:
            raise ValueError("Number precision must be an integer")

    def reshape(self, new_shape: tuple[int, int]) -> None:
        if isinstance(new_shape, tuple):
            self.rows, self.columns = new_shape
            self._adjust_dimensions()
        else:
            raise ValueError("Matrix shape must be an tuple of integers")

    def to_list(self) -> list[list[Union[int, float, str, bool]]]:
        return self.__data

    def to_tuple(self) -> list[list[Union[int, float, str, bool]]]:
        buffer = [tuple() for _ in range(self.rows)]

        for i, row in enumerate(self.__data):
            buffer[i] = tuple(row)

        return tuple(buffer)

    def copy(self) -> list[list[Union[int, float, str, bool]]]:
        return self.__data
