def number_to_words(num):
    if(num is None):
        return None
    if isinstance(num, str):
        return None
    if num > 3999 or num < 1:
        return None
    if( isinstance(num, float)):
        return None
    number_to_words_english_pair=[
        (1000, 'thousand'), (100, 'hundred'), (10, 'ten'),
        (9, 'nine'), (8, 'eight'), (7, 'seven'), (6, 'six'),
        (5, 'five'), (4, 'four'), (3, 'three'), (2, 'two'), (1, 'one')
    ]
    special_cases=[
        (90, 'ninety'), (80, 'eighty'),
        (70, 'seventy'), (60, 'sixty'), (50, 'fifty'), (40, 'forty'),
        (30, 'thirty'), (20, 'twenty'), (19, 'nineteen'), (18, 'eighteen'),
        (17, 'seventeen'), (16, 'sixteen'), (15, 'fifteen'), (14, 'fourteen'),
        (13, 'thirteen'), (12, 'twelve'), (11, 'eleven'), 
    ]
    words = []

    # Thousands
    if num >= 1000:
        thousands = num // 1000
        words.append(number_to_words(thousands))
        words.append('thousand')
        num = num % 1000

    # Hundreds
    if(num>=100 and num<=199):
        words.append('one hundred')
        num-=100
    if num >= 100:
        hundreds = num // 100
        words.append(number_to_words(hundreds))
        words.append('hundred')
        num = num % 100

    # Special cases for 11-19 and tens
    for val, word in special_cases:
        if num >= val:
            words.append(word)
            num -= val
            break

    # Tens and units
    for val, word in number_to_words_english_pair:
        if num >= val:
            words.append(word)
            num -= val

    return ' '.join(words).strip()
   

