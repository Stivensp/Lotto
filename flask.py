import webview

class API:
    def saludar(self):
        print("¡Hola desde Python!")
        # También puedes devolver un mensaje si quieres
        return "¡Hola desde Python, mensaje recibido!"

if __name__ == '__main__':
    api = API()
    webview.create_window('Mi Aplicación', 'index.html', js_api=api)
    webview.start()