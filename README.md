
1. ## Вводная часть
------------------------------------------------------------------------------------
Этот проект реализует алгоритм кластеризации DBSCAN с нуля.
Немного про DBSCAN. Для выполнения кластеризации DBSCAN, точки разделяются на главные,
соседние и шумы. Сама суть дбскан заключается в том, чтобы пройтись по всем точкам. Если точки достижимы друг из друга,
точки образуют один кластер. Но если нет - то тогда точка помечается как шум.

2. ## Документация
## DBSCAN - класс алгоритма дбскана

        DBScan(minpts, eps, x)
minpts - мин. кол-во соседей                                                     
eps - мин. дистанция между точек                                                         
x - сама дата

 ---------------------------------------------------------------------------------
 Ее методы:           
## '''neighbour'''
    neighbour()
Находит соседние точки для заданной точки.
Параметры:
p точка
Возвращает:
list: список соседних точек

## '''clustering'''
      clustering()
Выполняет кластеризацию данных.
Возвращает:
количество кластеров
## '''draw'''
      draw(count_cluster) 
Визуализирует кластеры.
Параметры:
count_cluster (int): количество кластеров

3. ## Пример использования
 ---------------------------
1. Загрузите файл с нужной вам датой(можете использвать ту которая есть в этом репозитории)
2. Загрузите DBScan.py 
3. Загрузите и зайдите в main.py
4. Отфильтруйте дату как показано на фотке
 ---------------------------
![изображение](https://github.com/user-attachments/assets/05da7e15-edb7-467c-a86f-668ddba3db06)
 ---------------------------
5. сохраните в переменную результат clustering()
6. пропишите метод draw() и запишите в нее переменную

## Примечание 
При исполнении кода может возникнуть данная ошибка
    ![Снимок экрана 2025-01-27 145459](https://github.com/user-attachments/assets/6efa480d-ea0b-4123-813f-f0202b2280cd)
Просто перезапустите код. Возникает она из-за подбора цвета для визуализации
## Итог
![изображение](https://github.com/user-attachments/assets/c5329a33-008c-4590-adea-eaf3b2037af7)
---------------------------
Распредилила нам на 3 класстра и совершило 1 выброс(помечаются крестиком)

