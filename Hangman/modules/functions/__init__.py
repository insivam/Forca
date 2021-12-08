from time import sleep
from math import e
regra = '''O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra proposta, tendo como dica o número de letras.
O jogador começa com uma quantidade de tentivas, a cada 1 letra errada, o jogador perde uma tentativa.
O jogo termina com o acerto da palavra ou com o término de tentativas.

Exemplo:

M E R C A D O ------> _ _ _ _ _ _ _
O jogador deve ir digitando as letras que podem existir na palavra.
A cada letra correta é escrita no espaço correspondente.

M E R C A D O → M _ _ C A _ _
Caso a letra não exista nessa palavra, é subtraido 1 de suas tentativas

O jogador pode escolher entre digitar uma letra ou fazer uma tentativa perigosa de adivinhar a palavra, digitando a palavra que pensa que é.

Caso o jogador deseja fazer uma tentativa perigosa de tentar adivinhar a palavra digitando e ele errar a palavra ele perde na hora.

O jogo é ganho se a palavra é adivinhada. Caso o jogador não descubra qual palavra é, ele perde o jogo.
'''


# opens the word file, and if necessary creates one
def open_file(am='r'):
    global file
    try:
        with open('Words', 'rt', encoding='utf-8') as file:
            creat = False
    except:
        try:
            with open('Words', 'x', encoding='utf-8') as file:
                creat = True
        except:
            print('\033[31mSistema falhou em criar o arquivo!\033[m')
            exit()
    try:
        file = open('Words', am, encoding='utf-8')
    except Exception:
        print('\033[31mNão foi possivel abrir o arquivo!\033[m')
    else:
        if creat:
            print('\033[32mArquivo criado com sucesso!\033[m')


# Creates a cool loking title
def lines(msg):
    print('-'*33)
    print(msg.center(33))
    print('-'*33)


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
        if lifes > 15:
            lifes = 15
        lifes = max(6, lifes)
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
            if lifes == 0:
                UI = input('Advinha uma palavra: ').upper(
                ).strip().replace(' ', '-')
                if UI == word:
                    guessed = True
                    break
                break
            UI = input('Advinhe uma letra ou a palavra: ').upper(
            ).strip().replace(' ', '-')

            if len(UI) == len(word):
                if UI.lower() == word.lower():
                    guessed = True
                break

            if UI == '' or UI[0] in f_word:
                print()
                continue

            guesses += 1
            lifes -= 1

            print()

            for c, l in enumerate(word):
                if l == UI[0]:
                    f_word[c] = l
            if '_' not in f_word:
                guessed = True
                break

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

        print()
        if UI == 'S':
            play()
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


def regras():
    lines('Regras')
    for i in regra:
        print(i, end='')
        sleep(.035)


# Calls one of the functions above
def call(num):
    lst = [play, view, add, delete, exit, regras]
    lst[num-1]()
