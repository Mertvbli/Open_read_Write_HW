import os
from pprint import pprint

path = os.path.join(os.getcwd())
rez = os.listdir(path)


def result_function(result):
    data = {}
    for i in result:
        if i.endswith(".txt"):
            with open(i, encoding='utf-8') as f:
                stroki = len(f.readlines())
            with open(i, encoding='utf-8') as f:
                data[i] = [stroki, f.read().strip()]
    data = sorted(data.items(), key=lambda x: x[1])
    for ddnn in data:
        with open("4.txt", "a", encoding='utf-8') as document:
            document.write(f"{ddnn[0]}\n")
            document.write(f"{ddnn[1][0]}\n")
            document.write(str(f"{ddnn[1][1]}\n"))
    print("Обработка файлов завершена")


result_function(rez)
