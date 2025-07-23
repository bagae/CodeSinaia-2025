def roman_converter(num):
    if(num is None):
        return None
    if isinstance(num, str):
        return None
    if num > 3999 or num < 1:
        return None
    if( isinstance(num, float)):
        return None
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100,'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""
    for value, numeral in roman_numerals:
        while num >= value:
            result += numeral
            num -= value
    return result