from hero import Hero,start_history
knight = Hero('Ричард',90,60,75,'меч')
dragon = Hero('Беззубик',200,150,110,'огонь')
gnom = Hero('Тройняшки',30,200,10,'ножик')
kintavr = Hero('Джо',140,70,65,'бутылка пива')
kislota_drakon = Hero('Viper',210,120,110,'кислота')
#знакомство с Ричардом
knight.print_info()
start_history()
#появление тройняшек(гномов)
gnom.print_info()
#битва тройняшек с Ричардом
gnom.strike(knight)
knight.strike(gnom)
#знакомство с Джо(кинтавр)
kintavr.print_info()
#бой Джо с Ричардом
kintavr.strike(knight)
knight.strike(kintavr)
#знакомство с viper
kislota_drakon.print_info()
#бой Ричарда с viper
knight.strike(kislota_drakon)
kislota_drakon.strike(knight)