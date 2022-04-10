import sqlite3
import time

import ijson

file_name = 'abc.json'
time_start = time.time()
with open(file_name, 'r', encoding='utf-8') as f:
    obj = ijson.items(f, 'audios.item', use_float=True)
    # audios = list(obj)
    # for audio in obj:
    audios = list(o["aid"] for o in obj)
print(len(audios))
for audio in audios:
    with open(file_name, 'r', encoding='utf-8') as f:
        obj2 = ijson.items(f, 'audios.item', use_float=True)
        # subsets = ([o["aid"],o["sid"],o["confidence"],o["begin_time"],o["end_time"],o["subsets"],o["text"]] for o in obj2 if o["aid"] == audio)
        subsets = (o["segments"] for o in obj2 if o["aid"] == audio)
        conn = sqlite3.connect('D:/ljl/study/sqlite/testlite.db')
        c = conn.cursor()
        for subset in subsets.__next__():
            c.execute(
                f'INSERT INTO "main"."segment"("sid", "confidence", "begin_time", "end_time", "subsets", "text", "aid") VALUES (\"{subset["sid"]}\", {subset["confidence"]}, {subset["begin_time"]}, {subset["end_time"]}, \"{str(subset["subsets"])}\", \"{subset["text"]}\", \"{audio}\")')
        conn.commit()
        conn.close()
time_end = time.time()
print('totally cost', time_end - time_start)
