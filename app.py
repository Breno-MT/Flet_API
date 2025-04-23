import flet as ft

icon_dark_mode = ft.Icons.DARK_MODE_OUTLINED
icon_light_mode = ft.Icons.LIGHT_MODE_OUTLINED

avatar = ft.CircleAvatar(
    bgcolor=ft.colors.BLUE,
    color=ft.colors.WHITE,
    content=ft.Text("MA"),
    max_radius=30,
    min_radius=15,
    tooltip="Marcelo Araujo",
    badge=ft.Badge(
        bgcolor=ft.colors.GREEN,    # Can make it like a button to change its value to afk or sum, or add an option to the menulist
        small_size=15,
        alignment=ft.alignment.top_right,  # This value is the default, you can set other alignment
    ),
)


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK

    def change_theme_mode(e: ft.ControlEvent):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = icon_dark_mode
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = icon_light_mode

        page.update()

    navbar = ft.Pagelet(
        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.DASHBOARD),
            leading_width=40,
            title=ft.Text("Lead Dashboard"),
            center_title=True,
            bgcolor=ft.Colors.SURFACE,
            actions=[
                avatar,
                ft.IconButton(icon=icon_dark_mode, on_click=change_theme_mode),
                ft.PopupMenuButton(
                    items=[
                        # TODO: change this buttons, or not, to have some real function
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item",
                            checked=False,
                        ),
                    ]
                ),
            ],
        ),
        content=ft.Container(),     # Dashboard code goes here, probably will be divided in pieces of codes
        height=200,
    )

    page.add(navbar)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
