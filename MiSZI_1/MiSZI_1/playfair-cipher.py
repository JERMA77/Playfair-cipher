FULL_ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Э', 'Ь', 'Ю', 'Я']        
          
def existOrNot(char, array):
    for i in range(4):
        for j in range(8):
            if char == array[i][j]:
                return True
    return False

def setAlphabet(keyWord):
    filteredKeyWord = keyWord.replace(' ', '')

    alphabet = [0] * 4
    for k in range(4): 
        alphabet[k] = [0] * 8  


    num = 0
    i = 0
    while i < 4:
        j = 0
        while j < 8:
            if num < len(filteredKeyWord):
                if not(existOrNot(filteredKeyWord[num], alphabet)):
                    alphabet[i][j] = filteredKeyWord[num]
                else:
                    if j == 7:
                        i -= 1
                        j -= 1
                    else:
                        j -= 1
                num+=1
            else:
                for k in range(32):
                    if not(existOrNot(FULL_ALPHABET[k], alphabet)):
                        alphabet[i][j] = FULL_ALPHABET[k]
                        break
            j += 1
        i += 1
    return alphabet




def encode(originalStr, alphabet):
    encodeStr = ""
    i = 0
    filteredStr = ""

    # Сохраняем позиции пробелов по оригинальной строке
    space_positions = [pos for pos, ch in enumerate(originalStr) if ch == ' ']

    # Удаляем пробелы для кодирования
    filteredStr = originalStr.replace(' ', '')

    # Добавляем символ, если нечётная длина
    if len(filteredStr) % 2 != 0:
        filteredStr += 'Х'

    while i < len(filteredStr):
        char1 = filteredStr[i]
        char2 = filteredStr[i+1]

        char1pos = char2pos = None

        for r in range(4):
            for c in range(8):
                if alphabet[r][c] == char1:
                    char1pos = (r, c)
                if alphabet[r][c] == char2:
                    char2pos = (r, c)

        if char1pos[0] == char2pos[0]:  # Один ряд
            encodeStr += alphabet[char1pos[0]][(char1pos[1] + 1) % 8]
            encodeStr += alphabet[char2pos[0]][(char2pos[1] + 1) % 8]
        elif char1pos[1] == char2pos[1]:  # Один столбец
            encodeStr += alphabet[(char1pos[0] + 1) % 4][char1pos[1]]
            encodeStr += alphabet[(char2pos[0] + 1) % 4][char2pos[1]]
        else:  # Прямоугольник
            encodeStr += alphabet[char1pos[0]][char2pos[1]]
            encodeStr += alphabet[char2pos[0]][char1pos[1]]

        i += 2

    # Вставляем пробелы в исходные позиции
    for pos in space_positions:
        encodeStr = encodeStr[:pos] + ' ' + encodeStr[pos:]

    return encodeStr


def decode(encodedStr, alphabet):
    decodeStr = ""
    # Сохраняем позиции пробелов
    space_positions = [pos for pos, ch in enumerate(encodedStr) if ch == ' ']

    filteredStr = encodedStr.replace(' ', '')

    i = 0
    while i < len(filteredStr):
        char1 = filteredStr[i]
        char2 = filteredStr[i+1]

        char1pos = char2pos = None

        for r in range(4):
            for c in range(8):
                if alphabet[r][c] == char1:
                    char1pos = (r, c)
                if alphabet[r][c] == char2:
                    char2pos = (r, c)

        if char1pos[0] == char2pos[0]:  # Один ряд
            decodeStr += alphabet[char1pos[0]][(char1pos[1] - 1) % 8]
            decodeStr += alphabet[char2pos[0]][(char2pos[1] - 1) % 8]
        elif char1pos[1] == char2pos[1]:  # Один столбец
            decodeStr += alphabet[(char1pos[0] - 1) % 4][char1pos[1]]
            decodeStr += alphabet[(char2pos[0] - 1) % 4][char2pos[1]]
        else:  # Прямоугольник
            decodeStr += alphabet[char1pos[0]][char2pos[1]]
            decodeStr += alphabet[char2pos[0]][char1pos[1]]

        i += 2

    # Удаляем возможный заполнитель 'Х' в конце
    if decodeStr.endswith('Х'):
        decodeStr = decodeStr[:-1]

    # Вставляем пробелы в исходные позиции
    for pos in space_positions:
        decodeStr = decodeStr[:pos] + ' ' + decodeStr[pos:]

    return decodeStr




currentAlphabet = setAlphabet((input("Напишите ключ-слово: ")).upper()) #Задаём алфавит

print("\nАлфавит, по которому кодируем текст:")
print(currentAlphabet[0])
print(currentAlphabet[1])
print(currentAlphabet[2])
print(currentAlphabet[3])

originalStr = input("\nНапишите текст, который нужно закодировать шифром Плейфера: ").upper()
print("\nИсходный текст: ", originalStr)

result = encode(originalStr, currentAlphabet)
print("\nЗашифрованный текст: " + result)
print("\nРасшифрованный текст: " + decode(result, currentAlphabet))