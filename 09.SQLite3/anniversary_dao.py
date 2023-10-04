import sqlite3 as sq

def get_anniv(aid):
    sql = 'select * from anniversary where aid=?'
    pass

# star data ~ end date, uid가 'admin' 또는 uid
def get_anniv_list(state, edate, uid):
    pass

def insert_anniv(params):
    sql = 'insert into anniversary(aname, adate, is_holiday, uid) values (?, ?, ?, ?)'
    pass

def inserf_anniv_many(params_list):
    sql = 'insert into anniversary(aname, adate, is_holiday, uid) values (?, ?, ?, ?)'
    pass

def update_anniv(params):
    sql = 'update anniversary set aname=?, adate=?, is_holiday=? where aid=?'
    pass

def delete_anniv(aid):
    sql = 'delete from anniversary where aid=?'
    pass



