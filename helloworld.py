import web, webbrowser, multiprocessing

urls = (
          '/', 'index'
    )

class index:
    def GET(self, name):
      return "Hello, World"

if __name__ == '__main__':
    app = web.application(urls, globals())
    multiprocessing.Process(target=app.run).start()
    webbrowser.open_new_tab("http://0.0.0.0:8080/")
