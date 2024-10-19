from unittest import TestCase

from python_programmers.judge import Judge


class JudgeTest(TestCase):
    def test_judge_is_defined(self):
        # when
        judge = Judge()

        # then
        self.assertTrue(judge)

    def test_정답을_설정할_수_있다(self):
        # given
        answer = 42
        judge = Judge()

        # when
        judge.setAnswer(answer)

        # then
        self.assertTrue(judge.answer == answer)

    def test_유저의_정답과_실제_정답이_일치하면_True_를_반환한다(self):
        # given
        answer = 42
        userAnswer = 42
        judge = Judge()
        judge.setAnswer(answer)

        # when
        result = judge.grade(userAnswer)

        # then
        self.assertTrue(result)
