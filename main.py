from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '360')


class TimeClock(GridLayout):
    def __init__(self, **kwargs):
        super(TimeClock, self).__init__(**kwargs)
        self.cols = 3
        self.time_one = Label(text='0',
                              font_size=65,
                              color=[.85, .25, .25, 1])
        self.time_two = Label(text=':',
                              font_size=65,
                              color=[.85, .25, .25, 1])
        self.time_there = Label(text='0',
                                font_size=65,
                                color=[.85, .25, .25, 1])
        self.button_start = Button(text='Старт',
                                   font_size=35,
                                   on_press=self.start,
                                   color=[.23, .28, .55, 1],
                                   background_color=[0, 0, 0, 1]
                                   )
        self.button_stop = Button(text='Стоп',
                                  font_size=35,
                                  on_press=self.stop,
                                  color=[.23, .28, .55, 1],
                                  background_color=[0, 0, 0, 1]
                                  )
        self.button_restart = Button(text='Сброс',
                                     font_size=35,
                                     on_press=self.restart,
                                     color=[.23, .28, .55, 1],
                                     background_color=[0, 0, 0, 1])
        self.add_widget(self.time_one)
        self.add_widget(self.time_two)
        self.add_widget(self.time_there)
        self.add_widget(self.button_start)
        self.add_widget(self.button_stop)
        self.add_widget(self.button_restart)

    def restart(self, *args):
        self.clock.cancel()
        self.time_one.text = '0'
        self.time_there.text = '0'

    def stop(self, *args):
        self.clock.cancel()

    def start(self, *args):
        self.time_there.text = str(int(self.time_there.text) + 1)
        if int(self.time_there.text) == 60:
            self.time_one.text = str(int(self.time_one.text) + 1)
            self.time_there.text = '0'
            self.clock = Clock.schedule_once(self.start, 1)
        else:
            self.clock = Clock.schedule_once(self.start, 1)


class MyFirstApp(App):
    def build(self):
        return TimeClock()


if __name__ == '__main__':
    MyFirstApp().run()
