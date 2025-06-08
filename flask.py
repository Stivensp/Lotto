import webview

class API:
 ""

if __name__ == '__main__':
    api = API()
    webview.create_window('Mi Aplicación', 'index.html', js_api=api,width=1210,height=720)
    webview.start()