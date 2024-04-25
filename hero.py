from time import sleep
from random import randint


# Функция для создания рамок с возможностью задания цвета
def bordered(text, color_code):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['\033[' + color_code + 'm┌' + '─' * width + '┐\033[0m']
    for s in lines:
        res.append('\033[' + color_code + 'm│\033[0m' + (s + ' ' * width)[:width] + '\033[' + color_code + 'm│\033[0m')
    res.append('\033[' + color_code + 'm└' + '─' * width + '┘\033[0m')
    return '\n'.join(res)


class Inventory:
    def __init__(self):
        self.items = {}

    # Метод добавления предмета в инвентарь
    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    # Метод удаления предмета из инвентаря
    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]
        else:
            print("Этого предмета нет в инвентаре.")

    # Метод отображения инвентаря
    def display_inventory(self):
        print("Инвентарь:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")


# Создание инвентаря и пример его использования
inventory = Inventory()
inventory.add_item("Меч")
inventory.add_item("Зелье здоровья")
inventory.add_item("Монеты", 10)
inventory.remove_item("Монеты", 5)
inventory.display_inventory()


class Weapon:
    def __init__(self, name, power_min, power_max, armor):
        self.name = name
        self.power_min = power_min
        self.power_max = power_max
        self.armor = armor


class ThrowingWeapon(Weapon):
    def __init__(self, name, power_min, power_max, armor, quantity):
        super().__init__(name, power_min, power_max, armor)
        self.quantity = quantity

    # Метод метания метательного оружия
    def throw(self):
        if self.quantity > 0:
            print(f"Вы метнули {self.name}")
            self.quantity -= 1
        else:
            print("У вас закончились снаряды!")


# Пример использования метательного оружия
shurikens = ThrowingWeapon("Шурикены", 20, 30, 0, 10)
shurikens.throw()
shurikens.throw()
shurikens.throw()
print(f"Осталось шурикенов: {shurikens.quantity}")


class Hero:
    def __init__(self, name, health, armor, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon

    # Метод восстановления здоровья героя при помощи пива
    def viper_pivo(self):
        self.health += 60
        print(self.name, 'восполнил себе здоровье')
        print('теперь уровень здоровья героя - ', self.health)

    # Метод повышения уровня героя после боя
    def lvl_up(self):
        self.health += 10
        self.armor += 20
        print(self.name, 'Повышение уровня')
        self.print_info()

    # Метод для определения, будет ли герой атаковать противника
    def is_attack(self, enemy):
        if input('Вступить в бой?').lower() == 'да':
            self.fight(enemy)
            if enemy.health <= 0:
                print(self.name, 'Победил!')
                return True
        else:
            print(self.name, 'В страхе убежал с поля боя, видимо ему еще рано')
            print('Конец игры')

    # Метод вывода начальной информации о герое и его статистики
    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        sleep(1)
        print('Уровень здоровья:', self.health)
        sleep(1)
        print('Класс брони:', self.armor)
        sleep(1)
        print('Сила удара:', self.weapon.power_max)
        sleep(1)
        print('Оружие:', self.weapon.name)
        sleep(1)
        print(' ')

    # Метод для проведения одного удара
    def strike(self, enemy):
        punched = randint(self.weapon.power_min, self.weapon.power_max)
        print('Удар!', self.name, 'атакует', enemy.name, 'силой', punched, 'используя', self.weapon, '\n')
        enemy.armor -= punched
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

    # Метод для проведения боя между героем и противником
    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в бою!!!!\n')
                break
            sleep(5)
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в бою!!!!\n')
                break
            sleep(5)


class NPC:
    def __init__(self, name, add_skill):
        self.name = name
        self.add_skill = add_skill

    # Метод для увеличения здоровья героя
    def health(self, hero):
        hero.health += 10
        print(self.name, 'Исцелил нашего героя', hero.name)
        print('Теперь уровень здоровья героя - ', hero.health)

    # Метод для починки брони героя
    def repair(self, hero):
        if hero.armor <= 100:
            hero.armor = 100

        print(self.name, 'Починил броню героя, теперь уровень брони составляет', hero.armor)


test = Hero('tst', 100, 100, Weapon('weapon', 100, 50, 30))

test.print_info()


class Enemy:
    def __init__(self, name, health, armor, weapon, add_skill):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon
        self.add_skill = add_skill

    # Метод для вывода информации о противнике
    def print_info(self):
        print('Поприветствуйте зловещего врага ->', self.name)
        sleep(1)
        print('Уровень здоровья:', self.health)
        sleep(1)
        print('Класс брони:', self.armor)
        sleep(1)
        print('Сила удара:', self.weapon.power_max)
        sleep(1)
        print('Оружие:', self.weapon.name)
        sleep(1)
        print(' ')

    # Метод для применения уникального навыка противника
    def apply_skill(self):
        print(f'Враг {self.name} применил уникальный навык {self.add_skill} и стал сильнее')

    # Метод для проведения удара противника
    def strike(self, enemy):
        punched = randint(self.weapon.power_min, self.weapon.power_max)
        print('Удар!', self.name, 'атакует', enemy.name, 'силой', punched, 'используя', self.weapon, '\n')
        enemy.armor -= punched
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0


class Ghost(Enemy):
    def __init__(self, name, health, armor, power_min, power_max, weapon, add_skill, visibility=True):
        super().__init__(name, health, armor, weapon, add_skill)
        self.visibility = visibility

    # Метод для скрытия противника от героя
    def invisible(self):
        print(f'{self.name} Скрылся от глаз героя, его теперь нельзя атаковать')
        self.visibility = False


# Коды для цвета рамки
color_code_red = "91"
color_code_blue = "94"
color_code_green = "92"
color_code_yellow = "93"


def start_history():
    print(bordered('история Ричарда началась когда его отец не мало известный рыцарь погиб от лап дракона',
                   color_code_green))
    # sleep(2)
    print(bordered('Ричарду на тот момент было 5 лет и с тех пор он решил,что он должен отомстить.', color_code_green))
    # sleep(2)
    print(
        bordered('И вот шли годы на протяжении всего этого времени он тренировался не покладая рук.', color_code_green))
    # sleep(2)
    print(bordered('И вот с той трагедии прошло 12 лет и Ричард решил,что время мести настало.', color_code_green))
    # sleep(2)


def act1():
    print(
        bordered('Ричард двинулся в путь и пройдя через реки и поля он наконец то подходит к следующему припядствию.',
                 color_code_green))
    # sleep(2)
    print(bordered(
        'Это был тёмный и мрачный лес.Ричарду было страшно в него заходить,но он вспомнил про свою цель и не задумываясь вступил в него.',
        color_code_green))
    # sleep(2)
    print(bordered(
        'И вот пройдя уже по леса он подумал, что дальше будет также легко,он даже удивился почему этот лес все так боялись.',
        color_code_green))
    # sleep(2)
    print(bordered(
        'Но вдруг из гущи леса на него выбегают 3 гнома которые требуют с него 3 золотые монеты,либо они его убьют.',
        color_code_red))
    # sleep(2)


def act2():
    print(bordered('Он не растерялся и с помощью своего меча отрубил 3 головы сразу.', color_code_red))
    # sleep(2)
    print(bordered('после этой битвы Ричард очень устал.', color_code_green))
    sleep(2)
    print(
        bordered('и подумал что в этом лесу обязательно должно быть какое то заведение для отдыха.', color_code_green))
    sleep(2)
    print(bordered(' И спустя пол часа скитаний он наткнулся на подпольное казино гномов.', color_code_green))
    sleep(2)
    print(bordered(' Но оттуда его выгнали ведь он был выше назначенного роста, а именно 80 см.', color_code_green))
    sleep(2)
    print(bordered('И тогда Ричард в отчаянии пошёл дальше, но вдруг удача ему улыбнулась и он увидел издалека бар.',
                   color_code_green))
    sleep(2)
    print(bordered('Подойдя поближе он увидел что это бар кентавра Джо.', color_code_green))
    sleep(2)
    print(bordered('Но цены на пивчанский не устроили Ричарда и он решил затеять драку с Джо.', color_code_red))
    sleep(2)


def act3():
    print(bordered('Джо конечно был не опытным бойцом но отдавать просто так свой напиток не хотел.', color_code_green))
    sleep(2)
    print(bordered('И по итогу Ричард хоть и потерял чуть здоровья но выйграл этот бой.', color_code_red))
    sleep(2)
    print(bordered('После этой схватки у Ричардо появился новый предмет как ПИВО,', color_code_yellow))
    sleep(2)
    print(bordered(
        'это было зелье исцеление которое он мог выпить в любой следующей битве что бы восполнить 60 едениц здоровья ',
        color_code_yellow))
    sleep(2)
    print(bordered('Позже он двинулся на север в сторону города под названием АНОР ЛОНДО.', color_code_green))
    sleep(2)
    print(bordered('Там он поченил свою броню у кузница и поел у бабушки Мери.', color_code_green))
    sleep(2)
    print(bordered('После полноценного отдыха он решил продолжить свой путь.', color_code_green))
    sleep(2)


def act4():
    print(bordered('Его следующая цель была Долина Драконов.', color_code_green))
    sleep(2)
    print(bordered('Кузнец ему рассказал что там обитает старый вид драконов который очень опасен из за своего яда.',
                   color_code_green))
    sleep(2)
    print(bordered('Но для ричарда его слова были лишь мотивацией пойти туда.', color_code_green))
    sleep(2)
    print(bordered(
        'И вот спустя 3 дня непрерывной дороги он видит ущелье в котором очень странно светится ярко-зелёным цветом река и скалы.',
        color_code_green))
    sleep(2)
    print(bordered(
        'Пройдя немного дальше он слышит громкий топот и сопение и повернув голову влево он видит его,того самого дракона про которого говорил кузнец.',
        color_code_red))
    sleep(2)
    print(bordered(
        'Весь покрыт плотной чешуёй тёмно-зелёного цвета дракон идёт в сторону Ричарда и Ричард понимает что битвы не избежать.',
        color_code_red))
    sleep(2)


def act4_1():
    print(bordered(
        'И ричард делает первый рывок в его сторону и наносит своим мечом первый удар в зону живота,но из за плотной чешуи дракон не чувствует удара и атакует в ответ.',
        color_code_red))
    sleep(2)
    print(bordered('выпустив свой яд, небольшая часть одежды Ричарда расщепляется.', color_code_red))
    sleep(2)
    print(bordered(
        'Но его это не остановила и он продолжил драку, но у него осталось мало здоровья и он решил восполнить его с помощью пива.',
        color_code_red))


def act5():
    sleep(2)
    print(bordered(
        'Но даже восполнив здоровье он понял что проиграет эту битву ведь его меч был почти сломан и тогда Ричарду пришлось отступить.',
        color_code_red))
    sleep(2)
    print(bordered('И подумав про починку своего меча он решил направиться в сторону юга в город АРИАМИСА',
                   color_code_green))
    sleep(2)
    print(bordered('Где он повстречал хорошего дворянина Джозафа.', color_code_green))
    sleep(2)
    print(bordered('Джозаф ему поведал что есть место где можно заполучить очень хороший меч.', color_code_green))
    sleep(2)
    print(bordered('Но что бы заполучить этот артефакт нужно победить орка МЕТАФОРОНА', color_code_yellow))
    sleep(2)
    print(bordered('Но ричарда эта информация не чуточки не напугала, а наоборот замотивировала.', color_code_green))
    sleep(2)
    print(
        bordered('И вот после починки меча Ричард двинулся в путь, а именно в Склеп Великанов,там и обитал МЕТАФОРОН.',
                 color_code_green))
    sleep(2)


def act6():
    print(bordered('И спустя неделю пути он видит тот самый Склеп.', color_code_green))
    sleep(2)
    print(bordered('В котором через туман виднеется огромная рука МЕТАФОРОНА. ', color_code_red))
    sleep(2)
    print(bordered('Ричард акуратно подходя к орку случайно наступает на ветку от чего она ломается и издаёт треск.',
                   color_code_red))
    sleep(2)
    print(bordered(
        'От этого треска просыпается орк, и начинается смертельная битва, Ричард понимал что он слабее и не сможет адалеть орка в схватке лицом к лицу.',
        color_code_red))
    sleep(2)
    print(
        bordered('Но тут из за бетонной колонны выбегает Джозаф и с помощью лука отвлекает чудовище.', color_code_red))
    sleep(2)
    print(bordered('И Ричард пользуясь моментом наносит удар в живот.', color_code_red))
    sleep(2)
    print(bordered('От чего орк падает на землю и Ричард с Джозафом добивают МЕТАФОРОНА.', color_code_red))
    sleep(2)
    print(bordered(
        'И Ричарду достаётся желанный трофей в виде меча МЕТАФОРОНА, который так и прозвали в честь его бывшего хозяина.\n',
        color_code_yellow))
    sleep(2)
