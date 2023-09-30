#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
#создание элементов интерфейса
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')
#привязка элементов к вертикальной линии
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)
#обработка событий
def show_winner():
    number = randint(0, 99)
    text.setText('Победитель:')
    winner.setText(str(number))

button.clicked.connect(show_winner)

main_win.show()
app.exec_()
#запуск приложения

