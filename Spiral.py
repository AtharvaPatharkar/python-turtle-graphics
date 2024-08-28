from turtle import speed, bgcolor, colormode, fd, rt, pencolor, write, hideturtle, penup, goto, done

def clamp(val, min_val=0, max_val=255):
    return max(min_val, min(max_val, val))

speed(15)
bgcolor('black')
r, g, b = 255, 0, 0  # Starting with red

# Increased loop range and even more color transitions
for i in range(255 * 18):
    colormode(255)
    
    if i < 255:
        g += 1  # Red to Yellow
    elif i < 255 * 2:
        r -= 1  # Yellow to Green
    elif i < 255 * 3:
        b += 1  # Green to Cyan
    elif i < 255 * 4:
        g -= 1  # Cyan to Blue
    elif i < 255 * 5:
        r += 1  # Blue to Magenta
    elif i < 255 * 6:
        b -= 1  # Magenta to Red
    elif i < 255 * 7:
        r += 1  # Red to Light Red
    elif i < 255 * 8:
        g += 1  # Light Red to Orange
    elif i < 255 * 9:
        b += 1  # Orange to Light Orange
    elif i < 255 * 10:
        r -= 1  # Light Orange to Light Yellow
    elif i < 255 * 11:
        g -= 1  # Light Yellow to Dark Yellow
    elif i < 255 * 12:
        b -= 1  # Dark Yellow to Brown
    elif i < 255 * 13:
        r += 1  # Brown to Dark Red
    elif i < 255 * 14:
        g += 1  # Dark Red to Pink
    elif i < 255 * 15:
        b += 1  # Pink to Violet
    elif i < 255 * 16:
        r -= 1  # Violet to Purple
    elif i < 255 * 17:
        g -= 1  # Purple to Dark Blue
    elif i < 255 * 18:
        b -= 1  # Dark Blue to Black
    
    # Ensure RGB values are within the valid range
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)
    
    fd(50 + i)
    rt(91)
    pencolor(r, g, b)

hideturtle()
done()
