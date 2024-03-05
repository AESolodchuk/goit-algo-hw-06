## Завдання 1. Граф
Кількість вершин: 8 дорівнює кількості родичів
Кількість ребер: 11 дорівнює кількості зв'язків між родичами
Ступені вершин дорівнює кількості зв'язків кожного з родичів:
|Прадід|Дід|Бабуся|Мама|Батько|Дядько|Брат|Я|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
1|4|3|4|2|3|2|3|


## Завдання 2. Обход графа
DFS path: [('Прадід', 'Дід'), ('Дід', 'Бабуся'), ('Бабуся', 'Мама'), ('Мама', 'Батько'), ('Батько', 'Я'), ('Я', 'Брат'), ('Брат', 'Дядько')]
BFS path: [('Прадід', 'Дід'), ('Дід', 'Бабуся'), ('Дід', 'Мама'), ('Дід', 'Дядько'), ('Мама', 'Батько'), ('Мама', 'Я'), ('Дядько', 'Брат')]

Алгоритми BFS (пошук в ширину) та DFS (пошук в глибину) йдуть по різних шляхах через графи через їх різні способи обходу вершин. BFS та DFS мають різні стратегії обходу вершин. BFS спочатку відвідує всі сусідні вершини відносно поточної вершини, а потім переходить до наступного рівня вершин, тоді як DFS спускається "глибоко" в граф,\n відвідуючи всі вершини у поточному шляху, перш ніж повернутися назад. Отже, BFS та DFS йдуть по різних шляхах через графи через використання різних стратегій обходу вершин, і це призводить до різних порядків відвідування вершин'

## Завдання 3. алгоритм Дейкстри