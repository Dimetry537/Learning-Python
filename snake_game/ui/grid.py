from PyQt5 import QtGui

class Grid():
    def __init__(self, label, size, step) -> None:
        self.label = label
        self.size = size
        self.step = step

    def render(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("black"))
        painter.setPen(pen)
        
        for i in range(self.size):
            painter.drawLine(0, self.step * i, self.size, self.step * i)
        for i in range(self.size):
            painter.drawLine(self.step * i, 0, self.step * i, self.size)
        painter.end()
