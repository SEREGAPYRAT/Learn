import sys
import os 
from package.modules.fun import Func 

class Main:
    

    def hello (self) -> None:
        while True:
            x=input("1-Создать файл.\n2-Прочитать файл.\n3-Обновить файл.\n4-Удалить файл.\n5-Выход из программы\n")
            if x == "1":
                fif.create()
            elif x == "2":
                fif.read()
            elif x == "3":
                fif.update()
            elif x == "4":
                fif.delete()
            elif x == '5':
                sys.exit()
            else:
                print('Неверно введено значение')

fif=Func(os.getcwd())
a=Main()
a.hello()
