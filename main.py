import flet as ft
from flet import TextStyle

from utils import funcs

class MyButton(ft.ElevatedButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(size=18, font_family="Segoe"),
                                        color={ft.ControlState.HOVERED: ft.Colors.WHITE},
                                        bgcolor={ft.ControlState.HOVERED: "#5461AA"}
                                    )

def main(page: ft.Page):
    page.title = "Simple File Manager"
    page.theme = ft.Theme(font_family="Segoe")
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    dir = ft.TextField(label="Выберите директорию или файл...", label_style= ft.TextStyle(size=20, font_family="Segoe"), text_size=20)
    srch = ft.TextField(label="Введите текст для поиска...", label_style= ft.TextStyle(size=20), text_size=20)

    result = ft.TextField(label="Результат", multiline=True, min_lines=1, max_lines=10, width=800, label_style= ft.TextStyle(size=20), text_size=20)

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files is None:
            dir.value = e.path
            dir.update()
            page.update()
        else:
            selected_files = ", ".join(map(lambda f: f.path, e.files))
            dir.value = selected_files
            dir.update()
            page.update()

    file_picker = ft.FilePicker(on_result=on_dialog_result)

    choose_dir = MyButton("Выбрать директорию...", on_click=lambda _: file_picker.get_directory_path())
    choose_file = MyButton("Выбрать файл...", on_click=lambda _: file_picker.pick_files(allow_multiple=False))

    def copy_file(e):
        funcs.copy(str(dir.value), "None")
        result.value = "Файл скопирован"
        result.update()
        page.update()

    def del_file(e):
        funcs.delete(str(dir.value))
        result.value = "Файл удален"
        result.update()
        page.update()

    def nf(e):
        result.value = str(funcs.num_files(str(dir.value)))
        result.update()
        page.update()

    def search_file(e):
        result.value = funcs.search(str(dir.value), str(srch.value))
        result.update()
        page.update()

    def add_date(e):
        funcs.add(str(dir.value))
        result.value = "Имена всех файлов изменены"
        result.update()
        page.update()

    def analyse_folder(e):
        result.value = funcs.analyse(str(dir.value))
        result.update()
        page.update()

    copy_button = MyButton("Копировать", on_click=copy_file)
    del_button = MyButton("Удалить", on_click=del_file)
    nf_button = MyButton("Подсчитать", on_click=nf)
    search_button = MyButton("Искать", on_click=search_file)
    add_button = MyButton("Добавить дату", on_click=add_date)
    analyse_button = MyButton("Проанализировать размер", on_click=analyse_folder)

    body = ft.Stack([
        file_picker,
        dir,
        ft.Container(
            content=ft.Column([
                ft.Row(controls=[ft.Row(controls=[choose_file, copy_button])]),
            ]),
            left=0,
            top=70
        ),
        ft.Row(controls=[result], top=130),
    ],
        width=800,
        height=500)

    def change_body(e):
        content = body.controls[2].content.controls
        content.clear()
        if e.control.selected_index == 0:
            content.append(
                ft.Column([
                    ft.Row(controls=[ft.Row(controls=[choose_file, copy_button])]),
                ])
            )

        elif e.control.selected_index == 1:
            content.append(
                ft.Column([
                    ft.Row(controls=[ft.Row(controls=[choose_file, del_button])]),
                ])
            )

        elif e.control.selected_index == 2:
            content.append(
                ft.Column([
                    ft.Row(controls=[ft.Row(controls=[choose_dir, nf_button])]),
                ])
            )

        elif e.control.selected_index == 3:
            content.append(
                ft.Column([
                    ft.Row(controls=[ft.Row(controls=[choose_dir, srch, search_button])]),
                ])
            )

        elif e.control.selected_index == 4:
            content.append(
                ft.Column([
                    ft.Row(controls=[ft.Row(controls=[choose_dir, add_button])]),
                ])
            )

        else:
            content.append(
                ft.Column([
                    ft.Row(controls=[ft.Row(controls=[choose_dir, analyse_button])]),
                ])
            )

        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        height=500,
        group_alignment=-0.9,
        on_change=change_body,
        selected_label_text_style= TextStyle(weight=ft.FontWeight.BOLD, color="black", font_family="Segoe", size=14),
        indicator_color="#5461AA",
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FILE_COPY_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.FILE_COPY_ROUNDED, color="white"),
                label_content=ft.Text("Копировать", color="black", font_family="Segoe", size=14)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.DELETE_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DELETE, color="white"),
                label_content=ft.Text("Удалить", color="black", font_family="Segoe", size=14)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.NUMBERS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.NUMBERS, color="white"),
                label_content=ft.Text("Кол-во файлов", color="black", font_family="Segoe", size=14)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.MANAGE_SEARCH_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.MANAGE_SEARCH, color="white"),
                label_content=ft.Text("Искать", color="black", font_family="Segoe", size=14)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ADD_CIRCLE_OUTLINE_ROUNDED,
                selected_icon=ft.Icon(ft.Icons.ADD_CIRCLE_ROUNDED, color="white"),
                label_content=ft.Text("Добавить", color="black", font_family="Segoe", size=14)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SNIPPET_FOLDER_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SNIPPET_FOLDER, color="white"),
                label_content=ft.Text("Узнать размер", color="black", font_family="Segoe", size=14)
            ),
        ],

    )

    page.add(
        ft.Container(
            width=page.width,
            height=50,
            bgcolor="#5461AA",
            border_radius=8,
            padding=5,
            content=ft.Column([ft.Text("Simple File Manager", color="white", font_family="Segoe", size=24)],
                              alignment=ft.MainAxisAlignment.CENTER)
        ),
        ft.Row([
            rail,
            ft.VerticalDivider(width=10),
            body
        ], expand=True)

    )
    page.update()


ft.app(main)
