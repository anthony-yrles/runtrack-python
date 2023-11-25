def jules_cesar(message: str, decalage: int):
    message = list(message.upper())
    encrypted_message = []

    for i in range(len(message)):
        char_code = ord(message[i])

        if char_code < 65 or char_code > 90:
            encrypted_message.append(message[i])
        elif char_code + decalage > 90:
            reste = 91 - char_code
            plus = decalage - reste
            encrypted_message.append(chr(65 + plus))
        else:
            encrypted_message.append(chr(char_code + decalage))

    result = ''.join(encrypted_message)
    result_lower = result.lower()
    print(result_lower)

jules_cesar("Je suis Jules Cesar, empereur de tous les romains", 5)



