print('Задача №1')

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def output_name(documents): # команда p
    number_doc = input('Введите номер документа: ')
    list_all_values = []
    for document in documents:
        list_all_values += document.values() 
    if number_doc not in list_all_values:
        print('Такого документа нет.') 
        print('Для добавления нового документа, введите команду - a')
    for document in documents:
        if number_doc == document['number']:
            print(document['name'])
            return
  
def output_place(documents): # команда s
    number_doc = input('Введите номер документа: ')
    list_all_values = []
    for shelf, place in directories.items():
        list_all_values += place
        for element in place:
            if element == number_doc:
                print(f'Документ находится на полке {shelf}')
    if number_doc not in list_all_values:
        print('Такого документа нет')    
        print('Для добавления нового документа, введите команду - a')    
        return    

def output_list_docs(documents): # команда l
    for document in documents:
        print(f'{document["type"]}  "{document["number"]}"  "{document["name"]}"')
    return
  
def add_docs(documents): # команда a 
    number_doc  = input('Номер документа: ')
    list_all_values = []
    for document in documents:
        list_all_values += document.values() 
    if number_doc in list_all_values:
        print('Такой документ уже существует')
    else:
        type_doc, name, chelf = input('Введите тип документа: '), input('Имя владельца: '), input('Номер полки, куда положить: ')
        if chelf not in directories:
            print('Такой полки нет')
            print('Для создания полки введите команду - as')
        else:
            document_new = {}
            document_new['type'] = type_doc
            document_new['number'] = number_doc
            document_new['name'] = name
            documents.append(document_new)
            for key, value in directories.items():
                if key == chelf:
                    value = value.extend([number_doc])
            print(f'Документ {document_new["type"]}  "{document_new["number"]}"  "{document_new["name"]}" создан и добавлен на полку {chelf}')
            print('Для просмотра каталога документов введите команду - l')
            return
      
def delete_docs(documents): # команда d
    number_doc = input('Введите номер документа: ')
    list_all_values = []
    for document in documents:
        list_all_values += document.values() 
    if number_doc not in list_all_values:
        print('Такого документа нет')
    else:
        for document in documents:
            if number_doc in document.values():
                del document["type"]
                del document['number']
                del document['name']
                for value in directories.values():  
                    for element in value[0::]:
                        if element in number_doc :
                            value.remove(element)
        for n, document in enumerate(documents):
            if bool(document) == False:
                del documents[n]
        print('Документ удален из каталога')            
    print('Для просмотра каталога документов введите команду - l')            
    return
  
def move_docs(documents): # команда m
    number_doc  = input('Номер документа: ')
    list_all_values = []
    for document in documents:
        list_all_values += document.values() 
    if number_doc not in list_all_values:
        print('Такого документа нет')
    else:
        target_shelf = input('Номер полки, куда положить: ')
        if target_shelf not in directories:
            print('Такой полки нет')
            print('Для создания полки введите команду - as')
        else:
            for shelf, docs in directories.items():
                for element in docs[0::]:
                    if element in number_doc :
                        docs.remove(element)
                        if shelf == target_shelf:
                            print('Документ уже лежит на этой полке')
                        else:
                            print(f'Документ перемещён c полки {shelf} на полку {target_shelf}')
            for key, value in directories.items():
                if key == target_shelf:
                    value = value.extend([number_doc])
            # print(directories)
    return
  
def add_chelf(directories): # команда as 
    chelf = input('Введите номер полки, которую нужно создать: ')
    if chelf in directories:
        print('Такая полка есть')
    else:
        directories[chelf] = []
        print(f'Полка {chelf} создана')
        return 
    
def quary_command():        
    command = True
    while command:
        print()
        command = input('Введите команду: ')
        if command.lower() == 'p':
            output_name(documents)
        elif command.lower() == 's':
            output_place(directories)
        elif command.lower() == 'l':
            output_list_docs(documents)
        elif command.lower() == 'a':
            add_docs(documents)
        elif command.lower() == 'd':
            delete_docs(documents)
        elif command.lower() == 'm':
            move_docs(documents)
        elif command.lower() == 'as':
            add_chelf(directories) 
        else:
            print('Такой команды нет')
      
quary_command()
