# main.py

import sqlite3
from createDB import (
  CREATE_USERS_TABLE,
  CREATE_TASKS_TABLE,
  CREATE_TASK_CATEGORIES_TABLE,
  CREATE_POMODORO_CYCLES_TABLE,
  CREATE_USER_TASK_CATEGORY_TABLE,
  CREATE_USER_ROLES_TABLE,
)

from data import (
  users_data,
  tasks_data,
  task_categories_data,
  pomodoro_cycles_data,
  user_task_category_data,
  user_roles_data
)

# Создаем базу
conn = sqlite3.connect('task_management.db')
cursor = conn.cursor()

# Создаём таблицы
cursor.execute(CREATE_USERS_TABLE)
cursor.execute(CREATE_TASKS_TABLE)
cursor.execute(CREATE_TASK_CATEGORIES_TABLE)
cursor.execute(CREATE_POMODORO_CYCLES_TABLE)
cursor.execute(CREATE_USER_TASK_CATEGORY_TABLE)
cursor.execute(CREATE_USER_ROLES_TABLE)

cursor.executemany('''
    INSERT INTO Users (user_id, username, email, created_at, user_role_id)
    VALUES (?, ?, ?, ?, ?)
''', users_data)

cursor.executemany('''
    INSERT INTO Tasks (task_id, task_name, task_description, status, created_at, user_id, category_id)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', tasks_data)

cursor.executemany('''
    INSERT INTO TaskCategories (category_id, category_name, category_description)
    VALUES (?, ?, ?)
''', task_categories_data)

cursor.executemany('''
    INSERT INTO PomodoroCycles (pomodoro_id, user_id, start_time, end_time, duration, task_id)
    VALUES (?, ?, ?, ?, ?, ?)
''', pomodoro_cycles_data)

cursor.executemany('''
    INSERT INTO UserRoles (user_role_id, user_role_name)
    VALUES (?, ?)
''', user_roles_data)

# Закрываем соединение
conn.commit()
conn.close()
