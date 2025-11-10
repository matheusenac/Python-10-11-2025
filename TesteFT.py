import flet as ft

def main(page: ft.Page):
    page.title = "Teste Flet"
    page.add(ft.Text("Testando e funcionando!", size=23, color="blue"))

ft.app(target=main)