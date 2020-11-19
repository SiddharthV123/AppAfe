import webview
import kivy
from kivy.app import App
import buildozer



webview.create_window('AstrologyFutureEye', 'https://astrologyfutureeye.com/')
webview.start()

class TestApp(App):
    pass


if __name__ == '__main__':
    TestApp().run()