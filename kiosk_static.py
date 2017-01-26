from helper import MJPEG_PORT, ROBOT_PORT, check_port, get_ip_address, get_netstat_output, INTERFACE

from bottle import template


def write_kiosk():
    with open('static/index.html', 'w') as static_page:
        try:
            mjpeg_status = 'Up' if check_port(MJPEG_PORT) else 'Down'
            robot_status = 'Up' if check_port(ROBOT_PORT) else 'Down'
            content = template('index',
                               ip_address=get_ip_address(INTERFACE),
                               netstat_output=get_netstat_output(),
                               mjpeg_status=mjpeg_status,
                               robot_status=robot_status)
        except Exception as e:
            print(str(e))
            content = "unable to determine ip"
        static_page.write(content)

if __name__=='__main__':
    write_kiosk()