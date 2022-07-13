from game.enemy import Enemy

e = Enemy(
    "Охраник", 
    '''Этот охранник родился в семье кузнеца и очень хорошо разбирается в оружии и людях,
    он благосклонно относится к бравым поступкам и отрицательно к воровству и преступлениям закона.
    ''',
    "sentiel_dialog.log",
    "sentiel_fight.log",
    "sentiel_sneak.log")

e.start_interaction()
