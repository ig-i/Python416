CREATE TABLE IF NOT EXISTS mainmenu(  -- создаем таблицу с пунктом меню
id INTEGER PRIMARY KEY AUTOINCREMENT, -- создаем поле для автоматического ключа id
title TEXT NOT NULL,                  -- создаем поле текст (не пустое)
url TEXT NOT NULL                      -- поле эл.адрес (не пустое)
);

CREATE TABLE IF NOT EXISTS posts (    -- создаем еще 1 таблицу posts
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
text TEXT NOT NULL,
time INTEGER NOT NULL
);