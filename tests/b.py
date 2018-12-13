import sys


char = sys.stdin.read(1)#le um char
line = sys.stdin.readline()##le uma linha inteira incluindo \n no final

print(line[-1]=="\n")#retorna true ou false aleatoriamente? (aparentemente depende se é input do console ou de arquivo)

print(line ,"%c %d %.5f  " %(char, 2, 1/3), end="")#printa a linha sem o \n


print(line.strip())
line = line.strip()
print(line.split(" "))
print(1<<10)

class struct:
    x=1<<5  #public
    __y=1<<4  #private
    def gety(self):
        return self.__y

obj=struct() 
print(obj.x, obj.gety())
