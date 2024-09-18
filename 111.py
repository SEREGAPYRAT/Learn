
import os 

class func:
    def __init__(self) -> None:
        pass

    def create(self):
        name=input('Введите название файла с его расширением \n Пример: file.txt \n')
        f=open(name,'w')
        f.write(input('Введите содержимаое файла'))
        f.close()

    def read(self):
        name=input('Введите название файла который хотите прочитать\n')
        if name in os.listdir():
            f=open(name,'r')
            print(f.read())
            f.close()
        else:
            print('файла с таким именем не существует')

    def update(self):
        name=input('Введите название файла который хотите изменить\n')
        if name in os.listdir():
            os.remove(name)
            f=open(name,'w')
            f.write(input('Введите содержимаое файла'))
            f.close()
        else:
            print('файла с таким именем не существует')

    def delete(self):
        name=input('Введите название файла который хотите изменить\n')
        if name in os.listdir():
            os.remove(name)
            print('Удаление успешно завершено')
        else:
            print('файла с таким именем не существует')

class main:
    
    def __init__(self) -> None:
        pass

    def hello (self) -> None:
        while True:
            x=input("1-Создать файл.\n2-Прочитать файл.\n3-Обновить файл.\n4-Удалить файл.\n")
            if x == "1":
                fif.create()
            elif x == "2":
                fif.read()
            elif x == "3":
                fif.update()
            elif x == "4":
                fif.delete()
            else:
                print('Ди наху')

fif=func()
a=main()
a.hello()
