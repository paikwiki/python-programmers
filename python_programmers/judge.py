class Judge:
    def __init__(self):
        self.answer = None

    def set_answer(self, answer):
        self.answer = answer

    def grade(self, user_answer):
        return {"user_output": user_answer, "result": self.answer == user_answer}
