'''
def my_add(n):
    my_list = []
    for i in range(1,n+1):
        x = i
        my_list.append(x)
    total = sum(my_list)
    print(total)

my_add(12)
'''

'''
def my_add3(start, end, step):
    my_list = []
    for i in range(1,end+1):
        x = start + (i-1)*step
        my_list.append(x)
    print(sum(my_list))

my_add3(8,3,7)
'''

'''
def my_add(n):
    my_list = []
    for i in range(1,n+1):
        x = i**2 - 1
        my_list.append(x)
    print(sum(my_list))

my_add(7)
'''

'''fig 1: 10, fig 2: 16, fig 3: 22
def my_dots(n):
    start = 10
    step = (n-1)*6
    total_dots = start + step
    print(f"The total number of dots is {total_dots}")
my_dots(30)'''

'''
def my_fraction_sum(n):
    my_list = []
    for i in range(1,n+1):
        x = 1/(i*(i+1))
        my_list.append(x)
    total = sum(my_list)
    print(total)

my_fraction_sum(50)
'''

'''-------Morse Code Generator-------'''
'''
def morse_code(n):
    total_code = ""
    for i, char in enumerate(n):
        if n[i].upper() == "A":
            code1 = ".-"
            total_code += code1
        elif n[i].upper() == "B":
            code2 = "-..."
            total_code += code2
        elif n[i].upper() == "C":
            code3 = "-.-."
            total_code += code3
        elif n[i].upper() == "D":
            code4 = "-.."
            total_code += code4
        elif n[i].upper() == "E":
            code5 = "."
            total_code += code5
        elif n[i].upper() == "F":
            code6 = "..-."
            total_code += code6
        elif n[i].upper() == "G":
            code7 = "--."
            total_code += code7
        elif n[i].upper() == "H":
            code8 = "...."
            total_code += code8
        elif n[i].upper() == "I":
            code9 = ".."
            total_code += code9
        elif n[i].upper() == "J":
            code10 = ".---"
            total_code += code10
        elif n[i].upper() == "K":
            code11 = "-.-"
            total_code += code11
        elif n[i].upper() == "L":
            code12 = ".-.."
            total_code += code12
        elif n[i].upper() == "M":
            code13 = "--"
            total_code += code13
        elif n[i].upper() == "N":
            code14 = "-."
            total_code += code14
        elif n[i].upper() == "O":
            code15 = "---"
            total_code += code15
        elif n[i].upper() == "P":
            code16 = ".--."
            total_code += code16
        elif n[i].upper() == "Q":
            code17 = "--.-"
            total_code += code17
        elif n[i].upper() == "R":
            code18 = ".-."
            total_code += code18
        elif n[i].upper() == "S":
            code19 = "..."
            total_code += code19
        elif n[i].upper() == "T":
            code20 = "-"
            total_code += code20
        elif n[i].upper() == "U":
            code21 = "..-"
            total_code += code21
        elif n[i].upper() == "V":
            code22 = "...-"
            total_code += code22
        elif n[i].upper() == "W":
            code23 = ".--"
            total_code += code23
        elif n[i].upper() == "X":
            code24 = "-..-"
            total_code += code24
        elif n[i].upper() == "Y":
            code25 = "-.--"
            total_code += code25
        elif n[i].upper() == "Z":
            code26 = "--.."
            total_code += code26
        elif n[i] == "0":
            code27 = "-----"
            total_code += code27
        elif n[i] == "1":
            code28 = ".----"
            total_code += code28
        elif n[i] == "2":
            code29 = "..---"
            total_code += code29
        elif n[i] == "3":
            code30 = "...--"
            total_code += code30
        elif n[i] == "4":
            code31 = "....-"
            total_code += code31
        elif n[i] == "5":
            code32 = "....."
            total_code += code32
        elif n[i] == "6":
            code33 = "-...."
            total_code += code33
        elif n[i] == "7":
            code34 = "--..."
            total_code += code34
        elif n[i] == "8":
            code35 = "---.."
            total_code += code35
        elif n[i] == "9":
            code36 = "----."
            total_code += code36
        elif n[i] == " ":
            total_code += " "
    print(total_code)

x = input("Please type in a sentence or word: ")
morse_code(x)
'''

'''
Morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'}


def morse(n):
    n = n.upper()
    code = ""
    for char in n:
        if char in Morse_code_dict:
            code += Morse_code_dict[char]
        else:
            code += "?"
    print(code)

x = input("Give a word or phrase: ")
morse(x)
'''