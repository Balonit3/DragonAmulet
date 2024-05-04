from time import sleep
from random import randint


# TODO Обновил функцию рамок, теперь цвет можно задавать кодами в момент вызова функции
def bordered(text, color_code):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['\033[' + color_code + 'm┌' + '─' * width + '┐\033[0m']
    for s in lines:
        res.append('\033[' + color_code + 'm│\033[0m' + (s + ' ' * width)[:width] + '\033[' + color_code + 'm│\033[0m')
    res.append('\033[' + color_code + 'm└' + '─' * width + '┘\033[0m')
    return '\n'.join(res)


class Hero:
    def __init__(self, name, health, armor, power_min, power_max, weapon, ):
        self.name = name
        self.health = health
        self.armor = armor
        self.power_min = power_min
        self.power_max = power_max
        self.weapon = weapon



    # TODO метод хила при помощи пива
    def viper_pivo(self, ):
        self.health += 60
        print(self.name, 'восполнил себе здоровье')
        print('теперь уровень здоровья героя - ', self.health)

    # TODO метод прокачки героя после боя
    def lvl_up(self):
        self.health += 10
        self.armor += 20
        print(self.name, 'Повышение уровня')
        self.print_info()

    # TODO метод с вопрос о нападении
    def is_attack(self, enemy):
        if input('Вступить в бой?').lower() == 'да':
            self.fight(enemy)
            if enemy.health <= 0:
                print(self.name, 'Победил!')
                return True
        else:
            print(self.name, 'В страхе убежал с поля боя, видимо ему еще рано')
            print('Конец игры')

    # TODO метод вывода начальной информации о герое и статистике
    def print_info(self):
        print('Поприветсвтуйте героя ->', self.name)
        sleep(1)
        print('Уровень здоровья:', self.health)
        sleep(1)
        print('Класс брони:', self.armor)
        sleep(1)
        print('Сила удара:', self.power_max)
        sleep(1)
        print('Оружие:', self.weapon)
        sleep(1)
        print(' ')

    # TODO метод одного удара
    def strike(self, enemy):
        punched = randint(self.power_min, self.power_max)
        print('Удар!', self.name, 'атакует', enemy.name, 'силой', punched, 'используя', self.weapon, '\n')
        enemy.armor -= punched
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

    # TODO метод полноценного боя
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

    def health(self, hero):
        hero.health += 10
        print(self.name, 'Исцелил нашего героя', hero.name)
        print('Теперь уровень здоровья героя - ', hero.health)

    def repair(self, hero):
        if hero.armor <= 100:
            hero.armor = 100

        print(self.name, 'Починил броню героя, теперь урвень брони составляет', hero.armor)


class Enemy(Hero):
    def __init__(self, name, health, armor, power_min, power_max, weapon, add_skill):
        super().__init__(name, health, armor, power_min, power_max, weapon)
        self.add_skill = add_skill






    def apply_skill(self):
        print(bordered(f'Враг {self.name} применил уникальный навык {self.add_skill} теперь он стал сильнее',color_code_purple))


class Gost(Enemy):
    def __init__(self, name, health, armor, power_min, power_max, weapon, add_skill, visibility=True):
        super().__init__(name, health, armor, power_min, power_max, weapon, add_skill)
        self.visibility = visibility

    def invisible(self):
        print(f'{self.name} Скрылся с глаз героя, его теперь нельзя атаковать')
        self.visibility = False



class BowWomen(Enemy):
    def __init__(self, name, health, armor, power_min, power_max, weapon, add_skill, fastshoot=True):
            super().__init__(name, health, armor, power_min, power_max, weapon, add_skill)
            self.fastshoot = fastshoot


class RedEyes(Enemy):
    def __init__(self, name, health, armor, power_min, power_max, weapon, add_skill, bifurcation=True):
            super().__init__(name, health, armor, power_min, power_max, weapon, add_skill)
            self.bifurcation = bifurcation




# Коды для цвета рамки
color_code_red = "91"
color_code_blue = "94"
color_code_green = "92"
color_code_yellow = "93"
color_code_purple = "35"


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
        bordered('Ричард двинулся в путь и пройдя через реки и поля он наконец то подходит к следующему припядствию. ',
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
        'И Ричарду достаётся желанный трофей в виде меча МЕТАФОРОНА, который так и прозвали в честь его бывшего хозяина.', color_code_yellow))
    sleep(2)
def act7():
    print(bordered('После всех этих боёв Ричард видит что в его кармане не осталось ни одной золотой монеты.', color_code_green))
    sleep(2)
    print(bordered('И он принимает решение заработать.',color_code_green))
    sleep(2)
    print(bordered('И как раз на выходе из склепа он замечает на дерево листок на котором написан: (‘Дорогой друг, если у тебя не осталось ни монеты золотой приходи ты в башню к нам и получишь приз ты свой’).',color_code_green))
    sleep(2)
    print(bordered('Ричарда очень заинтересовало это предложение и он отправился в деревню Энденвиль.',color_code_green))
    sleep(2)
    print(bordered('Там и находилась эта башня.',color_code_green))

def act8():
    print(bordered('И придя  к воротам этой деревни спустя несколько дней он удивился что на окраине северо - западной долины  стоит такая красивая деревня.',color_code_green))
    sleep(2)
    print(bordered('И зайдя в неё он увидел множество людей которые занимались своими делами.',color_code_green))
    sleep(2)
    print(bordered('Кто то поливал огород,кто то работал в своем ларьке и продавал рыбу,кто то например кузнец Валера делал очередные подковы для коней.',color_code_green))
    sleep(2)
    print(bordered('И Ричарда заинтересовал именно кузнец и подойдя к нему он спросил,зачем ты делаешь подковы если в этой деревне нету коней.',color_code_green))
    sleep(2)
    print(bordered('И тот ему ответил что они есть просто очень и очень мало.',color_code_green))
    sleep(2)
    print(bordered('Ведь недавно был набег гномов грабителей и они убили большую часть лошадей.',color_code_green))
    sleep(2)
    print(bordered('После Ричард поведал что недавно убил 3 таких гномов,но Валера сказал что 3 это очень мало ведь их армия насчитывает около 120 гномов.',color_code_green))
    sleep(2)
    print(bordered('И тогда Ричард вспомнил зачем он подходил к кузнецу,а именно узнать где находится башня.',color_code_green))
    sleep(2)
    print(bordered('И кузнец направил Ричарда куда ему нужно.',color_code_green))
    sleep(2)


def act9():
    print(bordered('И отойдя чуть дальше от кузницы Валеры, главный герой увидел высокую,каменную,c большим флагом башню.',color_code_green))
    sleep(2)
    print(bordered('И спросив у Валеры что это за флаг?',color_code_green))
    sleep(2)
    print(bordered('Он получил ответ что это флаг их деревни.',color_code_green))
    sleep(2)
    print(bordered('И пройдя внутрь Ричард поднял голову и увидел очень много этажей.',color_code_green))
    sleep(2)
    print(bordered('А на входе в башню сидел  старик Генрих.',color_code_green))
    sleep(2)
    print(bordered('Он и поведал Ричарду за что ты получишь золото.',color_code_green))
    sleep(2)
    print(bordered('Оказалось не так всё  просто, ведь чтобы получить золото нужно пройти около 20 этажей и за каждый из них ты получишь по 2 монеты.',color_code_green))
    sleep(2)
    print(bordered('Ричарда очень заинтересовало это предложение и он направился вверх.',color_code_green))
    sleep(2)


def act10():
    print(bordered('На первых из них находились самые слабые мобы которых Ричард без труда прошёл.',color_code_green))
    sleep(2)
    print(bordered('Однако после 5 этажа начались мобы среднего уровня на которых Ричард уже получал хоть и маленький но урон.',color_code_green))
    sleep(2)
    print(bordered('А вот последние 6 этажей были самыми сложными.',color_code_green))
    sleep(2)
    print(bordered('Например на 26 был призрак Каспер который умел становиться невидимым и наносить урон Ричарду тогда когда он не ожидал этого.',color_code_red))
    sleep(2)



def act10_1():
    print(bordered(
        'Также у него была спасобность по названием крик,он умел кричать на стоклько громко что наносил урон от своего крика.',
        color_code_red))
    sleep(2)
def act10_2():
    print(bordered('И вот когда у Ричарда осталось 20 единиц здоровья он подумал что умирает.',color_code_red))
    sleep(2)
    print(bordered('Но вспомнив про свою цель отомстить за отца он встал и надеясь на удачу нанес удар в пустоты и на удивление он попал прямо в голову Касперу',color_code_red))
    sleep(2)
    print(bordered('И тот погиб.Отлежавшись в комнатах для отдыха между этажами он двинулся дальше.',color_code_green))
    sleep(2)
    print(bordered('Следующим против него вышла лучница Летисия.',color_code_red))
    sleep(2)
def act10_3():
    print(bordered('Ее способность была такова что она могла ускорять свой натяг стрелы из за этого её стрелы летели очень быстро.',color_code_red))
    sleep(2)
def act10_4():
    print(bordered('И Ричарду было очень сложно бороться против нее ведь она даже не подпускала его к себе.',color_code_red))
    sleep(2)
    print(bordered('Но в последний момент когда у него было очень мало брони, он вспомнил про ядовитые дротики которые купил у прадовца в лесу по дороги к этой деревни.',color_code_red))
    sleep(2)
    print(bordered('И кинув 3 штуки сразу они поразили ногу,грудь и плечо лучницы.',color_code_red))
    sleep(2)
    print(bordered('От чего она упала и погибла.',color_code_red))
    sleep(2)


def act11():
    print(bordered('И вот время последнего этажа Ричард уже на исходе, у него мало брони,мало здоровья,почти сломано оружие.',color_code_green))
    sleep(2)
    print(bordered('Он думает кто же будет против него на этот раз.',color_code_green))
    sleep(2)
    print(bordered('И выходит маленький гномик и говорит, что в той битве в начале пути Ричарда против гномов он убил его маму,папу и брата.',color_code_red))
    sleep(2)
    print(bordered('Этот гномик ждал свою семью дома несколько дней, но так и не дождался.',color_code_green))
    sleep(2)
    print(bordered('И он попросил убить и его.',color_code_green))
    sleep(2)
    print(bordered('Но Ричард пожалел о той битве и очень сильно поменялся в лице.',color_code_green))
    sleep(2)
    print(bordered('И вместо того радостного рвущегося к победе рыцаря он стал морально подавленным и грустным человеком.',color_code_green))
    sleep(2)
    print(bordered('Ричард никак не мог убить этого гномика.',color_code_green))
    sleep(2)
    print(bordered('Но он понимал что не убив его он не получит золото.',color_code_green))
    sleep(2)
    print(bordered('И постояв там некоторое время он принял решение что честь дороже золота,извинился перед этим гномом и просто спустился на 1 этаж к старику.',color_code_green))
    sleep(2)
    print(bordered('И сказал прости,но я не смог пройти все 20 этажей.',color_code_green))
    sleep(2)
    print(bordered('Но вдруг старик улыбнулся и сказал что это и было финальное испытание и он выиграл своё золото.',color_code_green))
    sleep(2)
    print(bordered('Ричард стоял в недоумении,но старик ему сказал:’видишь ли,мы делаем последний этаж таким специально, мы берём случаи которые произошли с воином за последнее время и делаем из этих случаев моральное испытание.',color_code_green))
    sleep(2)
    print(bordered('И ты единственный кто смог его пройти’ и после этих слов старик отдал Ричарду мешок с золотом.',color_code_yellow))
    sleep(2)
    print(bordered('А именно с 40 монетами.',color_code_yellow))
    sleep(2)


def act12():
    print(bordered('И Ричард выйдя с этой башни был очень рад и доволен собой.',color_code_green))
    sleep(2)
    print(bordered('Но в его голове пролетела мысль,что же мне делать дальше.',color_code_green))
    sleep(2)
    print(bordered('И он подумал и принял решение идти к своему старому знакомому а именно к магу по имени Мерлин.',color_code_green))
    sleep(2)
    print(bordered('Но идти до него было очень долго и тогда он вспомнил что в этой деревне были кони.',color_code_green))
    sleep(2)
    print(bordered('И пройдясь по этой деревушке он наткнулся на загон с лошадьми и купив белого коня за 5 золотых монет,он дал ему имя Пегас.',color_code_green))
    sleep(2)
    print(bordered('И после знакомства со своим новым другом он поехал к Мерлину.',color_code_green))
    sleep(2)
    print(bordered('На выходе поблагодарив Валеру за помощь и отблагодарив его 3 монетами.',color_code_green))
    sleep(2)


def act13():
    print(bordered('По дороге к Мерлину Ричард наблюдал очень красивые виды,великолепные заснеженные  вершины гор, много рек и озёр,а также  зеленые леса.',color_code_green))
    sleep(2)
    print(bordered('И в одном из таких зелёных лесов он повстречал очень красивую эльфийку по имени Ева.',color_code_green))
    sleep(2)
    print(bordered('У неё были очень красивые глаза и очаровательная улыбка.',color_code_green))
    sleep(2)
    print(bordered('Ричарду Ева сразу понравилась и он решил познакомиться с ней.',color_code_green))
    sleep(2)
    print(bordered('Он подъехал к ней на своём коне и предложил прокатиться с ней.',color_code_green))
    sleep(2)
    print(bordered('Она была не против.',color_code_green))
    sleep(2)
    print(bordered('И вот они мчались по лесу,ветер обдувал их лица,они громко смеялись и наконец остановились.',color_code_green))
    sleep(2)
    print(bordered('И Ева сказала Ричарду что он ей понравился с первого взгляда.',color_code_green))
    sleep(2)
    print(bordered('И что у неё всегда была мечта найти такого как он.',color_code_green))
    sleep(2)
    print(bordered('Ричард задумался о том чтобы взять её с собой но не хотел чтобы она  пострадала,ведь она была слабовата,она лишь умела стрелять из лука и то не слишком хорошо.',color_code_green))
    sleep(2)
    print(bordered('И Ричард подумал про себя,Человек будет пристально смотреть на другого человека, если их чувства едины.',color_code_green))
    sleep(2)
    print(bordered('Чтобы защитить собственное счастье, чтобы воплотить в реальность свои мечты и просто чтобы сохранить свою жизнь. ',color_code_green))
    sleep(2)
    print(bordered('Бывают ли моменты, когда можно осуществить свою мечту, не оставив раны в сердце другого человека?',color_code_green))
    sleep(2)
    print(bordered('После этой мысли он принял решение что не хочет оставлять раны в ее сердце и сказав что он скоро вернется он уехал в закат.',color_code_green))
    sleep(2)

def act14():
    print(bordered('После этой встречи он долго думал про Еву,но не смотря на свои мысли ехал дальше и дальше от нее.',color_code_green))
    sleep(2)
    print(bordered('И вот спустя неделю он доехал до огромного заброшенного замка,где стояла большая каменная башня с длинной лестницей вверх.',color_code_green))
    sleep(2)
    print(bordered('На самом верху этой башня в маленькой комнатке и жил Мерлин.',color_code_green))
    sleep(2)


def act15():
    print(bordered('И зайдя к нему в комнату Ричард был очень рад и счастлив,ведь он не видел Мерлина со времён своего детства,Мерлин был лучшим другом его отца и когда отец Ричарда погиб Мерлин в отчаянии переехал в эту башню.',color_code_green))
    sleep(2)
    print(bordered('Помимо встречи со своим старым другом Ричард ехал сюда спросить по поводу нового оружия,а именно магической тростью,по рассказам жителей города АРИАМИСА эта трость обладала невероятной силой,с ее помощью можно было отбить почти любую атак,но взамен эта трость брала 15% твоей брони.',color_code_green))
    sleep(2)
    print(bordered('Ричарда эти цифры совсем не напугали ведь он планировал не получать урона вовсе.',color_code_green))
    sleep(2)
    print(bordered('Но мерлин сказал что эту трость просто так не достать.',color_code_green))
    sleep(2)
    print(bordered('Чтобы ее заполучить нужно отправиться на северо-запад и отыскать там ПОДЗЕМЕЛЬЕ ИРИТИЛЛА.',color_code_green))
    sleep(2)
    print(bordered('После найти ворота и у их начала тебя будет ждать неизвестное для всех существо.',color_code_green))
    sleep(2)
    print(bordered('Которое загадает тебе загадку.',color_code_green))
    sleep(2)
    print(bordered('И только отгадав её тебя пропустят внутрь.',color_code_green))
    sleep(2)
    print(bordered('Ричарду стало не по себе после слов ‘неизвестное для всех существо’ и он спросил почему неизвестное?',color_code_green))
    sleep(2)
    print(bordered('И старик ответил,потому что из всех рыцарей которые были там ни одному не удалось разгадать загадку.',color_code_green))
    sleep(2)
    print(bordered('Ричард был в недоумении.',color_code_green))
    sleep(2)
    print(bordered('Но был готов к этому испытанию.',color_code_green))
    sleep(2)
    print(bordered('И вот время ехать в путь.',color_code_green))
    sleep(2)
    print(bordered('Мерлин дал Ричарду в подарок мешочек с волшебным порошком и сказал открывать этот мешок в самой критической ситуации.',color_code_green))
    sleep(2)


def act16():
    print(bordered('Путь был очень не близок,но благодаря его верном другу Пегасу он доехал без особых проблем.',color_code_green))
    sleep(2)
    print(bordered('И вот этот момент настал.',color_code_green))
    sleep(2)
    print(bordered('Ричард заходит в это сырое и холодное подземелья.',color_code_green))
    sleep(2)
    print(bordered('Проходит чуть дальше от входа и видит огромные ворота за которыми темнота.',color_code_green))
    sleep(2)
    print(bordered('Но Ричард не испугался и пошёл к ним.',color_code_green))
    sleep(2)
    print(bordered('И вот он уже стоит рядом с ними и вдруг вход через который он зашёл закрывается и всё подземелье покрывает кромешная темнота.',color_code_red))
    sleep(2)
    print(bordered('Начинается землетрясение.',color_code_red))
    sleep(2)
    print(bordered('И в этот момент из темноты за воротами виднеются ярко-красные глаза.',color_code_red))
    sleep(2)
    print(bordered('И очень высоким голосом произносят,ну привет очередной никчемный воин,ты умрёшь также быстро как и все остальные.',color_code_red))
    sleep(2)
    print(bordered('И произносит загадку.',color_code_green))
    sleep(2)
    print(bordered('Утром ходит на 4 ногах,днем на 2 и вечером на 3,что это?',color_code_green))
    sleep(2)
    print(bordered('Ричард не понимает и спрашивает,сколько даётся времени на ответ.',color_code_green))
    sleep(2)
    print(bordered('И монстр ему отвечает что у тебя есть 10 часов и указывает в угол,где стоит 1 ведро воды и 2 сумки лесных ягод и говорит что тебе этого хватит ровно на 10 часов пребывания здесь.',color_code_green))
    sleep(2)
    print(bordered('Если дашь ответ хотя бы на секунду позже умрёшь.',color_code_green))
    sleep(2)


def act17():
    print(bordered('Ричарду понадобилось полчаса чтобы осознать что происходит.',color_code_green))
    sleep(2)
    print(bordered('И он начал перебирать все возможные варианты ответов.Но не один из них не подходил.',color_code_green))
    sleep(2)
    print(bordered('.И вот прошло уже 8 с половиной часов и у Ричарда в голове нету ни одного варианта ответа.',color_code_green))
    sleep(2)
    print(bordered('Но вдруг когда оставалось 3 минуты Ричард вспоминает про подарок Мерлина.',color_code_green))
    sleep(2)
    print(bordered('Он открывает этот мешочек и оттуда вылетает волшебная пыльца,которая обсыпает Ричарда и вдруг у него в голове всплывает слово ЧЕЛОВЕК и он понимает что ответ человек.',color_code_green))
    sleep(2)
    print(bordered('Ведь временные отрезки символизируют жизнь человека,утро это когда мы совсем маленькие и ползаем на четвереньках,день это осознанный возраст человека ходьба на двух ногах и вечер это старость,ходьба с тростью то бишь третьей ногой.',color_code_green))
    sleep(2)
    print(bordered('Он бежит к воротам и говорит ответ.',color_code_green))
    sleep(2)
    print(bordered('И чудовище по ту сторону было очень сильно удивленно,ведь за 30 лет что к нему ходят воины не один не ответил правильно.',color_code_green))
    sleep(2)
    print(bordered('И вот после правильного ответа ворота открылись.',color_code_green))
    sleep(2)
    print(bordered('И за ними стоял огромный зверь похожий на волка и медведя в смеси друг с другом.',color_code_green))
    sleep(2)


def act18():
    print(bordered('И позади монстра виднелся тот самый волшебный посох про который говорил Мерлин.',color_code_green))
    sleep(2)
    print(bordered('Но чтобы его заполучить, нужно одолеть этого зверя.',color_code_green))
    sleep(2)
    print(bordered('И вот, начинается бой.',color_code_red))
    sleep(2)


def act18_1():
    print(bordered('Удар за ударом наносят друг другу наши герои но никто не превзоходит друг друга.',color_code_red))
    sleep(2)
    print(bordered('Но вдруг Ричард наносит удар прямо под сердце менстру и тот падает,но когда Ричард приближается чтобы добить зверя,то враг резко поднимается и стремительным рывком с огромной скоростью атакует Ричарда после чего у Ричарда остаётся 20 единиц здоровья.',color_code_red))
    sleep(2)
    print(bordered('И он пытается из последних сил нанести удар по зверю, но вдруг зверь останавливается и раздваивается и с левой сторону в сторону Ричарда надвигается огромный волк,а справой медведь и тогда Ричард думает что всё,конец настал.',color_code_red))
    sleep(2)


def act18_2():
    print(bordered('Но в этот момент волк и медведь перестают замечать Ричарда и повернув голову назад Ричард видит что позади него стоит Мерлин со своей волшебной мантией которая имеет способность, всех кто находится под ней делать невидимыми.',color_code_red))
    sleep(2)
    print(bordered('И тогда под эффектом невидимости Ричард и Мерлин крадут посох и убегают.',color_code_yellow))
    sleep(2)
    print(bordered('Как раз пока шёл бой, вход в подземелье открылся и друзья без проблем выбрались оттуда.',color_code_green))
    sleep(2)
def theend():
    print(bordered('TO BE CONTINUATION',color_code_purple))














