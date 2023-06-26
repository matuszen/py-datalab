from utils import *


class Vector:
    def __init__(
        self,
        size: int,
        dtype: type = int,
    ) -> None:
        self.__size = size
        self.__dtype = dtype

        self.__precision = 4

        self._initialize_data()

    def __str__(self) -> str:
        buffer = [" " for _ in range(self.size)]

        for i, value in enumerate(self.__data):
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

            buffer[i] = formatted_value

        max_element_lengths = max(len(str(item)) for item in buffer)

        output = ""

        for row in buffer:
            output += "| "
            for value, max_length in zip(row, max_element_lengths):
                output += f"{value}{' ' * (max_length - len(value) + 1)}"

            output += "|\n"

        return output

    def __setitem__(self, index: int, value: object) -> None:
        if self.dtype == int:
            self.__data[index] = int(value)

        elif self.dtype == float:
            self.__data[index] = float(value)

        elif self.dtype == str:
            self.__data[index] = str(value)

        elif self.dtype == bool:
            self.__data[index] = bool(value)

    def __getitem__(self, index: int) -> object:
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
            init_item for _ in range(self.size)
        ]

    def _adjust_size(self) -> None:
        buffer = self.__data.copy()

        init_item = self._empty_element()

        self.__data = [
            init_item for _ in range(self.size)
        ]

        for i in range(self.size):
            try:
                self.__data[i] = buffer[i]
            except:
                continue

    def _change_data_type(self, new_dtype: type) -> None:
        temp_fun = lambda x: new_dtype(x)

        for i in range(self.size):
            self.__data[i] = temp_fun(self.__data[i])

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, new_size: int) -> None:
        if isinstance(new_size, int):
            self.__size = new_size
            self._adjust_size()
        else:
            raise ValueError("Vector size must be an integer")

    @property
    def dtype(self) -> type:
        return self.__dtype

    @dtype.setter
    def dtype(self, new_value: type) -> None:
        if new_value in (int, float, str, bool):
            self.__dtype = new_value
        else:
            raise ValueError("`dl.Vector.dtype` property must be an type object")

    def change_dtype(self, new_dtype: type) -> str:
        self.dtype = new_dtype
        self._change_data_type(new_dtype)

    def set_precision(self, new_precision: int) -> None:
        if isinstance(new_precision, int):
            self.__precision = new_precision
        else:
            raise ValueError("Number precision must be an integer")

    def to_list(self) -> list[list[Union[int, float, str, bool]]]:
        return self.__data

    def to_tuple(self) -> list[list[Union[int, float, str, bool]]]:
        buffer = [tuple() for _ in range(self.rows)]

        for i, row in enumerate(self.__data):
            buffer[i] = tuple(row)

        return tuple(buffer)

    def copy(self) -> list[list[Union[int, float, str, bool]]]:
        return self.__data
