import logging, sys

def fa_to_en(text):
    import re
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    return re.sub(
        "|".join(map(re.escape, mapping.keys())),
        lambda m: mapping[m.group()],
        str(text))

def describe(number):
    try:
        int(number)
        number = str(number)
    except Exception:
        warn_message = ("Cannot convert string to int. "
                        "Make sure to specify a number.")
        logging.warning(warn_message)

    number = fa_to_en(number)

    if len(number) > 102:
        raise ValueError("Number is too large to describe.")

    def describe3(number):
        ones = {1: "یک", 2: "دو", 3: "سه", 4: "چهار", 5: "پنج",
                6: "شش", 7: "هفت", 8: "هشت", 9: "نه"}

        tens = {1: "ده", 2: "بیست", 3: "سی", 4: "چهل", 5: "پنجاه",
                6: "شصت", 7: "هفتاد", 8: "هشتاد", 9: "نود"}

        teens = {1: "یازده", 2: "دوازده", 3: "سیزده", 4: "چهارده", 5: "پانزده",
                6: "شانزده", 7: "هفده", 8: "هجده", 9: "نوزده"}

        hundreds = {1: "صد", 2: "دویست", 3: "سیصد", 4: "چهارصد", 5: "پانصد",
                6: "ششصد", 7: "هفتصد", 8: "هشتصد", 9: "نهصد"}

        length = len(number)
        result = ""
        delimiter = ""
        for i, num in enumerate(number):
            ichar = int(num)
            position = length - i - 1
            if ichar == 0:
                continue
            if position == 2:
                result += f"{delimiter}{hundreds[ichar]}"
            elif position == 1:
                if ichar == 1 and (10 < int(number[-2:]) < 20):
                    result += f"{delimiter}{teens[int(number[-1:])]}"
                    break
                else:
                    result += f"{delimiter}{tens[ichar]}"
            elif position == 0:
                result += f"{delimiter}{ones[ichar]}"
            delimiter = " و "

        return result

    names = ["", "هزار", "میلیون", "میلیارد", "بیلیون", "بیلیارد", "تریلیون",
            "تریلیارد", "کوآدریلیون", "کادریلیارد", "کوینتیلیون", "کوانتینیارد",
            "سکستیلیون", "سکستیلیارد", "سپتیلیون", "سپتیلیارد", "اکتیلیون",
            "اکتیلیارد", "نانیلیون", "نانیلیارد", "دسیلیون", "دسیلیارد",
            "آندسیلیون", "آندسیلیارد", "دودسیلیون", "دودسیلیارد", "تریدسیلیون",
            "تریدسیلیارد", "کوادردسیلیون", "کوادردسیلیارد", "کویندسیلیون",
            "کویندسیلیارد", "سیدسیلیون", "سیدسیلیارد"]

    thousand_separated = f'{int(number):,}'.split(",")
    length = len(thousand_separated)
    result = ""
    delimiter = ""
    for i, num in enumerate(thousand_separated):
        if int(num) != 0:
            result += f"{delimiter}{describe3(num)}{' ' if i != length-1 else ''}{names[length-i-1]}"
            delimiter = " و "

    return result
