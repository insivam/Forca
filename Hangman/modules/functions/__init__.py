# opens the word file, and if necessary creates one
from math import e


def open_file(am='r'):
    global file
    try:
        with open('Words', 'rt'):
            creat = False
    except:
        try:
            with open('Words', 'x') as file:
                creat = True
        except:
            print('\033[31mSistema falhou em criar o arquivo!\033[m')
            exit()
    try:
        file = open('Words', am)
    except Exception:
        print('\033[31mNão foi possivel abrir o arquivo!\033[m')
    else:
        if creat:
            print('\033[32mArquivo criado com sucesso!\033[m')


# Creates a cool loking title
def lines(msg):
    print('-'*25)
    print(msg.center(25))
    print('-'*25)


# Let's you play the game
def play():
    from math import ceil
    from random import randint

    lines('JOGAR')

    open_file()
    data = file.readlines()
    file.close()

    if data == []:
        print('Adicione algumas palavras :)')
        return

    while True:
        word = data[randint(0, len(data)-1)].replace('\n', '')
        lifes = ceil(len(word)*.8)
        guesses = 0
        f_word = []

        for i in word:
            if i != '-':
                f_word.append('_')
            else:
                f_word.append('-')

        guessed = False
        while True:
            for i in f_word:
                print(i, end=' ')
            print(f'   💡= {guesses} 💚 = {lifes}')
            UI = input('Advinhe uma letra ou a palavra: ').upper(
            ).strip().replace(' ', '-')

            if len(UI) == len(word):
                if UI == word:
                    guessed = True
                break

            if UI == '' or UI[0] in f_word:
                continue

            guesses += 1
            lifes -= 1

            if '_' not in ''.join(f_word):
                guessed = True
                break
            elif lifes == 0:
                break
            else:
                for c, l in enumerate(word):
                    if l == UI[0]:
                        f_word[c] = l

        print()
        print(f'A palavra era {word}'.center(27))
        print(f'Voce adivinhou em {guesses} tentativas | {lifes} vidas' if guessed
              else f'Acabou suas vidas | {guesses} tentativas')

        while True:
            try:
                UI = input('Quer jogar de novo (S/N): ').upper().strip()[0]
            except Exception:
                print('\033[31mResposta invalida\033[m')
                continue
            if UI in 'SN':
                break
            print('\033[31mResposta invalida\033[m')
        if UI == 'S':
            continue
        return


# View all the words in the game
def view():
    lines('PALAVRAS')

    open_file()
    data = file.readlines()
    file.close()

    if data == []:
        print('Adicione algumas palavras :)')
        return

    for line in data:
        print(line.replace('\n', '').center(25))


# Add a new Word to the game
def add():
    lines('ADICIONAR')
    while True:
        UI = input("Qual palavra gostaria de adicionar: ").strip(
        ).upper().replace(' ', '-')

        open_file()
        data = file.readlines()
        file.close()

        for i in data:
            if UI == i.replace('\n', ''):
                print('\033[31mPalavra já foi adicionada antes\033[m')
                return

        if UI == '' or '_' in UI:
            print('\033[31mResposta invalida\033[m')
            continue

        open_file(am='a')
        file.write(f"{UI}\n")
        file.close()
        print('\033[32mPalavra adicionada com sucesso\033[m')
        while True:
            UI = input('Quer adiciona outra (S/N): ')[0].upper().strip()
            if UI in 'SN':
                break
            print('\033[31mResposta Invalida\033[m')
        if UI == 'S':
            continue
        return


# Delete a word from the game
def delete():
    lines('DELETAR')
    while True:
        UI = input('Qual palavra gostaria de deletar: ').upper().strip()

        open_file()
        data = file.readlines()
        file.close()

        words = []
        word = False
        for line in data:
            if line.replace('\n', '') != UI:
                words.append(line)
            else:
                word = True

        open_file('w')
        for i in words:
            file.write(i)
        file.close()

        if word:
            print(f'\033[32mPalavra {UI} deletada com sucesso\033[m')
            return
        print(f'\033[31mPalavra {UI} não encontrada!\033[m')

        while True:
            UI = input('Quer deletar outra (S/N): ')[0].upper().strip()
            if UI in 'SN':
                break
            print('\033[31mResposta Invalida\033[m')
        if UI == 'S':
            continue
        return


# Calls one of the functions above
def call(num):
    lst = [play, view, add, delete]
    lst[num-1]()
