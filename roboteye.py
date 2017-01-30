from bottle import run, template, static_file, route, get
from helper import ROBOTEYE_PORT, HOST


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@get('/')
def get_index():
    return template('robot')


if __name__ == '__main__':
    run(host=HOST, port=ROBOTEYE_PORT)
