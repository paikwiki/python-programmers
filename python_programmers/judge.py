class Judge:
    def __init__(self):
        self.answer = None

    def set_answer(self, answer):
        self.answer = answer

    def grade(self, userAnswer):
        return self.answer == userAnswer
