from tkinter import*

def cost(unit_type):
    """Стоимость"""
    if unit_type == "Rogue":
        return 1
    if unit_type == "Knight":
        return 5
    if unit_type == "Mage":
        return 7
    if unit_type == "Necromancer":
        return 1
    if unit_type == "Overseer":
        return 5
    if unit_type == "Elemental":
        return 7


def attack(unit_type):
    if unit_type == "Rogue":
        image = ['PNG\Rogue\Attack\Attack1.png', 'PNG\Rogue\Attack\Attack2.png',
                 'PNG\Rogue\Attack\Attack3.png','PNG\Rogue\Attack\Attack4.png',
                 'PNG\Rogue\Attack\Attack5.png','PNG\Rogue\Attack\Attack6.png',
                 'PNG\Rogue\Attack\Attack7.png']
    if unit_type == "Knight":
        image = ['PNG\Knight\Attack\Attack0.png', 'PNG\Knight\Attack\Attack1.png',
                 'PNG\Knight\Attack\Attack2.png','PNG\Knight\Attack\Attack4.png']
    if unit_type == "Mage":
        image = ['PNG\Mage\Attack\Attack1.png','PNG\Mage\Attack\Attack2.png',
                 'PNG\Mage\Attack\Attack3.png','PNG\Mage\Attack\Attack4.png',
                 'PNG\Mage\Attack\Attack5.png', 'PNG\Mage\Attack\Attack6.png',
                 'PNG\Mage\Attack\Attack7.png']
    if unit_type == "Necromancer":
        image = ['Necromancer\ecromancer_Attack_1.png', 'Necromancer\ecromancer_Attack_2.png',
                 'Necromancer\ecromancer_Attack_3.png', 'Necromancer\ecromancer_Attack_4.png']
    if unit_type == "Overseer":
        image = ['Mega_Beholder\MegaBeholder_attack1.png','Mega_Beholder\MegaBeholder_attack2.png',
                 'Mega_Beholder\MegaBeholder_attack3.png','Mega_Beholder\MegaBeholder_attack4.png']
    if unit_type == "Elemental":
        image = ['Elemental\Elemental_attack_1.png',
                  'Elemental\Elemental_attack_2.png',
                  'Elemental\Elemental_attack_3.png',
                  'Elemental\Elemental_attack_4.png',
                  'Elemental\Elemental_attack_5.png',
                  'Elemental\Elemental_attack_6.png']
    return image


def death(unit_type):
    if unit_type == "Rogue":
        image = ['PNG\Rogue\Death\death1.png','PNG\Rogue\Death\death2.png',
                 'PNG\Rogue\Death\death3.png','PNG\Rogue\Death\death4.png',
                 'PNG\Rogue\Death\death5.png','PNG\Rogue\Death\death6.png',
                 'PNG\Rogue\Death\death7.png','PNG\Rogue\Death\death8.png',
                 'PNG\Rogue\Death\death9.png','PNG\Rogue\Death\death10.png']
    if unit_type == "Knight":
        image = ['PNG\Knight\Death\death1.png','PNG\Knight\Death\death2.png',
                 'PNG\Knight\Death\death3.png','PNG\Knight\Death\death4.png',
                 'PNG\Knight\Death\death5.png','PNG\Knight\Death\death6.png',
                 'PNG\Knight\Death\death7.png','PNG\Knight\Death\death8.png',
                 'PNG\Knight\Death\death9.png','PNG\Knight\Death\death10.png']
    if unit_type == "Mage":
        image = ['PNG\Mage\Death\death1.png','PNG\Mage\Death\death2.png',
                 'PNG\Mage\Death\death3.png','PNG\Mage\Death\death4.png',
                 'PNG\Mage\Death\death5.png','PNG\Mage\Death\death6.png',
                 'PNG\Mage\Death\death7.png', 'PNG\Mage\Death\death8.png',
                 'PNG\Mage\Death\death9.png', 'PNG\Mage\Death\death10.png']
    if unit_type == "Necromancer":
        image = ['Necromancer\ecromancer_death1.png', 'Necromancer\ecromancer_death2.png',
                 'Necromancer\ecromancer_death3.png', 'Necromancer\ecromancer_death4.png',
                 'Necromancer\ecromancer_death5.png', 'Necromancer\ecromancer_death6.png']
    if unit_type == "Overseer":
        image = ['Mega_Beholder\MegaBeholder_death1.png','Mega_Beholder\MegaBeholder_death2.png',
                 'Mega_Beholder\MegaBeholder_death3.png','Mega_Beholder\MegaBeholder_death4.png',]
    if unit_type == "Elemental":
        image = ['Elemental\Elemental_death_1.png','Elemental\Elemental_death_2.png',
                 'Elemental\Elemental_death_3.png','Elemental\Elemental_death_4.png',
                 'Elemental\Elemental_death_5.png', 'Elemental\Elemental_death_6.png',]
    return image



def walk(unit_type):
    if unit_type == "Rogue":
        image = ['PNG\Rogue\Walk\walk1.png','PNG\Rogue\Walk\walk2.png',
                 'PNG\Rogue\Walk\walk3.png','PNG\Rogue\Walk\walk4.png',
                 'PNG\Rogue\Walk\walk5.png','PNG\Rogue\Walk\walk6.png']
    if unit_type == "Knight":
        image = ['PNG\Knight\Walk\walk1.png','PNG\Knight\Walk\walk2.png',
                 'PNG\Knight\Walk\walk3.png','PNG\Knight\Walk\walk4.png',
                 'PNG\Knight\Walk\walk5.png','PNG\Knight\Walk\walk6.png']
    if unit_type == "Mage":
        image = ['PNG\Mage\Walk\walk1.png', 'PNG\Mage\Walk\walk2.png',
                 'PNG\Mage\Walk\walk3.png', 'PNG\Mage\Walk\walk4.png',
                 'PNG\Mage\Walk\walk5.png','PNG\Mage\Walk\walk6.png']
    if unit_type == "Necromancer":
        image = ['Necromancer\ecromancer_walk1.png', 'Necromancer\ecromancer_walk2.png',
                 'Necromancer\ecromancer_walk3.png','Necromancer\ecromancer_walk4.png',
                 'Necromancer\ecromancer_walk5.png','Necromancer\ecromancer_walk6.png']
    if unit_type == "Overseer":
        image = ['Mega_Beholder\MegaBeholder_walk1.png','Mega_Beholder\MegaBeholder_walk2.png',
                 'Mega_Beholder\MegaBeholder_walk3.png','Mega_Beholder\MegaBeholder_walk4.png',]
    if unit_type == "Elemental":
        image = ['Elemental\Elemental_walk_1.png','Elemental\Elemental_walk_2.png',
                 'Elemental\Elemental_walk_3.png','Elemental\Elemental_walk_4.png',]
    return image


def card(unit_type):
    if unit_type == "Rogue":
        image = 0
    if unit_type == "Knight":
        image = 0
    if unit_type == "Mage":
        image = 0
    if unit_type == "Necromancer":
        image = 0
    if unit_type == "Overseer":
        image = 0
    if unit_type == "Elemental":
        image = 0
    return image


def health(unit_type):
    if unit_type == "Rogue":
        health = 0
    if unit_type == "Knight":
        health = 0
    if unit_type == "Mage":
        health = 0
    if unit_type == "Necromancer":
        health = 0
    if unit_type == "Overseer":
        health = 0
    if unit_type == "Elemental":
        health = 0
    return health


def force(unit_type):
    if unit_type == "Rogue":
        force = 0
    if unit_type == "Knight":
        force = 0
    if unit_type == "Mage":
        force = 0
    if unit_type == "Necromancer":
        force = 0
    if unit_type == "Overseer":
        force = 0
    if unit_type == "Elemental":
        rorce = 0
    return force


def step(unit_type):
    if unit_type == "Rogue":
        step = 0
    if unit_type == "Knight":
        step = 0
    if unit_type == "Mage":
        step = 0
    if unit_type == "Necromancer":
        step = 0
    if unit_type == "Overseer":
        step = 0
    if unit_type == "Elemental":
        step = 0
    return step
