def luhns_algorithm(card_number):
    total = 0
    num_digits = len(card_number)
    parity = num_digits % 2

    for i, digit in enumerate(card_number):
        digit = int(digit)
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0


def identify_card_issuer(card_number):
    length = len(card_number)
    first_digit = int(card_number[0])
    first_two_digits = int(card_number[:2])

    if length == 15 and (first_two_digits == 34 or first_two_digits == 37):
        return "AMEX"
    elif length == 16 and 51 <= first_two_digits <= 55:
        return "MASTERCARD"
    elif (length == 13 or length == 16) and first_digit == 4:
        return "VISA"
    else:
        return "INVALID"


number = input("Number: ")

if luhns_algorithm(number):
    card_issuer = identify_card_issuer(number)
else:
    card_issuer = "INVALID"
print(card_issuer)
