import sqlite3 as sq

def get_anniv(aid):
    conn = sq.connect('./db_sqlite/test.db')
    cur = conn.cursor()

    sql = 'select * from anniversary where aid=?'
    cur.execute(sql)
    rows = cur.fetchall()       # 결과 받을땐 이렇게!

    cur.close()                 # 다했으면 꼭 닫아주기!
    conn.close()

    return rows
 


# start date ~ end date, uid field가 'admin' 또는 uid
def get_anniv_list(sdate, edate, uid):
    conn = sq.connect('./db_sqlite/test.db')
    cur = conn.cursor()
    if uid == 'admin':
        sql = 'select * from anniversary where adate between ? and ? and uid=?'
    else:
        sql = "select * from anniversary where adate between ? and ? and (uid='admin' or uid=?)"
    cur.execute(sql, (sdate, edate, uid))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

def insert_anniv(params):
    conn = sq.connect('./db_sqlite/test.db')
    cur = conn.cursor()

    sql = 'insert into anniversary(aname, adate, is_holiday, uid) values (?, ?, ?, ?)'
    cur.execute(sql, params)              # 파라메타는 반드시 튜플로 전달해야 함 : (age, )
    conn.commit()

    cur.close()
    conn.close()


def insert_anniv_many(params_list):
    conn = sq.connect('./db_sqlite/test.db')
    cur = conn.cursor()
    sql = 'insert into anniversary(aname, adate, is_holiday, uid) values (?, ?, ?, ?)'
    cur.executemany(sql, params_list)            # executemany: params의 리스트를 한번에 !
    conn.commit()

    cur.close()
    conn.close()

def update_anniv(params):
    conn = sq.connect('./db_sqlite/test.db')
    cur = conn.cursor()

    sql = 'update anniversary set aname=?, adate=?, is_holiday=? where aid=?'
    cur.execute(sql, params)              # 파라메타는 반드시 튜플로 전달해야 함 : (age, )
    conn.commit()

    cur.close()
    conn.close()


def delete_anniv(aid):
    conn = sq.connect('./db_sqlite/test.db')
    cur = conn.cursor()

    sql = 'delete from anniversary where aid=?'
    cur.execute(sql, (aid, ))              # 파라메타는 반드시 튜플로 전달해야 함 : (age, )
    conn.commit()

    cur.close()
    conn.close()