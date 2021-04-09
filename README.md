# Список книг на лето

## Описание

Задача [Список книг на лето](https://stepik.org/lesson/243394/step/15)

Этим летом местная библиотека неожиданно столкнулась с потоком школьников, желающих взять некоторые книги из списка литературы. Чтобы не нагружать своих работников, руководство библиотеки решило создать электронную систему учета книг, которая бы показывала, какие книги есть в наличии. В библиотеке провели ревизию и записали в систему все книги. Когда очередной школьник пытается взять книгу, библиотекарь сначала проверяет, есть ли она в наличии. Если есть, книга временно удаляется из системы. У школьника есть один месяц, чтобы вернуть книгу. Вам поручили написать данную систему и протестировать ее на наборе смоделированных записей. Будем считать, что если школьник не вернул книгу в течение месяца, коллекторы, нанятые руководителем библиотеки, в день истечения срока самостоятельно изымают книгу.

## Данные

**Формат ввода:** программе сначала передается список книг через запятую, затем строки, описывающие поведение посетителей: строка вида\
`"Взять <книга> <дата> (<имя>)"`\
или\
`"Вернуть <книга> <дата>"`.\
Ввод происходит до точки.

> [!NOTE]
> Заметьте, что руководство библиотеки решило усложнить Вам задачу, и записи передаются не в хронологическом порядке. 

**Формат вывода:** после того, как посетитель взял книгу, необходимо вывести\
`"Книгу <книга> забрал(а) <имя>"`.\
Если данной книги нет, выведите\
`"Книга <книга> отсутствует. Ее забрал(а) <имя>"`.

## Примечание
  
- Если школьник взял книгу k-го числа n-го месяца, то гарантируется, что k-ый день (n + 1)-го месяца - это корректная дата.
- Гарантируется отсутствие неверных данных, подаваемых на вход. Например:
  - не возвращаются книги, которые не были взяты,
  - не возвращаются/не забираюся книги, которых не в списке
  - действие возврата книги коллекторами не добавляет действие возврата в список действий

## Особенности

Модуль `datetime` не используется, так как пока не изучался в этом курсе.

## Пример

*Sample Input:*

"Эдем", "Солярис", "Война и мир", "Честь имею", "Ночной дозор", "Оно"\
Взять "Честь имею" 03.08.2019 (Карл)\
Взять "Оно" 23.07.2019 (Джейн)\
Взять "Война и мир" 28.09.2019 (Наташа)\
Взять "Война и мир" 01.10.2019 (Сергей)\
Взять "Ночной дозор" 27.07.2019 (Дмитрий)\
Взять "Солярис" 02.08.2019 (Джейн)\
Вернуть "Честь имею" 10.08.2019\
Взять "Солярис" 01.08.2019 (Саймон)\
Взять "Ночной дозор" 28.08.2019 (Сергей)\
Взять "Оно" 21.07.2019 (Саймон)\
Вернуть "Солярис" 29.07.2019\
Взять "Эдем" 29.09.2019 (Наташа)\
Вернуть "Война и мир" 30.09.2019\
Взять "Эдем" 02.10.2019 (Саймон)\
Вернуть "Ночной дозор" 26.08.2019\
Взять "Солярис" 19.07.2019 (Карл)\
Взять "Оно" 22.08.2019 (Джейн)\
.

*Sample Output:*

Книгу "Солярис" забрал(а) Карл\
Книгу "Оно" забрал(а) Саймон\
Книга "Оно" отсутствует. Ее забрал(а) Саймон\
Книгу "Ночной дозор" забрал(а) Дмитрий\
Книгу "Солярис" забрал(а) Саймон\
Книга "Солярис" отсутствует. Ее забрал(а) Саймон\
Книгу "Честь имею" забрал(а) Карл\
Книгу "Оно" забрал(а) Джейн\
Книгу "Ночной дозор" забрал(а) Сергей\
Книгу "Война и мир" забрал(а) Наташа\
Книгу "Эдем" забрал(а) Наташа\
Книгу "Война и мир" забрал(а) Сергей\
Книга "Эдем" отсутствует. Ее забрал(а) Наташа
