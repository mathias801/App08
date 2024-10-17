import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla
    
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="mictlan"
    page.fgcolor="gray"
    
    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    PrimerNivel=ft.Audio(src="Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(PrimerNivel)
    
    SegundoNivel=ft.Audio(src="Segundo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(SegundoNivel)
    
    TercerNivel=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(TercerNivel)
    
    CuartoNivel=ft.Audio(src="Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(CuartoNivel)
    
    QuintoNivel=ft.Audio(src="Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(QuintoNivel)
    
    Nivel=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(TercerNivel)
    


ft.app(main)
