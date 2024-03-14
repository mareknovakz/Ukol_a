import logging

# Nastavení úrovně logování na DEBUG
logging.basicConfig(level=logging.DEBUG)

# Seznam prvků
list = [8, 12, 15, 20, 30, 85, 67, 50, 120, -43, 78, -10, -50, -20, 253]

# Definovana nahodna matematicka pravidla
class Rules:

    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def rule1(x):  # Cislo ze seznamu musi byt mensi nez 100
        logging.info(f"Rule 1: {x} < 100 ? {x < 100}")
        return x < 100

    @staticmethod
    def rule2(x):  # Cislo ze seznamu musi byt delitelne 2
        logging.info(f"Rule 2: {x} % 2 == 0 ? {x % 2 == 0}")
        return x % 2 == 0

    @staticmethod
    def rule3(x):  # Cislo nesmi byt zaporne
        logging.info(f"Rule 3: {x} >= 0 ? {x >= 0}")
        return x >= 0

    def filter(self):
        filtered_numbers = [number for number in self.numbers if all(rule(number) for rule in rules)]
        if not filtered_numbers:
            logging.error("No numbers passed the filter rules.")
        else:
            logging.info("Filtered Numbers: %s", filtered_numbers)
        return filtered_numbers

# Seznam pravidel
rules = [Rules.rule1, Rules.rule2, Rules.rule3]

# Instance třídy Rules
Fr = Rules(list)

# Filtrovaný seznam
filterlist = Fr.filter()

