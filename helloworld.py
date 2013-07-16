import web

urls = (
          '/', 'index'
    )

class index:
    def GET(self, name):
      return "Hello, World"

app = web.application(urls, globals())
application = app.wsgifunc()
