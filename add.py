import sqlite3
from typing import List

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

f = open("sql/data.sql", encoding="utf8")
lines = f.readlines()
f.close()


def add_genres(line_num: int, stmt: str):
    replace_stmt = "INSERT INTO genres (genre_id, genre, parent_id) VALUES ("
    tokenized_stmt: List[str] = stmt.split(replace_stmt)
    del (tokenized_stmt[0])
    tokenized_stmt: List[str] = tokenized_stmt[0].split(", ")
    tokenized_stmt[2] = tokenized_stmt[2][0:-2]
    sql_stmt = "INSERT INTO library_genre (id, name, parent_id) VALUES ("
    sql_stmt += tokenized_stmt[0] + ", "
    sql_stmt += tokenized_stmt[1] + ", "
    sql_stmt += tokenized_stmt[2]
    sql_stmt += ")"
    print("adding", tokenized_stmt[1], "to genres")
    cur.execute(sql_stmt)


def add_authors(line_num: int, stmt: str):
    replace_stmt = "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES ("
    tokenized_stmt: List[str] = stmt.split(replace_stmt)
    del (tokenized_stmt[0])
    tokenized_stmt: List[str] = tokenized_stmt[0].split(",")
    tokenized_stmt[3] = tokenized_stmt[3][0:-2]
    sql_stmt = "INSERT INTO library_author (id, first_name, middle_name, last_name) VALUES ("
    sql_stmt += tokenized_stmt[0] + ", "
    sql_stmt += tokenized_stmt[1] + ", "
    sql_stmt += tokenized_stmt[2] + ", "
    sql_stmt += tokenized_stmt[3]
    sql_stmt += ")"
    cur.execute(sql_stmt)
    try:
        if tokenized_stmt[1] != 'null' and tokenized_stmt[2] != 'null' and tokenized_stmt[3] != 'null':
            print(line_num + 1, 'adding', eval(tokenized_stmt[1]), tokenized_stmt[2], eval(tokenized_stmt[3]),
                  'to authors')
        if tokenized_stmt[1] != 'null' and tokenized_stmt[2] == 'null' and tokenized_stmt[3] != 'null':
            print(line_num + 1, 'adding', eval(tokenized_stmt[1]), eval(tokenized_stmt[3]), 'to authors')
        if tokenized_stmt[1] != 'null' and tokenized_stmt[2] == 'null' and tokenized_stmt[3] == 'null':
            print(line_num + 1, 'adding', eval(tokenized_stmt[1]), 'to authors')
    except NameError:
        raise SyntaxError('on line ' + str(line_num + 1))


def add_books(line_num: int, stmt: str):
    replace_stmt = "insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values ("
    tokenized_stmt: List[str] = stmt.split(replace_stmt)
    del (tokenized_stmt[0])
    tokenized_stmt: List[str] = tokenized_stmt[0].split(",")
    tokenized_stmt[6] = tokenized_stmt[6][0:-2]
    sql_stmt = "INSERT INTO library_book (id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES ("
    sql_stmt += tokenized_stmt[0] + ", "
    sql_stmt += tokenized_stmt[1] + ", "
    sql_stmt += tokenized_stmt[2] + ", "
    sql_stmt += tokenized_stmt[3] + ", "
    sql_stmt += tokenized_stmt[4] + ", "
    sql_stmt += tokenized_stmt[5] + ", "
    sql_stmt += tokenized_stmt[6]
    sql_stmt += ")"
    cur.execute(sql_stmt)
    try:
        print('adding', "'" + eval(tokenized_stmt[1]), 'to books' + "'")
    except SyntaxError:
        raise SyntaxError('on line ' + str(line_num + 1))


def add_publishers(line_num: int, stmt: str):
    replace_stmt = "INSERT INTO publishers(publisher_id,name) values ("
    tokenized_stmt: List[str] = stmt.split(replace_stmt)
    del (tokenized_stmt[0])
    tokenized_stmt: List[str] = tokenized_stmt[0].split(",")
    tokenized_stmt[1] = tokenized_stmt[1][0:-2]
    sql_stmt = "INSERT INTO library_publisher (id, name) VALUES ("
    sql_stmt += tokenized_stmt[0] + ", "
    sql_stmt += tokenized_stmt[1]
    sql_stmt += ")"
    print("adding", tokenized_stmt[1], "to publishers")
    # print(line_num+1, sql_stmt)
    cur.execute(sql_stmt)


def add_book_genres(line_num: int, stmt):
    replace_stmt = "INSERT INTO book_genres (book_id, genre_id) VALUES("
    tokenized_stmt: List[str] = stmt.split(replace_stmt)
    del (tokenized_stmt[0])
    tokenized_stmt: List[str] = tokenized_stmt[0].split(",")
    tokenized_stmt[1] = tokenized_stmt[1][0:-2]
    sql_stmt = "INSERT INTO library_book_genres (book_id, genre_id) VALUES ("
    sql_stmt += tokenized_stmt[0] + ", "
    sql_stmt += tokenized_stmt[1]
    sql_stmt += ")"
    print("adding", "to book_genres")
    cur.execute(sql_stmt)


def add_book_authors(line_num: int, stmt):
    replace_stmt = "INSERT INTO book_authors (book_id, author_id) values ("
    tokenized_stmt: List[str] = stmt.split(replace_stmt)
    del (tokenized_stmt[0])
    tokenized_stmt: List[str] = tokenized_stmt[0].split(",")
    tokenized_stmt[1] = tokenized_stmt[1][0:-2]
    sql_stmt = "UPDATE library_book SET author_id=" + tokenized_stmt[0] + " WHERE id=" + tokenized_stmt[1] + ";"
    print("updating", "to book with authors")
    cur.execute(sql_stmt)
    # print(sql_stmt)


step = ""
for line_num, line in enumerate(lines):
    if line[0:3] == "-- ":
        func = "add_" + line[3:].replace(" ", "_").replace("\n", "") + "()"
        if func[:-2] in globals().keys():
            step = line[3:].replace(" ", "_").replace("\n", "")
            # print(func)
    elif line == "\n":
        continue
    else:

        func = "add_" + step
        if func in globals().keys():
            myline = line.replace("\n", "")

            func = "add_" + step + f'({line_num}, "{myline}")'

            eval(func)

conn.commit()
conn.close()
