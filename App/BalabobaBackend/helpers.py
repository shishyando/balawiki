import os
import sqlite3
import balaboba
DATABASE = os.path.join(os.path.dirname(__file__), 'balawiki.db')
BB_TEXT_TYPES = {
    'WIKI_TEXT': balaboba._text_type.TextType(
        number = 8, 
        name = 'Короче, Википедия', 
        description = 'Напишите какое-нибудь слово, а Балабоба даст этому определение'
    ), 
    'FOLK_WISDOM_TEXT': balaboba._text_type.TextType(
        number = 11, 
        name = 'Народные мудрости', 
        description = 'Напишите что-нибудь и получите народную мудрость'
    )
} 

# Замечание про датабазу, у меня она почему-то не хотела инициализироваться, после запуска кода создается пустой файл
# пофиксил это так: в пайчарме вылезает после того как потрогал sql файл надпись, что, мол, подключите базу данных,
# там выбираете data source from path и там выбираете файл с базой данных, после этого откроется консоль,
# туда скопировать и запустить код из sql

def connect_db():
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv


def get_old_wikis(query):
    db = connect_db()
    responses = db.execute(
        'select response, response_timestamp from responses where query = (?) order by response_timestamp limit 5', [query])
    lst = []
    for i in responses.fetchall():
        lst.append((i[0], i[1]))
    print(lst)
    return lst


def push_wikis(query, wikis):
    db = connect_db()
    db.execute('delete from responses where query = (?)', [query])
    for i in wikis:
        db.execute('insert into responses (query, response, response_timestamp) values (?, ?, ?)', [query, i[0], i[1]])
    db.commit()


def get_old_comms(query):
    db = connect_db()
    comms = db.execute(
        'select comm, comm_timestamp from comms where query = (?) order by comm_timestamp limit 10',
        [query])
    lst = []
    for i in comms.fetchall():
        lst.append((i[0], i[1]))
    print(lst)
    return lst


def push_comms(query, comms):
    db = connect_db()
    db.execute('delete from comms where query = (?)', [query])
    for i in comms:
        db.execute('insert into comms (query, comm, comm_timestamp) values (?, ?, ?)', [query, i[0], i[1]])
    db.commit()


def get_new_wiki(query):
    bb = balaboba.Balaboba()
    return bb.balaboba(query, BB_TEXT_TYPES['WIKI_TEXT'])


def get_new_comm(query):
    bb = balaboba.Balaboba()
    return bb.balaboba(query, BB_TEXT_TYPES['FOLK_WISDOM_TEXT'])


def update(old_responses, new_response, timestamp):
    if len(old_responses) == 5:
        old_responses = old_responses[1:]
    old_responses.append((new_response, timestamp))
    return old_responses


def need_new_response(old_responses, cur_time, ttl):
    old_responses.sort(key=lambda tup: tup[1])
    if len(old_responses) < 5 or \
            cur_time - old_responses[0][1] > ttl:
        return True
    return False
