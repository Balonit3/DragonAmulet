from hero import (Hero, start_history,
                  Enemy, Gost, NPC,
                  act1, act2, act3, act4,
                  act4_1,)

knight = Hero('Ричард', 90, 60, 30, 75, 'меч')
dragon = Hero('Беззубик', 200, 150, 50, 110, 'огонь')
gnom = Enemy('Тройняшки', 30, 200, 10, 15, 'ножик', 'неть')
kentavr = Hero('Джо', 140, 70, 30, 60, 'бутылка пива')
kislota_drakon = Enemy('Viper', 210, 120, 65, 110, 'кислота', 'ядерная слизь')
gost = Gost('Каспер', 180, 180, 100, 180, 'эктоплазма', 'крик')

blacksmith = NPC('Кузнец Валера', 'Болтовня')

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
    knight.viper_pivo()
    kislota_drakon.apply_skill()
