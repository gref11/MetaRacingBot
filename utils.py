import pygetwindow as gw
import ctypes


class WindowError(Exception):
    pass


def get_scaling_factor(win_name):
    window = gw.getWindowsWithTitle(win_name)
    hwnd = window[0]._hWnd
    
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32
    dpi = user32.GetDpiForWindow(hwnd)
    
    default_dpi = 96
    
    scaling_factor = dpi / default_dpi

    return scaling_factor
