def main():
    card_number = input_number_card()
    # card_number = '4111-1111-4555-1142'
    trans_table = {
        '-': '', 
        ' ': '',
    }
    card_translation = str.maketrans(trans_table)
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


def input_number_card():
    '''
    Prompts the user for a 16-digit card number.
    If the number entered contains only digits and is 16 in length it splits the number into 4-digit chunks and returns it formatted with dashes.
    But if the number already has spaces or dashes, it simply returns it
    '''
    user_card = input('Enter card number of 16 digits: ').strip()

    if user_card.isdigit():
        parts = [user_card[index:index + 4] for index in range(0, len(user_card), 4)]
        # print(parts)
    
        user_card = '-'.join(parts)
    
    return user_card


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)


    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    
    return total % 10 == 0
    

if __name__ == '__main__':
    main()