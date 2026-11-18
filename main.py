
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

import network_tools
import security_tools
import python_tools
import phone_tools
import password_tools
import calculator_tools
import file_tools
import history_tools
import system_tools
import extra_tools

Window.clearcolor = (0.03, 0.05, 0.04, 1)

modules = [
    ("Шабака ва интернет", network_tools),
    ("Амнияти киберӣ", security_tools),
    ("Омӯзиши Python", python_tools),
    ("Асбобҳои телефон", phone_tools),
    ("Парол ва рамзгузорӣ", password_tools),
    ("Ҳисобкунакҳо", calculator_tools),
    ("Файлҳо ва матн", file_tools),
    ("Таърихи санҷишҳо", history_tools),
    ("Маълумоти система", system_tools),
    ("Асбобҳои иловагӣ", extra_tools)
]


class HackerMasterApp(App):

    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="[b]HACKER MASTER TJ[/b]\nVERSION 20.0",
            markup=True,
            font_size="25sp",
            size_hint_y=None,
            height=100,
            color=(0.22, 1, 0.08, 1)
        )

        self.layout.add_widget(title)

        for name, module in modules:
            button = Button(
                text=name,
                font_size="18sp",
                size_hint_y=None,
                height=55,
                background_normal="",
                background_color=(0.08, 0.20, 0.10, 1),
                color=(0.3, 1, 0.2, 1)
            )

            button.bind(
                on_press=lambda instance, m=module, n=name:
                self.open_module(m, n)
            )

            self.layout.add_widget(button)

        self.result = Label(
            text="CYBER SECURITY • VERSION 20.0",
            size_hint_y=None,
            height=50
        )

        self.layout.add_widget(self.result)

        return self.layout

    def open_module(self, module, name):
        self.result.text = name

        try:
            module.show_menu()
        except Exception as error:
            self.result.text = str(error)


if __name__ == "__main__":
    HackerMasterApp().run()
