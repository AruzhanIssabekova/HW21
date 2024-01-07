class Roman:
    def __init__(self, value):
        self.roman = value
        self.value = self.to_arabic()
    def to_arabic(self):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for numeral in reversed(self.roman):
            value = roman_numerals[numeral]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result
    def __add__(self, other):
        return Roman(self.to_roman_string(self.value + other.value))
    def __sub__(self, other):
        return Roman(self.to_roman_string(self.value - other.value))
    def __mul__(self, other):
        return Roman(self.to_roman_string(self.value * other.value))
    def __truediv__(self, other):
        return Roman(self.to_roman_string(self.value // other.value))

    @staticmethod
    def from_arabic(arabic_num):
        if not isinstance(arabic_num, int):
            raise TypeError("Арабское число должно быть представлено целым числом")
        return Roman(Roman.to_roman_string(arabic_num))
    @staticmethod
    def to_roman_string(num):
        roman_numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""
        for arabic, roman in roman_numerals:
            count, num = divmod(num, arabic)
            result += roman * count
        return result

roman_str1 = input("Введите первое римское число: ")
roman_str2 = input("Введите второе римское число: ")

num1 = Roman(roman_str1)
num2 = Roman(roman_str2)

result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2

print(f"Сложение: {result_add.roman}")
print(f"Вычитание: {result_sub.roman}")
print(f"Умножение: {result_mul.roman}")
print(f"Деление: {result_div.roman}")