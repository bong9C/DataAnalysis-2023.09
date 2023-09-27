from flask import Blueprint, session, redirect, flash
import util.map_util as mu

user_bp = Blueprint('user_bp', __name__)

menu = {'ho':0, 'us':1, 'cr':0, 'ma':0, 'sc':0}

@user_bp.route('/login')
def login() : 
    # admin, 관리자로 로그인 했다고 가정
    flash('관리자님 환영합니다.')
    session['uid'] = 'admin'
    session['uname'] = '관리자'
    return redirect('/')