import flet as ft


class App:
    def __call__(self, page: ft.Page):
        self.page = page
        self.page.add(ft.SafeArea(ft.Text('Label')))
