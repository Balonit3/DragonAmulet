from time import sleep


def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветсвтуйте героя ->', self.name)
        sleep(1)
        print('Уровень здоровья:', self.health)
        sleep(1)
        print('Класс брони:', self.armor)
        sleep(1)
        print('Сила удара:', self.power)
        sleep(1)
        print('Оружие:', self.weapon)
        sleep(1)
        print(' ')

    def strike(self, enemy):
        print('Удар', self.name, 'атакует', enemy.name, 'силой', self.power, 'используя', self.weapon, '\n')
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

    def strike_gnom(self, enemy_gnom):
        print('Удар', self.name, 'атакует', enemy_gnom.name, 'силой', self.power, 'используя', self.weapon, '\n')
        enemy_gnom.armor -= self.power
        if enemy_gnom.armor < 0:
            enemy_gnom.health += enemy_gnom.armor
            enemy_gnom.armor = 0
        print(enemy_gnom.name, 'получил удар\nкласс брони упал', enemy_gnom.armor, 'Уровень здоровья упал',
              enemy_gnom.health, '\n')

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

    def fight_Jo(self, enemy_JO):
        while self.health > 0 and enemy_JO.health > 0:
            self.strike(enemy_JO)
            if enemy_JO.health <= 0:
                print(enemy_JO.name, 'пал в бою!!!!\n')
                break
            sleep(5)
            enemy_JO.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в бою!!!!\n')
                break
            sleep(5)

    def fight_viper(self, enemy_kislota):
        while self.health > 0 and enemy_kislota.health > 0:
            self.strike(enemy_kislota)
            if enemy_kislota.health <= 0:
                print(enemy_kislota.name, 'пал в бою!!!!\n')
                break
            sleep(5)
            enemy_kislota.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в бою!!!!\n')
                break
            sleep(5)


def start_history():
    print(bordered('история Ричарда началась когда его отец не мало известный рыцарь погиб от лап дракона,'))
    sleep(2)
    print(bordered('Ричарду на тот момент было 5 лет и с тех пор он решил,что он должен отомстить.'))
    sleep(2)
    print(bordered('И вот шли годы на протяжении всего этого времени он тренировался не покладая рук.'))
    sleep(2)
    print(bordered('И вот с той трагедии прошло 12 лет и Ричард решил,что время мести настало.'))
    sleep(2)
    print(
        bordered('Ричард двинулся в путь и пройдя через реки и поля он наконец то подходит к следующему припядствию. '))
    sleep(2)
    print(bordered(
        'Это был тёмный и мрачный лес.Ричарду было страшно в него заходить,но он вспомнил про свою цель и не задумываясь вступил в него.'))
    sleep(2)
    print(bordered(
        'И вот пройдя уже по леса он подумал, что дальше будет также легко,он даже удивился почему этот лес все так боялись.'))
    sleep(2)
    print(bordered(
        'Но вдруг из гущи леса на него выбегают 3 гнома которые требуют с него 3 золотые монеты,либо они его убьют.'))
    sleep(2)
    print(bordered('Он не растерялся и с помощью своего меча отрубил 3 головы сразу.'))
    sleep(2)
    print(bordered('После этой непростой битвы он решил расслабиться и пойти в бар к кинтавру Джо.'))
    sleep(2)
    print(bordered('Но по скольку этот лес не простой вместо желанной бутылочки пивчанского он получил суровый бой.'))
    sleep(2)
    print(bordered('Джо не обладал сверх навыками но был готов дать отпор Ричарду за свой божественный напиток '))
    sleep(2)
    print(bordered('После этой схватки у Ричардо появился новый предмет как ПИВО,'))
    sleep(2)
    print(bordered(
        'это было зелье исцеление которое он мог выпить в любой следующей битве что бы восполнить своё здоровье '))
    sleep(2)
    print(bordered('Позже он двинулся на север в сторону города под названием АНОР ЛОНДО.'))
    sleep(2)
    print(bordered('Там он поченил свою броню у кузница и поел у бабушки Мери.'))
    sleep(2)
    print(bordered('После полноценного отдыха он решил продолжить свой путь.'))
    sleep(2)
    print(bordered('Его следующая цель была Долина Драконов.'))
    sleep(2)
    print(bordered('Кузнец ему рассказал что там обитает старый вид драконов который очень опасен из за своего яда.'))
    sleep(2)
    print(bordered('Но для ричарда его слова были лишь мотивацией пойти туда.'))
    sleep(2)
    print(bordered(
        'И вот спустя 3 дня непрерывной дороги он видит ущелье в котором очень странно светится ярко-зелёным цветом река и скалы.'))
    sleep(2)
    print(bordered(
        'Пройдя немного дальше он слышит громкий топот и сопение и повернув голову влево он видит его,того самого дракона про которого говорил кузнец.'))
    sleep(2)
    print(bordered(
        'Весь покрыт плотной чешуёй тёмно-зелёного цвета дракон идёт в сторону Ричарда и Ричард понимает что битвы не избежать.'))
    sleep(2)
    print(bordered(
        'И ричард делает первый рывок в его сторону и наносит своим мечом первый удар в зону живота,но из за плотной чешуи дракон не чувствует удара и атакует в ответ.'))
    sleep(2)
    print(bordered('выпустив свой яд, небольшая часть одежды Ричарда расщепляется.\n '))
    sleep(2)
