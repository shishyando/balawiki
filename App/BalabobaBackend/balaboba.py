import time
from BalabobaBackend.helpers import *


def get_text(query):  # Короче хочу по абзацам текст
    if query == 'тян':
        return ['Короче, тян — это не девушка, а просто женщина, которая, в отличие от девушки, не умеет готовить.',
                'Короче, тян — это девушка, которая не хочет иметь с вами детей.',
                'Короче, тян — девушка, которая не хочет отношений.',
                'Короче, тян — девушка, которая на вопрос "Где ты работаешь?" отвечает: "Я не работаю, я — творю".',
                'Короче, тян — то, чего так не хватает по выходным каждому уважающему себя мужчине.']
    cur_time = int(time.time())
    old_wikis = get_old_wikis(query)  # [(wiki_text, timestamp)]
    if need_new_response(old_wikis, cur_time, 3600 * 24):
        new_wiki = get_new_wiki(query)
        upd_wikis = update(old_wikis, new_wiki, cur_time)
        push_wikis(query, upd_wikis)
        # нужно возвращать текст с размеченными редиректами?
        return [e[0] for e in upd_wikis]
    return [e[0] for e in old_wikis]


def get_comments(query):  # Короче хочу по абзацам народные мудрости
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
        upd_comms = update(old_comms, new_comm)
        push_comms(query, upd_comms)
        return [e[0] for e in upd_comms]
    return [e[0] for e in old_comms]
