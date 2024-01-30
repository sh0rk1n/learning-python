import pygame
import random

pygame.init() # preparing the module pygame for operation

screen = pygame.display.set_mode((1600, 900)) # creating app window res 1600x900 ; type surface (2D object)

surface = pygame.Surface((1600,900)) # (1600,900) - tuple ; surface() - function/class?
surface.fill((255,255,255)) # filling the surface  color

screen.blit(surface,(300,250)) # displaying the surface on the screen
pygame.display.flip() # displaying changes on the screen

pygame.font.init()
font = pygame.font.Font(None,36)

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

attemps = 6
while attemps > 0:
    letter = input("Введите букву: ").lower()
    
    # Отображение текущего состояния слова с угаданными буквами
    text = font.render("Слово: " + " ".join(a if a in guessed_letters else "_" for a in choose_word), True, (0, 0, 0))
    surface.fill((255, 255, 255))  # Очистка поверхности перед обновлением
    screen.blit(surface, (300, 250))  # Отображение поверхности на экране
    screen.blit(text, (300, 500))  # Отображение текста с текущим состоянием слова
    pygame.display.flip()  # Обновление экрана

    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            print("Вы уже угадали букву!")
        elif letter in choose_word:
            guessed_letters.add(letter)
            print("Вы угадали! Слово: ", " ".join(a if a in guessed_letters else "_" for a in choose_word ))
        else:
            attemps -=1
            print("Вы не угадали! Осталось попыток: ", attemps)
    else:
        print("Введите корректную букву!")


running = True
while running:
    
    for event in pygame.event.get(): # перебирает все события - iterates throught all events
        if event.type == pygame.QUIT: # если закрыли окно - if closed the app windows
            running= False # cycle end

pygame.quit() # end pygame // script completed


