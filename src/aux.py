def message_to_screen(msg,color):
    screen_text = font.render(msg,True, color)
    gameDisplay.blit(screen_text,[display_width/2 ,display_height/2]) #adaptar depois