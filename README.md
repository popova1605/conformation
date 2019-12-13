#

Программа состоит из модулей:

1. main \n
Отвечает за начало и завершение игры.
Функции:
1.1 main
Запускает игру.
1.2 new_game
Запускает новую игру, обновляет параметры игры.
1.3 new_turn
Отвечает за чередование ходов игроков. Выполняет проверку на то, закончилась ли игра, и если закончилась, выдает
сообщение о том, кто победил.
1.4 finish
Завершает игру, удаляет все с канваса.

2. mathematical parametrs
2.1 class Player
Поля: номер игрока, мана, деньги и здоровье.
2.2 class Game
Класс, содержащий параметры текущей игры.
Поля: номер игрока, который сейчас ходит, список игроков, кол-во денег у каждого игрока в начале хода, мана,
добавляемая игроку перед его ходом.
Функции:
2.2.1 инициализация игры
2.2.2 end_turn
Завершает ход, обновляет параметры игрока.
2.2.3 check_fail
Проверяет, не закончилась ли игра на текущем ходе.

3. field
3.1 class Buttle_field
Класс игрового поля.
Поля: размер поля, массив дорожек, содержащихся на поле, объекты надписей на канвасе.
Функции:
3.1.1 инициализация поля
3.1.2 move_roads
Вызывает функцию движения для каждого персонажа на всех дорожках. Проводит проверку на поражение.
3.1.3 set_parametrs
Изменяет значения text денег и/или маны для одного из двух игроков на значения, содержащиеся в экземпляре класса Game.
3.1.4 set_players_parametrs
Изменяет значения text денег и/или маны для одного из двух игрков на значения, содержащиеся в экземпляре класса Player.
3.2 class Road
Класс дорожек.
Поля: списки персонажей, находящихся на дорожке, рисунок последней положенной карты, координату y центра дорожки и
ее ширину.
Функции:
3.2.1 инициализация дорожки
3.2.2 move_units
Вызов move для всех персонажей на дорожке. Проверка на факт встречи с вражескими персонажами. В случае встречи вызов
функции fight и удаление проигравших персонажей с дорожки.
3.2.3 catch_card
Добавление новой карты на дорожку. Смена изображения последней положенной карты. Создание соответствующего карте
персонажа.

4. units
4.1 class Unit
Класс персонажей.
Поля: тип персонажа, сила, здоровье, изображение.
Функции:
4.1.1 инициализация персонажа
4.1.2 move
Движение персонажа. Один его шаг.
4.1.3 ex_animation
Функция анимации персонажа. Прописаны его движения.
4.1.4 win
Анимация персонажа, которая активируется при его победе.
4.1.5 kill
Анимация смерти персонажа, потерявшего все здоровье.
4.1.6 attak
анимация атаки
4.1.7 die
удаление персонажа
4.2 Функция fight
Анимирует драку персонажей и меняет их здоровье. Возвращает список проигравших персонажей. Если таких нет, то
вызывается рекурсивно.

5. unittypes
Модуль функций, возвращающих разные параметры в зависимости от типа персонажа.
Функции:
5.1 cost
возвращает стоимость персонажа
5.2 attack
возвращает анимацию движения персонажа
5.3 death
возвращает анимацию смерти персонажа
5.4 walk
возвращает анимацию ходьбы персонажа
5.6 card
возвращает изображение карты персонажа
5.7 health
возвращает здоровье персонажа
5.8 force
возвращает убойную силу персонажа
5.9 step
возвращает длину шага персонажа

6. decks_and_cards
6.1 class Deck
класс колоды
6.1.1 инициализация колоды
6.1.2 is_clicked
проверка попадания мыши по колоде
6.1.3 create_card
Создание карты данной колодой. Привязка move к движению курсора. Привязка find_road к отпусканию кнопки мыши.
6.2 class Card
6.2.1 инициализация карты
6.2.2 move
Движение карты по экрану с учетом запрета на выход за границы поля и на чужое поле.
6.2.3 find_road
Подбор дорожки по месту отпускания карты. Отвязывает мышь. Карта умирает, если дорожки не нашлось.
6.2.4 hide
Удаляет изобажение с экрана без удаления объекта.
6.3 find_clicked_decks
находит колоду, на которую нажал игрок
6.4 active_decks
активация колоды

7. graphics
вся графика тут

8. fileinput
Реализует возможность сохранения игры и продолжения ее после закрытия с прежними параметрами.

9. testgr
модуль для тестироваия графики

10. move_test
модуль для тестирования движения
