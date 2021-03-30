

def read_txt():
    F_txt = open("source.txt","r") # открывает и читает файл, об этом говорит флажок "r"
    for line in F_txt: # цыкл, который переберает каждую строчку в файле
        divided_line = line.split() # split() разделяет слова
        print(*divided_line) # выводит в весь файл
    F_txt.close()


def write_txt():
    column_one = input("Столбец 1")
    column_two = input("Столбец 2")
    column_three = input("Столбец 3")
    column_four = input("Столбец 4")
    F_txt = open("source_1.txt","a") # флажок а изменяет файл и добавляет запись, в отичии от флажка w, который перезаписывает файл
    F_txt.write("\n"+column_one+" "+column_two+" "+column_three+" "+column_four) # записывает весь импот с учетом пробелов и абзацев
    F_txt.close()

def del_txt():
    del_line = int(input("Номер строки:")) # номер строки, которую надо удалить
    with open("source.txt","r") as textobj: # читает файл и превращает его в "объект" "textobj"
        global list
        list = list(textobj) # список слов из одной строчки
        print(list)
    del list[del_line - 1] # удаляет строчку с учетом индекса массива, который начинается с 0
    with open("source.txt","w") as textobj: # перезапись файла
        for n in list:
            textobj.write(n) # записывает все строчки за исключение удаленной

def sort_txt():
    A = []
    count = 0
    nuber_of_line = 0
    nuber_of_column = int(input("Номер столбца"))-1
    F_txt = open("source.txt","r")
    for line in F_txt: # цыкл который выполняет то же самое что выполняет метод чтения, но он каждую строчку добавляет в массив А
        nuber_of_line += 1 # определяет сколько сейчас строчек в файле
        divided_line = line.split()
        A.append(divided_line) # то самое добавление в массив
    for i in range(nuber_of_line-1): # СОРТИРОВКА ПУЗЫРЬКОМ ТРУДНО ОБЪЯСНИТЬ ПРОСТО НАДО ВНИМАТЕЛЬНО ПОСМОТРЕТЬ НА НЕГО!!!!!
        for j in range(nuber_of_line-i-1):
            if A[j][nuber_of_column][0]> A[j+1][nuber_of_column][0]:
                A[j], A[j+1] = A[j+1], A[j]
    # после сортировки пузырьком мы получаем массив-матрицу, если у него 4 строки то он выглядит вот так:
    # A = [[[столбец 1][столбец 2][столбец 3][столбец 4]]
    #      [[столбец 1][столбец 2][столбец 3][столбец 4]]
    #      [[столбец 1][столбец 2][столбец 3][столбец 4]]
    #      [[столбец 1][столбец 2][столбец 3][столбец 4]]]
    F_txt_w = open("source.txt","w") # тут начинается перезапись файла
    for i in range(nuber_of_line):
        for j in range(4):
            count += 1

            a = A[i][j]
            #суть этого цикла в том, что он записывает каждое слово, через пробел, в файл и подсчитует с помощю count количество слов, чтобы после 4 слова делать абзац
            if count % 4:
                F_txt_w.write(str(a)+ " ")
            else:
                F_txt_w.write(str(a)+ "\n")



def question():# первый метод, он выбирает что сделать с файлом и какой метод запустьть
    question = int(input("Что сделать с файлом?\n 1:Посмотреть\n 2:Добавить строку\n 3:Удалить строку\n 4:Сортировка\n 5:Стоп\n"))
    if question == 1:
        read_txt()
    elif question == 2:
        write_txt()
    elif question == 3:
        del_txt()
    elif question == 4:
        sort_txt()
    elif question == 5:
        pass

###################################

question() # запускает первый метод










