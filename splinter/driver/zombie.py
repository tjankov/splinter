from splinter.driver import DriverAPI


def socket_send(message):
    import socket
    host= 'localhost'
    port = 8042
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect((host, port))
    _socket.send(message)
    _socket.close()


#def socket_write(js):
#    return socket_send("%s\nstre" % js)


class ZombieDriver(DriverAPI):

    def visit(self, url):
        socket_send('browser.visit("%s")' % url)

    @property
    def html(self):
        return socket_send('browser.html()') 


