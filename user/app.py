'''
練習プログラム
'''
from bottle import Bottle,\
    jinja2_template as template,\
        static_file, request, redirect
        
from bottle import response, run
import psycopg2
import psycopg2.extras

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'book_data'
DB_USER = 'book_user'
DB_PASS = '314159'

app = Bottle()

def get_connection():
    dsn = 'host={host} port={port} dbname={dbname} \
        user={user} password={password}'
    dsn = dsn.format(user=DB_USER, password=DB_PASS, \
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME)
    return psycopg2.connect(dsn)

@app.route('/', method=['GET', 'POST'])
def index():
    return "Hello World"

@app.route('/add', method=['GET', 'POST'])
def add():
    form_html = """<html>
    <head>登録フォーム</head>
    <body>
    <form action="/add" method="post">
    ユーザID:<input type="text" name="user_id" value="<!--user_id-->" /><br />
    パスワード:<input type="text" name="passwd" value="<!--passwd-->" /><br />
    email:<input type="text" name="email" value="<!--email-->" /><br />
    氏:<input type="text" name="user_shi" value="<!--user_shi-->" /><br />
    名:<input type="text" name="user_mei" value="<!--user_mei-->" /><br />
    <input type="submit" value="確認" name="next"/>
    </form>
    </body>
    </html>
    """
    
    confirm_html = """<html>
    <head>確認</head>
    <body>
    <form action="/regist" method="post">
    ユーザID:<!--user_id--><br />
    パスワード:<!--passwd--><br />
    email:<!--email--><br />
    氏:<!--user_shi--><br />
    名:<!--user_mei--><br />
    <input type="hidden" name="user_id" value="<!--user_id-->" />
    <input type="hidden" name="passwd" value="<!--passwd-->" />
    <input type="hidden" name="email" value="<!--email-->" />
    <input type="hidden" name="user_shi" value="<!--user_shi-->" />
    <input type="hidden" name="user_mei" value="<!--user_mei-->" />
    <input type="submit" value="back" name="next"/>&nbsp;&nbsp;
    <input type="submit" value="regist" name"next"/>
    </form>
    </body>
    </html>
    """
    
    if request.method == "GET" or request.forms.get('next') == 'back':
        return form_html.replace('<!--user_id-->', '').\
        replace('<!--passwd-->', '').\
        replace('<!--email-->', '').\
        replace('<!--user_shi-->', '').\
        replace('<!--user_mei-->', '')
    else:
        form = {}
        form['user_id'] = request.forms.decode().get('user_id')
        form['passwd'] = request.forms.decode().get('passwd')
        form['email'] = request.forms.decode().get('email')
        form['user_shi'] = request.forms.decode().get('user_shi')
        form['user_mei'] = request.forms.decode().get('user_mei')
    
        if request.forms.get('next') == 'back':
            html = form_html
        else:
            html = confirm_html
            
        return html.replace('<!--user_id-->', form['user_id']).\
        replace('<!--passwd-->', form['passwd']).\
        replace('<!--email-->', form['email']).\
        replace('<!--user_shi-->', form['user_shi']).\
        replace('<!--user_mei-->', form['user_mei'])
    
@app.route('/regist', method=["POST"])
def regist():
    if request.forms.get('next') == 'back':
        response.status = 307
        response.set_header("Location", '/add')
        return response
    else:
        user_id = request.forms.decode().get('user_id')
        passwd  = request.forms.decode().get('passwd')
        email   = request.forms.decode().get('email')
        user_shi = request.forms.decode().get('user_shi')
        user_mei = request.forms.decode().get('user_mei')
        
        sql = """insert into book_user \
        (user_id, passwd, email, user_shi, user_mei, del) \
        values \
        (%(user_id)s, %(passwd)s, %(email)s, %(user_shi)s, %(user_mei)s, false);"""
        
        val = {'user_id':user_id, 'passwd':passwd,\
            'email':email, 'user_shi':user_shi,\
            'user_mei':user_mei}
        with get_connection() as con:
            with con.cursor() as cur:
                cur.execute(sql, val)
            con.commit()
        redirect('/add')
        
@app.route('/list')
def list():
    sql = """select user_id, email, user_shi,\
        user_mei from book_user \
        where del = false \
        order by user_id asc;"""
    with get_connection() as con:
        with con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            rows = [dict(row) for row in rows]
    return template('list.html', rows=rows)




if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port=8000, reloader=True, debug=True)