create table if not exists responses(
    id integer primary key autoincrement,
    query text not null,
    response text not null,
    response_timestamp int not null
);

create table if not exists comms(
    id integer primary key autoincrement,
    query text not null,
    comm text not null,
    comm_timestamp int not null
);