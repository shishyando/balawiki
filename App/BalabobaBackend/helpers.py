def get_old_wikis(query):
    # return a list: [(response_text, timestamp)] for query
    # no more than 5 items
    # @figor
    pass


def push_wikis(query, wikis):
    # set list wikis [(wiki_text, timestamp)] for the query
    # @figor
    pass


def get_old_comms(query):
    # same thing
    # no more than 10 items
    # @figor
    pass


def push_comms(query, comms):
    # set list comms [(comm_text, timestamp)] for the query
    # @figor
    pass


def get_new_wiki(query):
    # balaboba api @bugor
    pass


def get_new_comm(query):
    # balaboba api @bugor
    pass


def update(old_responses, new_response, timestamp):
    if len(old_responses) == 5:
        old_responses = old_responses[1:]
    old_responses.append(tuple(new_response, timestamp))
    return old_responses


def need_new_response(old_responses, cur_time, ttl):
    old_responses.sort(key=lambda tup: tup[1])
    if len(old_responses) < 5 or \
            cur_time - old_responses[-1][1] > ttl:
        return True
    return False

