import pygetwindow as gw
import cv2
import mss
import time
import numpy
from utils import *



class MetaRacingBot:
    def __init__(self):
        self.win_name = 'TelegramDesktop'
        # self.win_name = 'git'


        title = ""
        sct = mss.mss()

        img = numpy.asarray(sct.grab({"top": 0, "left": 0, "width": 1, "height": 1}))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        cv2.imshow(title,  img)



    def get_window_position_and_size(self):
        try:
            # Получаем окно по его названию
            window = gw.getWindowsWithTitle(self.win_name)[0]  # Возвращает список окон с указанным заголовком
            if window is not None:
                # Получаем позицию и размеры окна
                position = (window.top, window.left)
                size = (window.width, window.height)
                return position, size
            else:
                raise WindowError("Окно не найдено!")
        except IndexError:
            raise WindowError("Окно с таким названием не найдено.")
        except Exception as e:
            raise WindowError(f"Произошла ошибка: {e}")
    
    def screen_record(self):
        while True:
            # scaling_factor = get_scaling_factor(self.win_name)
            scaling_factor = 1
            (top, left), (width, height) = self.get_window_position_and_size()
            win = {"top": int(top * scaling_factor + 11), "left": int(left * scaling_factor + 15), "width": int(width * scaling_factor) - 30, "height": int(height * scaling_factor) - 22}
            # print(win)

            title = ""
            sct = mss.mss()


            img = numpy.asarray(sct.grab(win))
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            cv2.imshow(title,  img)
            
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                return



if __name__ == '__main__':
    mrb = MetaRacingBot()
    # print(mrb.get_window_position_and_size())
    try:
        mrb.screen_record()
    except Exception as e:
        print(e)

