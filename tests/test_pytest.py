from random import choice


def test_first_try():
    print('Hello World!')


# Тут я с каким-нибудь абсурдом решил поиграться. Изначально, хотел тест замедлить, чтобы посмотреть, что будет
def get_letter():
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"№;%:?*() '
    alphabet_list = []
    for _ in string:
        alphabet_list.append(_)
    return choice(alphabet_list)


def test_first_try2():
    for char in 'Hello World!':
        random_char = get_letter()
        while char != random_char:
            random_char = get_letter()
        else:
            print(char, end='')


def test_greeting():
    greeting = 'Hello World!'
    assert greeting == 'Hello World!!!', 'строки не совпадают'


def test_assert_positive_case():
    assert (five := '5') in '12345', f'{five} не находится в строке'


def test_assert_negative_case():
    assert (five := '5') in '1234', f'{five} не находится в строке'
