from ursina import *

app = Ursina()

player = Entity(name = "O",  color = color.rgb(178, 102, 255))

cursor = Tooltip(player.name, color = player.color, origin = (0, 0), scale = 2, enabled = True)
cursor.background = False

mouse.visible = False

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

for x in range(3):
    for y in range(3):
        b = Button(parent = scene, position = (x, y))

        board[x][y] = b

        def on_click(b = b): 
            b.text = player.name
            b.color = player.color
            b.collision = False
            check_for_victory()

            if player.name == "O":
                player.name = "X"
                player.color = color.rgb(204, 255, 153)
            
            else:
                player.name = "O"
                player.color = color.rgb(178, 102, 255)

            cursor.text = player.name
            cursor.color = player.color

        b.on_click = on_click

def check_for_victory():
    name = player.name

    won = (
        (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name) or # | left column
        (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name) or # | middle column
        (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name) or # | right column

        (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name) or # - bottom
        (board[0][1].text == name and board[1][1].text == name and board[2][1].text == name) or # - middle
        (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name) or # - top

        (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name) or # /
        (board[2][0].text == name and board[1][1].text == name and board[0][2].text == name)) # \

    if won:
        print_on_screen("Hello", position=(0, 4))
        
        

            
app.run()