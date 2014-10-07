from path import path
from tornado.websocket import WebSocketHandler
import tornado.ioloop
import tornado.web

# http://bibhas.in/blog/using-jinja2-as-the-template-engine-for-tornado-web-framework/


here = path(__file__).parent
pkg = here.parent


class MainHandler(tornado.web.RequestHandler):
    html = here / 'index.html'
    tvars = dict(react="react-0.11.2",
                 semantic='semantic/packaged')

    @property
    def html_txt(self):
        return self.html.text().format(**self.tvars)

    def get(self):
        self.write(self.html_txt)


class DashboardIO(WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"


application = tornado.web.Application([
    (r'/static/(.*)', tornado.web.StaticFileHandler,
     {'path': here / 'static'}),
    (r"/dashboard.ws", DashboardIO),
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
