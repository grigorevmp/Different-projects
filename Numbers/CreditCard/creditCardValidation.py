# Берет номер кредитной карты от производителя (Visa, MasterCard, American Express, Discover) и
# проверяет на правильность номер (разберитесь, как кредитные карты используют контрольную сумму)

# Validate credit card number
# luhn algorithm

import re


def luhn(code):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(code)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0


def getType(num):
    """
    num -> result
    """

    if re.match(r"^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$", str(num)):
        return "Solo Card"
    if re.match(r"^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|("
                r"4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110["
                r"0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$", str(num)):
        return "Switch Card:"
    if re.match(r"^(62[0-9]{14,17})$", str(num)):
        return "Union Pay Card"
    if re.match(r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$", str(num)):
        return "Visa Master Card"
    if re.match(r"^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$", str(num)):
        return "Maestro Card"
    if re.match(r"^3[47][0-9]{13}$", str(num)):
        return "American Express"
    if re.match(r"^(6541|6556)[0-9]{12}$", str(num)):
        return "BCGlobal"
    if re.match(r"^(?:220[0-4])\d+$", str(num)):
        return "MIR"
    if re.match(r"^389[0-9]{11}$", str(num)):
        return "Carte Blanche Card"
    if re.match(r"^63[7-9][0-9]{13}$", str(num)):
        return "Insta Payment Card"
    if re.match(r"^9[0-9]{15}$", str(num)):
        return "KoreanLocalCard"
    if re.match(r"^(6304|6706|6709|6771)[0-9]{12,15}$", str(num)):
        return "Laser Card"
    if re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", str(num)):
        return "Visa"
    if re.match(r"^5[1-5][0-9]{14}$", str(num)):
        return "MasterCard"
    if re.match(r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$", str(num)):
        return "Diners Club"
    if re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", str(num)):
        return "Discover"
    if re.match(r"^(?:2131|1800|35[0-9]{3})[0-9]{11}$", str(num)):
        return "JCB"
    if re.match(r"^(4026|417500|4405|4508|4844|4913|4917)\d+$", str(num)):
        return "Electron"
    if re.match(r"^(636)\d+$", str(num)):
        return "Interpay"
    if re.match(r"^(62|81)\d+$", str(num)):
        return "Cup"
    return "Unknown type"


def inputData():
    """
    <input> -> num
    """
    _num = input("Input number of your credit card: ")
    num = 0

    try:
        num = int(_num)
    except ValueError:
        print("Enter a positive integer.")

    return num


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Credit card --\n")

    shouldContinue = True

    while shouldContinue:

        num = inputData()

        if luhn(num):
            print("\nCard is valid")
        else:
            print("\nCard is NOT valid")

        print(f"Card type: {getType(num)}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
