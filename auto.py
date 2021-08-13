from pyautogui import press, typewrite
import pyautogui
from pyperclip import copy

pyautogui.FAILSAFE = False


def do_all_actions(promo_code: str):
    copy(promo_code)
    press('F2')
    print(promo_code)
    typewrite(promo_code)