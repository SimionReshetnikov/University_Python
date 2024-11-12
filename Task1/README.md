
![Блок схема](https://github.com/user-attachments/assets/c5fbbdf2-444d-4e08-ba01-07da57152cc0)


Код Python

def getMaxValue(b,c):
 a = int(input("Введите число: "))
 if a < 0:
   return -1
 else:
   return max(a, b, c)

result = getMaxValue(10, 5)
print(result)
