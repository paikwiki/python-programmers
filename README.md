# Programmers 문제풀이 도구(for Python)

프로그래머스 문제를 로컬에서 풀이할 수 있도록 도와주는 도구입니다.

## 실행 방법

`./quizzes/c30l120803.py`에서 작성 예시를 확인할 수 있습니다.

```python
def solution(num1, num2):
    return num1 - num2


inputs_and_outputs = [
    (2, 3, -1),
    (100, 2, 98),
]
```

프로그래머스 문제에 제시된 `solution()` 함수의 파라미터와 `c30l120803.py`의 `solution()` 함수의 파라미터를 동일하게 작성한 후, `solution()` 함수를 완성합니다.

`inputs_and_outputs`에는 입력값과 출력값을 튜플로 갖는 리스트를 작성합니다. 튜플의 맨 마지막 값이 출력값입니다. 즉 첫 번째 리스트 아이템 `(2, 3, -1)`에서 `2`, `3`은 각각 함수의 인자 `num1`, `num2`이고, `-1`은 기대하는 출력값입니다.

작성 후에는 아래처럼 테스트를 실행해볼 수 있습니다.

```sh
$ poetry run submit --target=quizzes/c30l120803.py
🟢 TestCase #1: Success
🔴 TestCase #2: Failure
 - yours:       99
 - expected:    98
 - input:       (100, 2)
$
```

## 임시 도구 - 문제 입출력 가져오기

아래 명령으로 문제의 입출력 데이터와 빈 `solution()` 함수를 화면에 출력할 수 있습니다.

```sh
$ poetry run crawl --url=https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score, result):
    return None


inputs_and_outputs = [
    # k, m, score, result
    (3, 4, [1, 2, 3, 1, 2, 3, 1], 8),
    (4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2], 33),
]
```

이 명령과 쉘 리디렉션을 함께 활용해서 문제 입출력 데이터를 파일에 세팅할 수 있습니다.

```sh
$ poetry run crawl --url=https://school.programmers.co.kr/learn/courses/30/lessons/135808 > quizzes/c30l135808.py
```

> 이 기능은 ChatGPT를 이용해 생성했으며, 프로그래머스의 모든 문제에 대응하지 못하는 임시 기능입니다.
