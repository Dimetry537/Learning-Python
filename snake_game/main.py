from ctypes import Union
import sys
from game import Game
from PyQt5 import QtGui, QtWidgets
from ui.grid import Grid
from PyQt5.QtCore import QTimer, Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, game):
        super().__init__()
        self.size = 1500
        self.step = 50
        # coordinates cuntes as left corner
        self.game = game
        self.player_input = None

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(self.size, self.size)
        canvas.fill(QtGui.QColor("white"))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.setFixedSize(self.size, self.size)

        self.__render_grid()
        
    def tick(self):
       self.game.play(self.player_input)
       self.__render_snake()
       self.__render_apple()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0 == Qt.Key.Key_Up:
            self.player_input = 'up'
        if a0 == Qt.Key.Key_Down:
            self.player_input = 'down'

        # TODO: add left and right
        return super().keyPressEvent(a0)
   
    def __render_grid(self):
        grid = Grid(self.label, self.size, self.step)
        grid.render()

    def __render_snake(self):
        # TODO: get snake from game and based on size render filled rectangles
        pass

    def __render_apple(self):
        # TODO: get apple from game and based on size render filled rectangle
        pass

    def __convert_coordinates(self, x, y) -> Union[int, int]:
        # преобразуем координаты 50 -> 1 (суть в сжатии)
        pass

game = Game()
app = QtWidgets.QApplication(sys.argv)
window = MainWindow(game)
window.show()
timer = QTimer()
timer.timeout.connect(window.tick)
timer.start(1000)
app.exec_()