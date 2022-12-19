import random
import time
from markupsafe import Markup
from flask import url_for
from BalabobaBackend.helpers import *
WORDS_WITH_LINKS = 3
MIN_SYBMOLS_IN_LINK_WORD = 5
PROHIBITED_ENDINGS = ['й', 'я']

# Проверяем, что слово подходящее для создания ссылки
def check_word(word):
    return word.isalpha() and len(word) >= MIN_SYBMOLS_IN_LINK_WORD and \
           not word[-1] in PROHIBITED_ENDINGS


def get_img(query):
    return get_img_link(query)

# Добавляем к случайным наборам слов в тексте ссылку на запрос
def insert_link(text):
    words = text.split()
    if len(words) == 0:
        return text
    
    already_used_id = []
    for i in range(WORDS_WITH_LINKS):
        link_start = random.randint(0, len(words) - 1) 
        while link_start < len(words) and not check_word(words[link_start]):
            link_start += 1

        if link_start in already_used_id or link_start == len(words):
            continue
        
        already_used_id.append(link_start)
        link_word = words[link_start]
        words = words[:link_start] + words[link_start + 1:]
        url_text = Markup('<a onclick="loading();" href="' + \
                        url_for('wiki_show', q=link_word) + \
                        '">' + link_word + '</a>')
        words.insert(link_start, url_text)
    
    return ' '.join(words) 


def get_text(query):  # Короче хочу по абзацам текст
    query = query.lower()
    if query == 'тян':
        return ['Короче, тян — это не девушка, а просто женщина, которая, в отличие от девушки, не умеет готовить.',
                'Короче, тян — это девушка, которая не хочет иметь с вами детей.',
                'Короче, тян — девушка, которая не хочет отношений.',
                'Короче, тян — девушка, которая на вопрос "Где ты работаешь?" отвечает: "Я не работаю, я — творю".',
                'Короче, тян — то, чего так не хватает по выходным каждому уважающему себя мужчине.']
    cur_time = int(time.time())
    old_wikis = get_old_wikis(query)  # [(wiki_text, timestamp)]
    if need_new_response(old_wikis, cur_time, 3600 * 24):
        new_wiki = insert_link(get_new_wiki(query))
        upd_wikis = update(old_wikis, new_wiki, cur_time)
        push_wikis(query, upd_wikis)
        # нужно возвращать текст с размеченными редиректами?
        return [e[0] for e in upd_wikis]
    return [e[0] for e in old_wikis]


def get_comments(query):  # Короче хочу по абзацам народные мудрости
    query = query.lower()
    if query == 'тян':
        return ['тян моего друга – всем тян. (т.е. рыба, которую ловят на удочку)',
                'тян ищем, призываем, а тян все нет',
                'тяночку бы',
                'тян -тян, не тронь – больно!'
                ] * 2

    cur_time = int(time.time())
    old_comms = get_old_comms(query)  # [(comm_text, timestamp)]
    if need_new_response(old_comms, cur_time, 3600 * 10):
        new_comm = get_new_comm(query)
        upd_comms = update(old_comms, new_comm, cur_time)
        push_comms(query, upd_comms)
        return [e[0] for e in upd_comms]
    return [e[0] for e in old_comms]
