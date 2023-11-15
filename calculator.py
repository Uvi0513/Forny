def colored_text(text, r, g, b):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

text1 = "█▀▀ █▀█ █▀█ █▄░█ █▄█"
text2 = "█▀░ █▄█ █▀▄ █░▀█ ░█░"

# Set RGB values for each text
color_red = (255, 0, 0)      # Red
color_green = (0, 255, 0)    # Green
color_yellow = (255, 255, 0) # Yellow

# Print colored text
print(colored_text(text1, *color_red))
print(colored_text(text2, *color_green))
print(colored_text(text1, *color_yellow))
