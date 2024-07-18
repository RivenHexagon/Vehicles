# controls.py
import arcade

def on_key_press(obj, symbol, modifiers):
    """Handle user keyboard input
    Q: Quit the game
    P: Pause/Unpause the game
    I/J/K/L: Move Up, Left, Down, Right
    Arrows: Move Up, Left, Down, Right
    Arguments:
        symbol {int} -- Which key was pressed
        modifiers {int} -- Which modifiers were pressed
    """

    if symbol == arcade.key.Q:
        # Quit immediately
        arcade.close_window()

    if symbol == arcade.key.W or symbol == arcade.key.UP:
        obj.player.change_y = 5

    if symbol == arcade.key.S or symbol == arcade.key.DOWN:
        obj.player.change_y = -5

    if symbol == arcade.key.A or symbol == arcade.key.LEFT:
        obj.player.change_x = -5

    if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
        obj.player.change_x = 5

def on_key_release(self, symbol: int, modifiers: int):
    """Undo movement vectors when movement keys are released
    Arguments:
        symbol {int} -- Which key was pressed
        modifiers {int} -- Which modifiers were pressed
    """

    if (
        symbol == arcade.key.W
        or symbol == arcade.key.S
        or symbol == arcade.key.UP
        or symbol == arcade.key.DOWN
        ):
        self.player.change_y = 0

    if (
        symbol == arcade.key.A
        or symbol == arcade.key.D
        or symbol == arcade.key.LEFT
        or symbol == arcade.key.RIGHT
        ):
        self.player.change_x = 0