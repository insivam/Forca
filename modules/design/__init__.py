def menu(lst):  # Brings up a menu in console
    from time import sleep

    while True:
        sleep(1.5)

        print('-'*25)
        print('MENU'.center(25))
        print('-'*25)

        for c, i in enumerate(lst):
            print(f"{c+1} - {i}")

        try:
            UI = int(input('Qual a sua escolha: '))

        except Exception:
            print('\033[31mResposta invalida\033[m')
            continue

        else:
            if UI > len(lst) or UI <= 0:
                print('\033[31mResposta invalida\033[m')
                continue

            if UI == 6:
                print('Até a proxima!')
                exit()

            print()
            return(UI)
