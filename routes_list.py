from bottle import Bottle, jinja2_template as template,\
    request, redirect
from bottle import response
import routes
from models import connection, Books
from utils.auth import Auth
import urllib.parse as urlpar

app  = routes.app
auth = Auth()

@app.route('/list')
def list():
    auth.check_login()
    
    bookList = connection.query(Books.name,
                            Books.volume, Books.author,
                            Books.publisher, Books.memo,
                            Books.id_)\
            .filter(Books.delFlg == False).all()
    headers = ['書名', '巻数', '著者', '出版社', 'メモ', '操作']
    return remplate('list.html', bookList=bookList, headers=headers)