import flet as ft
from label import storage


class App:
    def __call__(self, page: ft.Page):
        self.page = page
        self.page.add(ft.SafeArea(ft.Text('Label')))
        self.storage_path = storage.get_storage_path(self.page)
