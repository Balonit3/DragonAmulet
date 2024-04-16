from hero import Hero, start_history, Enemy, Gost, NPC, act1, act2

knight = Hero('Ричард', 90, 60, 75, 'меч')
dragon = Hero('Беззубик', 200, 150, 110, 'огонь')
gnom = Hero('Тройняшки', 30, 200, 10, 'ножик')
kintavr = Hero('Джо', 140, 70, 65, 'бутылка пива')
kislota_drakon = Enemy('Viper', 210, 120, 110, 'кислота', 'ядерная слизь')
gost = Gost('Каспер', 180, 180, 180, 'эктоплазма', 'крик')

blacksmith = NPC('Кузнец Валера', 'Болтовня')

start_history()
knight.print_info()
act1()
gnom.print_info()
finish = knight.is_attack(gnom)
knight.lvl_up()

if finish:
    act2()
    kintavr.print_info()

# kislota_drakon.print_info()
# kislota_drakon.apply_skill()
#
# gost.print_info()
# gost.invisible()

# # знакомство с Ричардом
# knight.print_info()
# start_history()
# # появление тройняшек(гномов)
# gnom.print_info()
# # битва тройняшек с Ричардом
# gnom.strike(knight)
# knight.strike(gnom)
# # знакомство с Джо(кинтавр)
# kintavr.print_info()
# # бой Джо с Ричардом
# kintavr.strike(knight)
# knight.strike(kintavr)
# # знакомство с viper
# kislota_drakon.print_info()
# # бой Ричарда с viper
# knight.strike(kislota_drakon)
# kislota_drakon.strike(knight)

'''


'''
