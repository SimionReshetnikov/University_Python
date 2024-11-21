import re

def process_command(command, array):
    
    index = re.match(r"Получить элемент по (\d+) индексу", command)
    sliceMatch = re.match(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
    reverseIndex = re.match(r"Получить (\d+)-ый элемент с конца массива", command)

    if index:
        index = int(index.group(1))
        
        if 0 <= index < len(array):
            return array[index]
        else:
            return "Индекс выходит за пределы массива"

    elif sliceMatch:
        
        start = int(sliceMatch.group(1))
        end = int(sliceMatch.group(2))
        step = int(sliceMatch.group(3))
        
        if 0 <= start < len(array) and 0 <= end <= len(array):
            return array[start:end:step]
        else:
            return "Начальный или конечный индекс выходит за пределы массива"

    elif reverseIndex:
        reverse_index = int(reverseIndex.group(1))
        
        if 0 < reverse_index <= len(array):
            return array[-reverse_index]
        else:
            return "Индекс с конца выходит за пределы массива"

    else:
        return "Команда не соответствует ожидаемому формату"


someArray = [7, 3, 5, 4, 0, 6, 9, 2]
print(process_command("Получить элемент по 4 индексу", someArray))  
print(process_command("Получить элементы с 3 по 6 с шагом 1", someArray))  
print(process_command("Получить 1-ый элемент с конца массива", someArray)) 
print(process_command("Получить элемент по 12 индексу", someArray))
