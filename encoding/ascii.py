from random import randint

# chr( number_to_convert )      -> ascii encoded character
# ord( character_to_convert )   -> ascii decoded decimal


# char = "v"
# number = ord(char)
# print(char, number)

# number = 84
# char = chr(number)
# print(number, char)


def decode(numbers):
    characters = []
    for number in numbers:
        letter = chr(number)
        characters.append(letter)
    return "".join(characters)


def encode(message):
    characters = []
    for letter in message:
        num = ord(letter)
        characters.append(num)
    return characters


def decrypt(cipher, offset):
    # print("Decrypting:", cipher)
    offset_numbers = []
    for number in encode(cipher):
        if not number == 32:
            number += offset
        if number > 122:
            number -= 26
        offset_numbers.append(number)
    # print("Offset:    ", offset_numbers)
    decoded = decode(offset_numbers)
    print("Decode:", offset, " ", decoded)
    return decoded


def encrypt(message):
    random_offset = randint(1, 25)
    encoded_message = encode(message)
    encrypted_numbers = []
    for number in encoded_message:
        if not number == 32:
            number += random_offset
        if number > 122:
            number -= 26
        encrypted_numbers.append(number)
    return decode(encrypted_numbers), random_offset


def brute_force(cipher):
    for offset in range(26):
        decrypt(cipher, offset)


brute_force("gylls wblcmngum uhx u bujjs hyq syul")

