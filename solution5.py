import re


class RomanNumber:
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_numbers_rev = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    roman_normal = '^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
    romans = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    romans_rev = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

    def __init__(self, ptr):
        if RomanNumber.is_roman(ptr):
            self.rom_value = ptr
            self.int_value = RomanNumber.decimal_number(self)
        else:
            if RomanNumber.is_int(ptr):
                self.int_value = ptr
                self.rom_value = RomanNumber.roman_number(self)
            else:
                print('Ошибка!')
                self.int_value = None
                self.rom_value = None

    @staticmethod
    def is_roman(value):
        if isinstance(value, int) or isinstance(value, float):
            return False
        elif re.match(RomanNumber.roman_normal, value):
            return True
        return False

    def decimal_number(self):
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

    @staticmethod
    def is_int(value):
        return isinstance(value, int) and 0 < value <= 3999

    def roman_number(self):
        num = self.int_value
        if 100 <= num <= 999:
            num_4 = 0
            num_3 = num // 100 * 100
            num_2 = num // 10 % 10 * 10
            num_1 = num % 10
        elif 1000 <= num <= 3999:
            num_4 = num // 1000 * 1000
            num_3 = num // 100 % 10 * 100
            num_2 = num // 10 % 10 * 10
            num_1 = num % 10
        else:
            num_4 = 0
            num_3 = 0
            num_2 = num // 10 * 10
            num_1 = num % 10
        number = [num_4, num_3, num_2, num_1]
        new_num = ''
        for i in number:
            ost = i
            if i in RomanNumber.romans_rev:
                new_num += RomanNumber.romans_rev[i]
            else:
                for j in RomanNumber.roman_numbers_rev:
                    if ost // j != 0:
                        new_num += RomanNumber.roman_numbers_rev[j] * (ost // j)
                        if ost % j != 0:
                            ost = ost % j
                        else:
                            break

        return new_num

    def __str__(self):
        if self.rom_value is None:
            return 'None'
        return self.rom_value

    def __repr__(self):
        return str(self.rom_value)
