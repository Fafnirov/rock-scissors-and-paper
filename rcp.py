# rcp.py
# Очень простая версия "Камень-Ножницы-Бумага"

import random
import sys

MOVES = ("камень", "ножницы", "бумага") #константа (кортеж) с допустимыми ходами
SHORT = {"к": "камень", "н": "ножницы", "б": "бумага"} #Словарь, дебич, чекай ниже.

def get_move(prompt="Твой ход (камень/ножницы/бумага или к/н/б, q чтобы выйти): "): #объявление функции get_move!!!!!!!!!! принимает необязательный параметр prompt (строка приглашения типа).
    s = input(prompt).strip().lower()
    if s in ("q", "quit", "exit"):
        print("Пока!")
        sys.exit(0)
    return SHORT.get(s, s)  # если сокращение — переводим, иначе возвращаем как есть

def decide(p, c):
    if p == c:
        return "ничья"
    if (p, c) in (("камень","ножницы"), ("ножницы","бумага"), ("бумага","камень")):
        return "игрок"
    return "компьютер"

def main():
    print("Камень-Ножницы-Бумага — простая версия")
    while True:
        player = get_move()
        if player not in MOVES:
            print("Непонятно, попробуй: камень/ножницы/бумага")
            continue
        comp = random.choice(MOVES)
        print("Компьютер:", comp)
        winner = decide(player, comp)
        if winner == "ничья":
            print("Ничья")
        elif winner == "игрок":
            print("Ты выиграл!")
        else:
            print("Компьютер выиграл.")
        print()  # пустая строка для читаемости

if __name__ == "__main__":
    main()
