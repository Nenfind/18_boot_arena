# # Arena

## Мини-проект "игра-арена"
Цель данной активности - получить удовольствие от применения ООП.

В результате выполнения у вас должна получиться мини-игра арена, на которую вы выпустите своих персонажей и заставите их сражаться между собой. Играющая сама в себя и выдающая вам только результат своей работы.

Если вы улучшите игру так, чтобы можно было влиять на игровой процесс не из кода(!), обязательно поделитесь, мы с удовольствием потестируем!

Для работы вам потребуется только среда разработки, через которую можно запускать код для выполнения. Подойдет тот же VSC или PyCharm, который ты уже используешьь :)

## Техническое задание
Программа должна иметь следующие классы и функции:

* Вещи: `class Thing` Класс содержит в себе следующие параметры - название, процент защиты, атаку и жизнь; Это могут быть предметы одежды, магические кольца, всё что угодно)

* Персонаж: `class Person` Класс, содержащий в себе следующие параметры:
1. Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
2. Метод, принимающий на вход список вещей `set_things(things)`;
3. Метод вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;

* Паладин: `class Paladin` Класс наследуется от персонажа, при этом количество присвоенных жизней и процент защиты умножается на 2 **в конструкторе**;

Воин: `class Warrior` Класс наследуется от персонажа, при этом атака умножается на 2 **в конструкторе**.

## Алгоритм проведения боя:
- Шаг 1 - создаем произвольное количество вещей с различными параметрами, процент защиты не должен превышать 10%(0.1). Сортируем по проценту защиты, по возрастанию;

- Шаг 2 - создаем произвольно 10 персонажей, кол-во воинов и паладинов произвольно. Имена персонажам тоже рандомные из созданного списка 20 имен. Придумайте своих уникальных персонажей или заставьте сражаться знаменитостей, посмотрим кто сильнее =)

- Шаг 3 - одеваем персонажей рандомными вещами. Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;

- Шаг 4 - отправляем персонажей на арену, и в цикле в произвольном порядке выбирается пара Нападающий и Защищающийся.

У Защищающегося вызывается метод вычитания жизни на основе атаки `attack_damage` Нападающего.
Количество получаемого урона рассчитывается по формуле: `attack_damage - attack_damage * final_protection`
Общий процент защиты `final_protection` вычисляется по формуле `базовый процент защиты + процент защиты от всех надетых вещей`
Жизнь вычитается по формуле `hit_points - (attack_damage - attack_damage*final_protection)`, где `final_protection` - коэффициент защиты в десятичном виде;
Цикл идет до тех пор, пока не останется последнего выжившего. Как только кол-во жизней меньше или равно 0, персонаж удаляется из арены (списка). Для отслеживания процесса битвы выведите информацию в таком виде: `{атакующий персонаж} наносит удар по {защищающийся персонаж} на {кол-во урона} урона`.

## Критерии оценки:
* Работоспособность программы (если не работает программа, то выйти на 1 место возможно лишь в том случае, если у всех команд будут музейные экспонаты).
* Соответствие программы условиям задания, корректность работы алгоритма
* Структура проекта (размещение классов, использование констант, enum и т.п.)
* Оформление (соответствие PEP8, PEP257 и т.п.). Помним, что разработчик не писатель, а в первую очередь читатель.
* Использование системы контроля версий.
* Расширение функционала программы (не обязательно)
  
**Идеи по расширению:**
- Игрок против компьютера (возможно, это выбор персонажей или выбор конкретных предметов на бой)
- Подсветить разными цветами разные события, используем, например, `colorama`
- Добавить 3 расу, например, эльфов
- Интегрировать игру в Django (самое простое - отдавать результаты случайной игры на странице, чуть сложнее - пусть пользователь создаст своего персонажа, и он поучаствует в битве)

## Как правильно выполнять и отправлять задание на проверку:
* Капитан команды (да, вам надо выбрать капитана) форкает себе этот репозиторий.
* Капитан команды предоставляет доступ к своему репозиторию второму участнику команды.
* Каждый создает свою собственную feature-ветку, в которой пишет код (можно несколько веток, если это посчитаете целесообразным).
* Не стесняйтесь делать коммиты, когда считаете, что нужно зафиксировать какие-то опеределенные изменения.
* Сливать все изменения желательно через создание pull-request. Это позволит еще раз чекнуть то, что сделано и проверить на наличие ошибок.

## Хаки для хакатона
- Руки помнят, а линтеры напоминают.
- Даже для того, чтобы описать мычание требуется не меньше двух букв.
- Не позволяй модифицировать немодифицируемое.
- Чукча - читатель.
- Разваливающаяся Лада доставит в пункт назначения быстрее Мерседеса с заклинившим движком.

Успехов!

P.S. В задании описаны только основные моменты функционала программы. Как все это реализовать, и какие инструменты использовать - решать вам. Ограничений на полет вашей фантазии здесь нет, так что дерзайте! =) P.P.S. А еще можно добавить немного истории вашей любимой игровой вселенной или выдумать полностью свою. Это не обязательно, но вдруг вам захочется ;)
