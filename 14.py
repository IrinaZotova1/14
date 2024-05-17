# Приложение выводит по дате рождения животное, которое Вам подходит. Название животного берется из списка
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt5 import uic


class AnimalCompatibilityApp(QMainWindow):
    def __init__(self):
        super(AnimalCompatibilityApp, self).__init__()
        uic.loadUi('primer_animal.ui', self)
        self.setWindowTitle('Animal Compatibility Calculator')

        self.layout = QVBoxLayout()
        self.date_input = self.findChild(QLineEdit, 'line')
        self.calculate_button = self.findChild(QPushButton, 'Button')
        self.result_label = self.findChild(QLabel, 'label')
        self.cartin_label = self.findChild(QLabel, 'label_cartin')
        self.date_input.setPlaceholderText(f"YYYY-MM-DD")

        self.calculate_button.clicked.connect(self.calculate_animal_compatibility)

    def calculate_animal_compatibility(self):
        date = self.date_input.text()
        if len(date) == 10:
            animal = determine_animal_compatibility(date)
            self.result_label.setText(f'Ваше животное - {animal}')
        else:
            self.result_label.setText('Неверно введена дата')


def determine_animal_compatibility(date):
    animals = ['Собака', 'Кошка', 'Лошадь', 'Рыба', 'Кролик', 'Тигр', 'Змея', 'Обезьяна', 'Свинья', 'Дракон', 'Овца',
               'Петух', 'Бык']
    day = int(date.split('-')[-1])
    return animals[day % len(animals)]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    animal_app = AnimalCompatibilityApp()
    animal_app.show()
    sys.exit(app.exec_())