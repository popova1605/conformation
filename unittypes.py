# функции, возвращающие то, что зависит от персонажа
# Всех новых персонажей предлагается записывать сюда через elif
# FIXME придумайте персонажей!!!!

from tkinter import*


def cost(unit_type):
    """Стоимость"""
    if unit_type == "rogue":
        return 1


def attack(unit_type):
    """Объект картинки на карте"""
    if unit_type == "rogue":
        image = []
    return image


def death(unit_type):
    if unit_type == "rogue":
        image = []
    return image


def walk(unit_type):
    if unit_type == "rogue":
        image = ['rogue_run_1_0.png', 'rogue_run_1_1.png', 'rogue_run_1_2.png', 'rogue_run_1_3.png']
    return image


def card(unit_type):
    if unit_type == "rogue":
        image = 0
    return image


def health(unit_type):
    if unit_type == "rogue":
        health = 0
    return health


def force(unit_type):
    if unit_type == "rogue":
        force = 0
    return force


def step(unit_type):
    if unit_type == "":
        step = 500
    return step


def money_cost(unit_type):
    if unit_type == "":
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
