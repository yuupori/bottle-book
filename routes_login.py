from bottle import Bottle, jinja2_template as template,\
    request, redirect
from bottle import response
import routes
from models import connection, BookUser
from utils.session import Session
from utils.auth import Auth
import urllib.parse as urlpar

REDIRECT_AFTER_LOGIN  = '/list'
REDIRECT_AFTER_LOGOFF = '/'

app = routes.app

@app.route('/')
def index():
    err_msg = request.query.error
    if err_msg is None:
        err_nsg = None
        
    return template('login.html', error=err_msg)

@app.route('/login', method='POST')
def login():
    user_id = request.forms.decode().get('user_id')
    passwd  = request.forms.decode().get('passwd')
    
    user = connection.query(BookUser.user_id).filter\
        (BookUser.user_id == user_id,\
            BookUser.passwd == passwd,\
                BookUser.delFlg == False).scalar()
    print(user)
    if user is not None:
        auth = Auth()
        auth.add_auth(user)
        redirect(REDIRECT_AFTER_LOGIN)
    else:
        err_msg = urlpar.quote('認証に失敗しました')
        redirect(REDIRECT_AFTER_LOGOFF + '?error=' + err_msg)
        
@app.route('/logout', method=['GET', 'POST'])
def logout():
    auth = Auth()
    auth.del_auth()
    redirect(REDIRECT_AFTER_LOGOFF)
    