class Maid():
    """
    Класс Служаночки.
    Содержит в себе состояние служаночки на данный момент, а так же всю информацию про нее
    """

    # Конструктор класса
    def __init__(self):
        self.name = "Служаночка"

    # Узнать имя Служаночки
    def get_name(self):
        return self.name

