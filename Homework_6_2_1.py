# TODO 6_2 Код Морзе для представления цифр и букв используя тире и точки. Напишите функцию для кодирования текстового
# сообщения в соответствии с кодом Морзе. Словари в помощь

morze_dict = { "A":".-",    "B":"-...",  "C":"-.-.",
               "D":"-..",   "E":".",     "F":"..-.",
               "G":"--.",   "H":"....",  "I":"..",
               "J":".---",  "K":"-.-",   "L":".-..",
               "M":"--",    "N":"-.",    "O":"---",
               "P":".--.",  "Q":"--.-",  "R":".-.",
               "S":"...",   "T":"-",     "U":"..-",
               "V":"...-",  "W":".--",   "X":"-..-",
               "Y":"-.--",  "Z":"--..",  "0":"-----",
               "1":".----", "2":"..---", "3":"...--",
               "4":"....-", "5":".....", "6":"-....",
               "7":"--...", "8":"---..", "9":"----."}


print('Vvedite text:')
text = str(input())
print(   text.split() for i in range (len(text.split() )   )  )

def morze(data):
    spisok = []
    for letter in data:
        spisok.append((data[letter]))
    return " ".join(spisok)

morze(text)
#for i in range(1,len(spisok)+1):
#    if i % 5 != 0 or i==0:
#        print(spisok[i-1], end=" ")
#   else:
#        print(spisok[i-1], end="\n ")

