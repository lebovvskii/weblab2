
1) Выборка данных из связанных таблиц с условиями и сортировкой:

//Получить список задач (Tasks) с информацией о пользователях (Users) и категориях (Task Categories),
//отсортированный по статусу задачи и времени создания:
SELECT Tasks.task_id, Tasks.task_name, Tasks.status, Tasks.created_at, Users.username, TaskCategories.category_name
FROM Tasks
JOIN Users ON Tasks.user_id = Users.user_id
JOIN TaskCategories ON Tasks.category_id = TaskCategories.category_id
WHERE Tasks.status = 'In Progress'
ORDER BY Tasks.created_at DESC;


2) Запросы с группировкой и групповыми функциями:

//Получить количество задач по каждому пользователю:
SELECT Users.username, COUNT(Tasks.task_id) AS task_count
FROM Users
LEFT JOIN Tasks ON Users.user_id = Tasks.user_id
GROUP BY Users.username;

//Получить среднюю продолжительность работы (duration) в циклах Pomodoro по пользователям:
SELECT Users.username, AVG(PomodoroCycles.duration) AS avg_duration
FROM Users
LEFT JOIN PomodoroCycles ON Users.user_id = PomodoroCycles.user_id
GROUP BY Users.username;

3) Запросы со вложенными запросами или табличными выражениями:

//Получить задачи (Tasks) с максимальной продолжительностью по каждой категории (Task Categories):
SELECT Tasks.task_id, Tasks.task_name, Tasks.duration, TaskCategories.category_name
FROM Tasks
JOIN TaskCategories ON Tasks.category_id = TaskCategories.category_id
WHERE Tasks.duration = (SELECT MAX(duration) FROM Tasks WHERE category_id = TaskCategories.category_id);

//Получить пользователей (Users), у которых количество циклов Pomodoro больше среднего:
SELECT * FROM Users
WHERE user_id IN (
  SELECT user_id
  FROM PomodoroCycles
  GROUP BY user_id
  HAVING COUNT(pomodoro_id) > (SELECT AVG(cycles_count) FROM (SELECT user_id, COUNT(pomodoro_id) AS cycles_count FROM PomodoroCycles GROUP BY user_id));
);

4)Запросы корректировки данных (обновление, добавление, удаление):

//Обновление данных:

UPDATE Tasks SET status = 'Completed' WHERE task_id = 1;

//Добавление данных:
INSERT INTO TaskCategories (category_id, category_name, category_description) VALUES (11, 'NewCategory', 'Description of NewCategory');

//Удаление данных:
DELETE FROM Tasks WHERE task_id = 2;

