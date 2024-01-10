# createDB.py

CREATE_USERS_TABLE = '''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_role_id INTEGER,
    FOREIGN KEY (user_role_id) REFERENCES UserRoles(user_role_id)
);
'''

CREATE_TASKS_TABLE = '''
CREATE TABLE IF NOT EXISTS Tasks (
    task_id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    task_description TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER,
    category_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES TaskCategories(category_id)
);
'''

CREATE_TASK_CATEGORIES_TABLE = '''
CREATE TABLE IF NOT EXISTS TaskCategories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL,
    category_description TEXT
);
'''

CREATE_POMODORO_CYCLES_TABLE = '''
CREATE TABLE IF NOT EXISTS PomodoroCycles (
    pomodoro_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    duration INTEGER,
    task_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
);
'''

CREATE_USER_TASK_CATEGORY_TABLE = '''
CREATE TABLE IF NOT EXISTS UserTaskCategory (
    user_id INTEGER,
    category_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES TaskCategories(category_id),
    PRIMARY KEY (user_id, category_id)
);
'''

CREATE_USER_ROLES_TABLE = '''
CREATE TABLE IF NOT EXISTS UserRoles (
    user_role_id INTEGER PRIMARY KEY,
    user_role_name TEXT NOT NULL
);
'''
