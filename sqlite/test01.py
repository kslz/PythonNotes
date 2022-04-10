import sqlite3
import ijson
from ijson.backends import _yajl2


def wtf(abc):
    print(abc)
    return abc


# 这里输入你的文件路径
file_name = 'abc.json'
with open(file_name, 'r', encoding='utf-8') as f:
    obj = ijson.items(f, 'audios.item', use_float=True)
    # audios = list(obj)
    # for audio in obj:
    audios = ([o["aid"], o["duration"], o["md5"], o["path"], o["source"], str(o["tags"]), o["url"]] for o in obj)
    for audio in audios:
        print(audio)

conn = sqlite3.connect('D:/ljl/study/sqlite/testlite.db')
c = conn.cursor()
print("Opened database successfully")

cursor = c.execute('SELECT *,rowid "NAVICAT_ROWID" FROM "main"."audio" LIMIT 0,1000')
# for row in cursor:
#     print(row)
# for i in range(5,100):
#     cursor = c.execute(
#         'INSERT INTO "main"."audio"("aid", "duration", "md5", "path", "source", "url", "tags") VALUES ('+str(i)+', 3, "4", '
#         '"5", "6", "7", "7")')

# cursor = c.execute('INSERT INTO "main"."audio"("aid", "duration", "md5", "path", "source", "url", "tags") VALUES ("3", 3, "4", "5", "6", "7", "7")')
conn.commit()

print("Operation done successfully")
conn.close()
