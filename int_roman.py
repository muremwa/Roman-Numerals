# Python class to convert an integer to a roman numeral.
from functools import lru_cache


class IntRoman:
    """
    This class is used to convert an integer to it's equivalent roman numeral
    usage:
    1. create new instance of the class
        >>> ir = IntRoman()
    2. use the to_roman method to convert
        >>> ir.to_roman(4)
        'IV'
    3. use the to_roman_list method to convert a list of integers
        >>> ir.to_roman_list([4, 63, 963, 623])
        ['IV', 'LXIII',  'CMLXIII', 'DCXXIII']

    currently supports up to 3999
    """
    __romans = (('I', 'X', 'C', 'M'), ('V', 'L', 'D'))

    @lru_cache()
    def __one_to_three(self, number: int, place_value: int)-> str:
        """
        takes a number between 1 and 3 and returns a roman equivalent depending on place value
        """
        place_value -= 1
        value_ = self.__romans[0][place_value]
        return value_*number

    @lru_cache()
    def __mid_six(self, number: int, place_value: int) -> str:
        """
        takes a number between 4 and 8 and returns a roman equivalent depending on place value
        """
        place_value -= 1
        value_ = self.__romans[1][place_value]
        inc = self.__romans[0][place_value]

        if number == 4:
            return inc + value_

        if number == 5:
            return value_

        return value_ + (inc * (number - 5))

    @lru_cache()
    def __nine(self, place_value: int) -> str:
        """
        returns a roman equivalent of 9 depending on place value
        """
        place_value -= 1
        return self.__romans[0][place_value] + self.__romans[0][place_value+1]

    @lru_cache(maxsize=3999)
    def __resolute(self, integer: int) -> str:
        """
        splits an number up and passes it to the right method and receives its roman equivalent
        """
        integer = list(str(integer))
        integer.reverse()
        res = []
        groups = [[i for i in range(1, 4)], [i for i in range(4, 9)], [9]]

        for k, s in enumerate(integer, 1):
            s = int(s)

            if s in groups[0]:
                res.append(self.__one_to_three(s, k))

            elif s in groups[1]:
                res.append(self.__mid_six(s, k))

            elif s in groups[-1]:
                res.append(self.__nine(k))

        res.reverse()
        return ''.join(res)

    def to_roman(self, integer: int) -> str:
        """
        converts an integer to roman numeral
        :param integer: an integer
        :return: roman numeral as a string

        :raises ValueError if number is above 3999
        :raises TypeError if it is not an integer
        """
        if type(integer) != int:
            raise TypeError('Only converts integers')

        if integer > 3999:
            raise ValueError('Currently only supports values up to 3,999')

        if integer == 0:
            raise ValueError('zero has no roman numeral equivalent')

        return self.__resolute(integer)

    def to_roman_list(self, list_int: list) -> list:
        """
        takes in a list of integers and returns a list of their respective roman numbers in the same index as the number
        the functions raises an error even if one element in the list is not an integer
        """
        if type(list_int) not in [list, tuple, set]:
            raise TypeError('to_roman_list only accepts lists, tuples or sets')

        list_int_type = type(list_int)

        if list_int_type == set:
            print('The order of your results may differ from input. Read about sets in python')

        list_int = [self.to_roman(num) for num in list_int]

        return list_int_type(list_int)

    def __repr__(self):
        return "<IntRoman Converter>"
