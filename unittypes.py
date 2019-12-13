# функции, возвращающие то, что зависит от персонажа
# Всех новых персонажей предлагается записывать сюда через elif
# FIXME придумайте персонажей!!!!

from tkinter import*


def cost(unit_type):
    """Стоимость"""
    if unit_type == "Rogue":
        return 1
    if unit_type == "Knight":
        return 1
    if unit_type == "Mage":
        return 1
    if unit_type == "Necromancer":
        return 1


def attack(unit_type):
    if unit_type == "Rogue":
        image = ['C:\Users\Artem\conformation\PNG\Rogue\Attack\Attack1.png', 'C:\Users\Artem\conformation\PNG\Rogue\Attack\Attack2.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Attack\Attack3.png','C:\Users\Artem\conformation\PNG\Rogue\Attack\Attack4.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Attack\Attack5.png','C:\Users\Artem\conformation\PNG\Rogue\Attack\Attack6.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Attack\Attack7.png']
    if unit_type == "Knight":
        image = ['C:\Users\Artem\conformation\PNG\Knight\Attack\ attack0.png', 'C:\Users\Artem\conformation\PNG\Knight\Attack\ attack1.png',
                 'C:\Users\Artem\conformation\PNG\Knight\Attack\ attack2.png','C:\Users\Artem\conformation\PNG\Knight\Attack\ attack4.png']
    if unit_type == "Mage":
        image = ['C:\Users\Artem\conformation\PNG\Mage\Attack\ attack1.png','C:\Users\Artem\conformation\PNG\Mage\Attack\ attack2.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Attack\ attack3.png','C:\Users\Artem\conformation\PNG\Mage\Attack\ attack4.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Attack\ attack5.png', 'C:\Users\Artem\conformation\PNG\Mage\Attack\ attack6.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Attack\ attack7.png']
    if unit_type == "Necromancer":
        image = ['C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_Attack_1.png', 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_Attack_2.png',
                 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_Attack_3.png', 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_Attack_4.png']
    if unit_type == "Overseer":
        image = ['C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_attack1.png','C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_attack2.png',
                 'C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_attack3.png','C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_attack4.png']
    if unit_type == "Elemental":
        image == ['C:\Users\Artem\conformation\ 3 Elemental\Elemental_attack_1.png',
                  'C:\Users\Artem\conformation\ 3 Elemental\Elemental_attack_2.png',
                  'C:\Users\Artem\conformation\ 3 Elemental\Elemental_attack_3.png',
                  'C:\Users\Artem\conformation\ 3 Elemental\Elemental_attack_4.png',
                  'C:\Users\Artem\conformation\ 3 Elemental\Elemental_attack_5.png',
                  'C:\Users\Artem\conformation\ 3 Elemental\Elemental_attack_6.png']
    return image


def death(unit_type):
    if unit_type == "Rogue":
        image = ['C:\Users\Artem\conformation\PNG\Rogue\Death\death1.png','C:\Users\Artem\conformation\PNG\Rogue\Death\death2.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Death\death3.png','C:\Users\Artem\conformation\PNG\Rogue\Death\death4.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Death\death5.png','C:\Users\Artem\conformation\PNG\Rogue\Death\death6.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Death\death7.png','C:\Users\Artem\conformation\PNG\Rogue\Death\death8.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Death\death9.png','C:\Users\Artem\conformation\PNG\Rogue\Death\death10.png']
    if unit_type == "Knight":
        image = ['C:\Users\Artem\conformation\PNG\Knight\Death\death1.png','C:\Users\Artem\conformation\PNG\Knight\Death\death2.png',
                 'C:\Users\Artem\conformation\PNG\Knight\Death\death3.png','C:\Users\Artem\conformation\PNG\Knight\Death\death4.png',
                 'C:\Users\Artem\conformation\PNG\Knight\Death\death5.png','C:\Users\Artem\conformation\PNG\Knight\Death\death6.png',
                 'C:\Users\Artem\conformation\PNG\Knight\Death\death7.png','C:\Users\Artem\conformation\PNG\Knight\Death\death8.png',
                 'C:\Users\Artem\conformation\PNG\Knight\Death\death9.png','C:\Users\Artem\conformation\PNG\Knight\Death\death10.png']
    if unit_type == "Mage":
        image = ['C:\Users\Artem\conformation\PNG\Mage\Death\death1.png','C:\Users\Artem\conformation\PNG\Mage\Death\death2.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Death\death3.png','C:\Users\Artem\conformation\PNG\Mage\Death\death4.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Death\death5.png','C:\Users\Artem\conformation\PNG\Mage\Death\death6.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Death\death7.png', 'C:\Users\Artem\conformation\PNG\Mage\Death\death8.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Death\death9.png', 'C:\Users\Artem\conformation\PNG\Mage\Death\death10.png']
    if unit_type == "Necromancer":
        image = ['C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_death1.png', 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_death2.png',
                 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_death3.png', 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_death4.png',
                 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_death5.png', 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_death6.png']
    if unit_type == "Overseer":
        image = ['C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_death1.png','C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_death2.png',
                 'C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_death3.png','C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_death4.png',
                 'C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_death6.png']
    if unit_type == "Elemental":
        image = ['C:\Users\Artem\conformation\ 3 Elemental\Elemental_death_1.png','C:\Users\Artem\conformation\ 3 Elemental\Elemental_death_2.png',
                 'C:\Users\Artem\conformation\ 3 Elemental\Elemental_death_3.png','C:\Users\Artem\conformation\ 3 Elemental\Elemental_death_4.png',
                 'C:\Users\Artem\conformation\ 3 Elemental\Elemental_death_5.png', 'C:\Users\Artem\conformation\ 3 Elemental\Elemental_death_6.png',]
    return image



def walk(unit_type):
    if unit_type == "Rogue":
        image = ['C:\Users\Artem\conformation\PNG\Rogue\Walk\walk1.png','C:\Users\Artem\conformation\PNG\Rogue\Walk\walk2.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Walk\walk3.png','C:\Users\Artem\conformation\PNG\Rogue\Walk\walk4.png',
                 'C:\Users\Artem\conformation\PNG\Rogue\Walk\walk5.png','C:\Users\Artem\conformation\PNG\Rogue\Walk\walk6.png']
    if unit_type == "Knight":
        image = ['C:\Users\Artem\conformation\PNG\Knight\Walk\walk1.png','C:\Users\Artem\conformation\PNG\Knight\Walk\walk2.png',
                 'C:\Users\Artem\conformation\PNG\Knight\Walk\walk3.png','C:\Users\Artem\conformation\PNG\Knight\Walk\walk4.png',
                 'C:\Users\Artem\conformation\PNG\Knight\Walk\walk5.png','C:\Users\Artem\conformation\PNG\Knight\Walk\walk6.png']
    if unit_type == "Mage":
        image = ['C:\Users\Artem\conformation\PNG\Mage\Walk\walk1.png', 'C:\Users\Artem\conformation\PNG\Mage\Walk\walk2.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Walk\walk3.png', 'C:\Users\Artem\conformation\PNG\Mage\Walk\walk4.png',
                 'C:\Users\Artem\conformation\PNG\Mage\Walk\walk5.png','C:\Users\Artem\conformation\PNG\Mage\Walk\walk6.png']
    if unit_type == "Necromancer":
        image = ['C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_walk1.png', 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_walk2.png',
                 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_walk3.png','C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_walk4.png',
                 'C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_walk5.png','C:\Users\Artem\conformation\ 1 Necromancer\Necromancer_walk6.png']
    if unit_type == "Overseer":
        image = ['C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_walk1.png','C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_walk2.png',
                 'C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_walk3.png','C:\Users\Artem\conformation\ 2 Mega_Beholder\MegaBeholder_walk4.png',]
    if unit_type == "Elemental":
        image = ['C:\Users\Artem\conformation\ 3 Elemental\Elemental_walk_1.png','C:\Users\Artem\conformation\ 3 Elemental\Elemental_walk_2.png',
                 'C:\Users\Artem\conformation\ 3 Elemental\Elemental_walk_3.png','C:\Users\Artem\conformation\ 3 Elemental\Elemental_walk_4.png',]
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


def money_cost(unit_type):
    if unit_type == "Rogue":
        return 0
    if unit_type == "Knight":
        return 0
    if unit_type == "Mage":
        return 0
    if unit_type == "Necromancer":
        return 0
    if unit_type == "Overseer":
        return 0
    if unit_type == "Elemental":
        return 0
def x(unit_type):
    if unit_type == "":
        x = 0
    return x


def additional_mana(unit_type):
    if unit_type == "":
        additional_mana = 0
    return additional_mana


def additional_money(unit_type):
    if unit_type == "":
        additional_money = 0
    return additional_money


# etc.
