def get_text(query): # Короче хочу по абзацам текст
    if query == 'тян':
        return ['Короче, тян — это не девушка, а просто женщина, которая, в отличие от девушки, не умеет готовить.',
                'Короче, тян — это девушка, которая не хочет иметь с вами детей.',
                'Короче, тян — девушка, которая не хочет отношений.',
                'Короче, тян — девушка, которая на вопрос "Где ты работаешь?" отвечает: "Я не работаю, я — творю".'] * 2
    return ['Короче, сыр — продукт питания, в состав которого входит большое количество углеводов, жиров, белков и витаминов.',
            'Короче, сыр — это то, что остается в холодильнике после того, как все остальные продукты закончились.',
            'Короче, сыр — продукт, который можно съесть и получить удовольствие, а можно купить и сделать из него что-то.'] * 2


def get_comments(query): # Короче хочу по абзацам народные мудрости
    if query == 'тян':
        return ['тян тя – вёшенка, ёнтя – ёрш. (т.е. рыба, которую ловят на удочку)',
                'тян гуем, тянем, а тян все нет',
                'тян ко – это женщина, которая никогда не станет женщиной.',
                'тян -тян, не тронь – больно!'
         ] * 10
    return ['сыр в мышеловке счастлив, пока не съедят.',
            'сыр с плесенью, а хлеб с отрубями.',
            'сыр да мясо – жизнь прекрасна, но и в ней есть свои минусы.'] * 3

