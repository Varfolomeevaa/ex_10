import re


class RomanNumber:
    '''
    class of roman numbers
    '''
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_normal = '^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
    romans = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    def __init__(self, ptr):
        '''
        method for initialization
        :param ptr: Roman number
        '''
        if RomanNumber.is_roman(ptr):
            self.rom_value = ptr
            self.new_value = ptr
        else:
            print('Ошибка!')
            self.rom_value = None

    @staticmethod
    def is_roman(value):
        '''
        method for defining roman number or not
        :param value: roman number
        :return: True of False
        '''
        if re.match(RomanNumber.roman_normal, value):
            return True
        return False

    def decimal_number(self):
        '''
        method for converting Roman numerals to Arabic
        :return: arabic number
        '''
        dec_number = 0
        new = ''
        number = self.rom_value
        if number is not None:
            for i in RomanNumber.romans:
                if i in number:
                    dec_number += RomanNumber.romans[i] * number.count(i)
                    number = number.replace(i, 'A')
            number = number.split('A')
            for j in range(len(number)):
                if number[j] != '':
                    new += number[j]
            number = new
            for i in range(len(number)):
                dec_number += RomanNumber.roman_numbers[number[i]]
        return dec_number

    def __str__(self):
        '''
        method for string representation
        :return: roman number
        '''
        if self.rom_value is None:
            return 'None'
        return self.rom_value

    def __repr__(self):
        '''
        method for interactive presentation
        :return: roman number
        '''
        return str(self.rom_value)
