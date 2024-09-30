
import os 

class Func:
    def __init__(self,place) -> None:
        self.place = place

    def __add__ (self,other):
        return(self.place+other)

    def create(self):
        name=input('Введите название файла с его расширением \n Пример: file.txt \n')
        with open(self.place+'/'+name,'w') as f:
            f.write(input('Введите содержимаое файла'))
        

    def read(self):
        name=input('Введите название файла который хотите прочитать\n')
        if name in os.listdir():
            with open(self.place+'/'+name,'r') as f:
                print(f.read())
        else:
            print('файла с таким именем не существует')

    def update(self):
        name=input('Введите название файла который хотите изменить\n')
        if name in self.place():
            os.remove(name)
            with open(self.place+'/'+name,'w') as f:
                f.write(input('Введите содержимаое файла'))
        else:
            print('файла с таким именем не существует')

    def delete(self):
        name=input('Введите название файла который хотите изменить\n')
        if name in self.place():
            os.remove(name)
            print('Удаление успешно завершено')
        else:
            print('файла с таким именем не существует')
