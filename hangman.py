import pygame
import random
import sys

pygame.init() # preparing the module pygame for operation

screen = pygame.display.set_mode((1600, 900)) # creating app window res 1600x900 ; type surface (2D object)

surface = pygame.Surface((800, 200)) # Increase the size of the surface
surface.fill((255, 255, 255)) # filling the surface color

screen.blit(surface, (400, 450)) # Adjust the coordinates to display the surface on the screen
pygame.display.flip() # displaying changes on the screen

pygame.font.init() # preparing the module pygame_font
font = pygame.font.Font(None, 36) # size of font

dictionary = [
    "акробатика", "биохимия", "вице-канцлер", "гомеопатия", "декортирование",
    "эпистемология", "женевская", "зенитно-ракетный", "идентификация", "кварцевание",
    "лексикография", "многогранник", "нейтринный", "обсидиан", "псевдокарст",
    "центробанк", "ревербератор", "симультанка", "термоядерный", "ультразвук",
    "фрактальный", "хирург", "цианид", "электроэнцефалограф", "японская",
    "авианосец", "бульдозер", "водоподготовка", "гетерогенный", "деэскалация",
    "экспедиционер", "яхтсмен", "антарктический", "бета-катаралаза", "космический",
    "лингвист", "метаморфоз", "оптико-электронный", "памятничек", "ретроград",
    "синхрофазотрон", "трансцендентальный", "универсализация", "флокуляция", "хлорофилл",
    "цитрусовый", "шершень", "энциклопедия", "активатор", "бифуркация", "деспотичный",
    "экзистенциализм", "генетический", "жернов", "зубр", "инквизитор", "коллигативный",
    "манометр", "ницшеанство", "омнибус", "псевдопарадокс", "радиоактивный", "сульфид",
    "теодолит", "ультрамарин", "фотоаэратор", "хризантема", "целлофан", "чародей",
    "шизофрения", "экспериментальный", "юриспруденция", "автоматизация", "барбекю", 
    "визирь", "гранатомет", "дендрит", "эпифантия", "кашицеобразный", "лексикон",
    "псевдосфера", "сцинтилляция", "эксцентричный", "юницеф", "анахронизм", "бактериофаг",
    "венгерский", "геофизика", "диспаритет", "электромиография", "экспоненциальный", 
    "янтарь", "акклиматизация", "благотворительность", "вице-президент", "гипнотизм",
    "дифференциация", "экстраполяция", "ювелир", "завитушка"
]

choose_word = random.choice(dictionary) # choose the random word
guessed_letters = set() # create a set where will come the letters which user guessed

attempts = 6
input_text="" # переменная для хранения введеного текста польз.
while attempts > 0:
    for event in pygame.event.get(): # перебираем все события, которые произошли в pygame (типа нажатие клавиши мыши и тд)
        if event.type == pygame.QUIT: # если окно закрыли
            pygame.quit() # завершается работа пугейм
            sys.exit() # завершается выполнение программы
        elif event.type == pygame.KEYDOWN: # если нажали клавишу
            if event.unicode.isalpha(): # если это буква
                letter = event.unicode.lower() # преобразование символа в строчный формат
                if letter not in guessed_letters:
                    if letter in choose_word:
                        guessed_letters.add(letter)
                    else:
                        attempts -= 1
                input_text += letter
                if event.key == pygame.K_RETURN:  # Если нажат Enter
                    # Обработка введенной буквы после нажатия Enter
                    input_text = ""  # Сброс введенной буквы после подтвержденияи

    text = font.render("Слово: " + " ".join(a if a in guessed_letters else "_" for a in choose_word), True, (0, 0, 0))
    input_surface = font.render("Введенная буква: " + input_text, True, (0, 0, 0))

    surface.fill((255, 255, 255)) # заливает поверхность белым цветом
    screen.blit(surface, (400, 450)) # отображается surface на основном экране
    screen.blit(text, (400, 450)) # отображается "Слово: "
    screen.blit(input_surface, (400, 500)) # "введеная буква:"
    pygame.display.flip()

    if set(choose_word) <= guessed_letters: # если множество всех букв рандомного слова <= множеству угаданых слов
        print("Поздравляю, вы угадали слово:", choose_word)
        break
    elif attempts == 0:
        print("Игра окончена. Вы проиграли. Загаданное слово было:", choose_word)
        break
pygame.quit() # end pygame // script completed
sys.exit()



