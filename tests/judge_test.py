from unittest import TestCase

from python_programmers.judge import Judge


class JudgeTest(TestCase):
    def test_is_defined(self):
        # when
        judge = Judge()

        # then
        self.assertTrue(judge)

    def test_정답을_설정할_수_있다(self):
        # given
        answer = 42
        judge = Judge()

        # when
        judge.set_answer(answer)

        # then
        self.assertTrue(judge.answer == answer)

    def test_유저의_정답과_실제_정답이_일치하면_result가_True인_DTO를_반환한다(self):
        # given
        answer = 42
        user_answer = 42
        judge = Judge()
        judge.set_answer(answer)

        # when
        result = judge.grade(user_answer)

        # then
        self.assertEqual(result, {"user_output": user_answer, "result": True})
