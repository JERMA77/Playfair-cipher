FULL_ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Э', 'Ь', 'Ю', 'Я']        
          
def existOrNot(char, array):
    for i in range(4):
        for j in range(8):
            if char == array[i][j]:
                return True
    return False

def setAlphabet(keyWord):
    # Убираем пробелы и делаем все буквы в верхнем регистре
    filteredKeyWord = keyWord.replace(' ', '').upper()

    # Создаём пустую таблицу 4x8
    alphabet = [ [None] * 8 for _ in range(4)]

    used_chars = set()  # Множество для отслеживания использованных символов
    num = 0
    i = 0
    j = 0

    # Заполняем таблицу сначала уникальными символами из ключа
    while num < len(filteredKeyWord):
        char = filteredKeyWord[num]
        if char not in used_chars:
            alphabet[i][j] = char
            used_chars.add(char)
            j += 1
            if j == 8:  # Переход к следующему ряду
                j = 0
                i += 1
        num += 1

    # Заполняем оставшиеся ячейки оставшимися буквами алфавита
    for char in FULL_ALPHABET:
        if char not in used_chars:
            alphabet[i][j] = char
            used_chars.add(char)
            j += 1
            if j == 8:  # Переход к следующему ряду
                j = 0
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