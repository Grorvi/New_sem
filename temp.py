def menu():
    dict_phnbk = {}
    while True:
        anc = int(input('Введите запрос: 1:Сохранить телефонную книгу, 2: Показать все контакты, 3:Найти контакт '
                        '4:Добавить контакт, 5:Изменить контакт,  6: Удалить контакт, 7: Выход :'))
        if anc == 1:
            save_dir(dict_phnbk)
            print('save')
        elif anc == 2:
            if len(dict_phnbk) == 0:
                dict_phnbk = open_read_dir()
            if len(dict_phnbk) == 0:
                print('Справочник пуст')
            else:
                print(dict_phnbk)
        elif anc == 3:
            cntc_find(dict_phnbk)
        elif anc == 4:
            value_new_cnt = add_cntc(dict_phnbk)
            print(value_new_cnt)
            dict_phnbk.update(value_new_cnt)
            print('Сохранись!')
        elif anc == 5:
            new_cntc = cntc_find(dict_phnbk)
            add_cntc(dict_phnbk, new_cntc)
        elif anc == 6:
            new_cntc = cntc_find(dict_phnbk)
            print(f'Удалили контант:{new_cntc[0]}: {dict_phnbk.pop(new_cntc[0])}')
            print('Сохранись!')
        elif anc == 7:
            print('End')
            break
        else:
            print('Введите ещё раз')
            
