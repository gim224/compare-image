import mouse    
import keyboard

if __name__ == "__main__":    
    mouse.move(-700, 200, absolute=True, duration=0)
    print(mouse.get_position())
    mouse.double_click()

    keyboard.write(str(123))