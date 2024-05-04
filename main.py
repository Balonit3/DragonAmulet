from hero import (Hero, start_history,
                  Enemy, Gost, NPC,
                  act1, act2, act3, act4,
                  act4_1,act5,act6,act7,act8,act9,
                  act10,act10_1,act10_2,BowWomen,act10_3,act10_4,
                  act11,act12,act13,act14,act15,act16,act17,act18,RedEyes,act18_1,act18_2,theend)

knight = Hero('Ричард', 90, 60, 30, 75, 'меч')
dragon = Hero('Беззубик', 200, 150, 50, 110, 'огонь')
gnom = Enemy('Тройняшки', 30, 200, 10, 15, 'ножик', 'неть')
kentavr = Hero('Джо', 140, 70, 30, 60, 'бутылка пива')
kislota_drakon = Enemy('Viper', 210, 120, 65, 110, 'кислота', 'ядерная слизь')
gost = Gost('Каспер', 180, 180, 100, 180, 'эктоплазма', 'крик')
blacksmith = NPC('Кузнец Валера', 'Болтовня')
bowwomen = BowWomen('Летисия',90,65,50,85,'лук','быстрая стрельба')
REDEYES = RedEyes('красный глаз','120',70,35,90,'лапы','раздвоение')


start_history()
knight.print_info()
act1()
gnom.print_info()
finish = knight.is_attack(gnom)
knight.lvl_up()

if finish:
    act2()
    kentavr.print_info()
    kentavr.strike(knight)
    knight.print_info()

    act3()
    act4()
    kislota_drakon.print_info()
    act4_1()
    kislota_drakon.apply_skill()
    knight.viper_pivo()
    act5()
    #починить меч
    act6()
    act7()
    act8()
    act9()
    act10()
    gost.print_info()
    act10_1()
    gost.apply_skill()
    act10_2()
    bowwomen.print_info()
    act10_3()
    bowwomen.apply_skill()
    act10_4()
    act11()
    act12()
    act13()
    act14()
    act15()
    act16()
    act17()
    act18()
    REDEYES.print_info()
    REDEYES.strike(knight)
    act18_1()
    REDEYES.apply_skill()
    act18_2()
    theend()


