from email.mime import application
import bottle
import routes
import routes_list
import routes_login
from utils.session import Session

app = routes.app
app_sess = routes.app_sess

if __name__ == '__main__':
    bottle.run(app=app_sess, host='0.0.0.0', port=8000, reloader=True, debug=True)
else:
    application = app_sess