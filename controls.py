import arcade  # Import arcade to access key constants

def on_key_press(key, modifiers, keys_pressed):
    keys_pressed.add(key)

def on_key_release(key, modifiers, keys_pressed):
    if key in keys_pressed:
        keys_pressed.remove(key)
