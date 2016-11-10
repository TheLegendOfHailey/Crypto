msg = 'QCRSQFOTH ZOP FCQYG!'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'

for key in range(len(ALPHABET)):
    result = ''
    for symbol in msg:
        if symbol in ALPHABET:
            num = ALPHABET.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(ALPHABET)

            result = result + ALPHABET[num]

        else:
              result = result + symbol

    print('your magic number is.... %s! %s' % (key,  result))
