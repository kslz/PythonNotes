import sqlite3
import time

import ijson

file_name = 'abc.json'
time_start = time.time()
with open(file_name, 'r', encoding='utf-8') as f:
    obj = ijson.items(f, 'audios.item', use_float=True)
    # audios = list(obj)
    # for audio in obj:
    audios = list(
        [o["aid"], float(o["duration"]), o["md5"], o["path"], o["source"], str(o["tags"]), o["url"]] for o in obj)
print(len(audios))
conn = sqlite3.connect('D:/ljl/study/sqlite/testlite.db')
c = conn.cursor()
table = "\"table\""
cursor = c.execute(f'SELECT name FROM sqlite_master WHERE type={table} ORDER BY name')
for row in cursor:
    print(row)
print("Opened database successfully")
for audio in audios:
    c.execute(
        f'INSERT INTO "main"."audio"("aid", "duration", "md5", "path", "source", "url", "tags") VALUES (\"{audio[0]}\",{audio[1]},\"{audio[2]}\",\"{audio[3]}\",\"{audio[4]}\",\"{audio[6]}\",\"{audio[5]}\")')

conn.commit()
print("Records created successfully")
conn.close()
