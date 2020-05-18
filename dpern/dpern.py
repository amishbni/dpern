import logging, sys

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

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
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

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

        position = length = len(number)
        result = ""
        for i in range(length):
            ichar = int(number[i])
            if position == 3:
                if ichar != 0:
                    result += f"{hundreds[ichar]} و "
                position -= 1
            elif position == 2:
                if ichar == 1 and (10 < int(number[-2:]) < 20):
                    result += f"{teens[int(number[-1:])]} و "
                    position -= 1
                elif ichar != 0:
                    result += f"{tens[ichar]} و "
                position -= 1
            elif position == 1:
                if ichar != 0:
                    result += f"{ones[ichar]} و "
                position -= 1

        return result[:-3]

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
    for i in range(length):
        name = names[length-i-1]
        num = thousand_separated[i]
        if int(num) != 0:
            described = describe3(num)
            result += f"{described} {name} و "

    if result.strip()[-2:] == " و":
        result = rreplace(result, " و", "", 1).strip()
    if result.strip()[-2:] == " و":
        result = rreplace(result, " و", "", 1).strip()

    return result
