import Game_Module as gm

# metoda wypiswaynia tekstu na ekran
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    gm.screen.blit(img, (x, y))


# # instancja przycisku
# lvl_easy = button.Button(240, 125, gm.button_lvl1, 1.5)
# exit = button.Button(240, 325, gm.button_lvl1, 1.5)

def display_option():
    gm.screen.blit(gm.score_image, (180, 230))
    draw_text("SCORE: ", gm.font, gm.WHITE, 230, 240)
    gm.screen.blit(gm.play, (180, 380))
    draw_text("Press 'E' to play!", gm.font, gm.WHITE, 230, 390)
    gm.screen.blit(gm.exit, (180, 450))
    draw_text("Press 'Q' to quit!", gm.font, gm.WHITE, 230, 460)
