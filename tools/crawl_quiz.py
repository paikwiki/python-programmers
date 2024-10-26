import argparse
import re

import requests
from bs4 import BeautifulSoup


def fetch_data(url: str):
    # 임시 보정
    unformatted_inputs_and_outputs = ("courses/30/lessons/17682",)
    if url.endswith(unformatted_inputs_and_outputs):
        print("# 🚨 문제 입출력 예시 형태가 다른 문제입니다. 수정 후 사용하세요.\n")

    # HTML 페이지 가져오기
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return [], []

    soup = BeautifulSoup(response.content, "html.parser")

    # "입출력 예" 텍스트 찾기
    targets = ["입출력 예", "입출력 예제"]
    target_heading = soup.find(text=targets)
    if not target_heading:
        print('"입출력 예" 텍스트를 찾을 수 없습니다.')
        return [], []

    # "입출력 예" 다음에 오는 첫 번째 테이블 찾기
    table = target_heading.find_next("table", {"class": "table"})
    if not table:
        print("Failed to find the example table.")
        return [], []

    # 테이블의 헤더와 데이터 추출
    headers = [th.text.strip() for th in table.find_all("th")]
    data = [
        [td.text.strip() for td in row.find_all("td")]
        for row in table.find_all("tr")[1:]  # 첫 행(헤더) 제외
    ]

    return headers, data


def convert_value(value):
    """재귀적으로 값을 변환합니다."""
    try:
        # 숫자로 변환 가능하면 숫자로 변환
        return int(value)
    except ValueError:
        try:
            # 리스트로 변환 가능하면 재귀적으로 리스트 내부도 변환
            parsed_list = eval(value)
            if isinstance(parsed_list, list):
                return [convert_value(item) for item in parsed_list]
            return parsed_list
        except (SyntaxError, NameError):
            # 변환할 수 없으면 원래 값을 반환
            return value


def generate_python_script(parameters, data, url):
    # 주석으로 들어갈 칼럼 정보 생성
    header_comment = f"# {', '.join(parameters)}"

    # 데이터 리스트 생성
    data_lines = []
    for row in data:
        converted_row = [convert_value(item) for item in row]
        formatted_row = ", ".join(repr(item) for item in converted_row)
        data_lines.append(f"    ({formatted_row}),")

    # 전체 스크립트 조합
    script = f"""# {url}


def solution({', '.join(parameters[0:-1])}):
    return None


inputs_and_outputs = [
    {header_comment}
{chr(10).join(data_lines)}
]"""

    return script


def is_valid_url(url):
    """주어진 URL이 유효한 형식인지 정규식을 사용해 검사합니다."""
    # URL 유효성 검사용 정규식
    pattern = re.compile(
        r"^(https?://)?"  # http:// 또는 https:// (선택적)
        r"([a-zA-Z0-9.-]+)"  # 도메인 이름 (예: example.com)
        r"(\.[a-zA-Z]{2,6})"  # 최상위 도메인 (.com, .net 등)
        r"(:\d+)?"  # 포트 번호 (선택적)
        r"(/[a-zA-Z0-9&%_.~+-]*)*"  # 경로 (선택적)
        r"(\?[a-zA-Z0-9&%_.~+=-]*)?"  # 쿼리 문자열 (선택적)
        r"(#[-a-zA-Z0-9_]*)?$"  # 프래그먼트 식별자 (선택적)
    )

    # URL이 패턴과 일치하면 True 반환
    return re.match(pattern, url) is not None


def is_programmers_url(url):
    return url.startswith("https://school.programmers.co.kr/learn/courses/30/")


def main():
    parser = argparse.ArgumentParser(
        description="프로그래머스 웹사이트에서 입출력 예를 가져옵니다."
    )
    parser.add_argument("--url", required=True, help="문제 페이지의 URL을 입력해주세요")
    args = parser.parse_args()

    if not is_valid_url(args.url):
        print(f"유효한 URL이 아닙니다: {args.url}")
        exit(1)

    if not is_programmers_url(args.url):
        print(f"프로그래머스 문제 URL이 아닙니다: {args.url}")
        exit(1)

    headers, data = fetch_data(args.url)

    if headers and data:
        quiz = generate_python_script(headers, data, args.url)
        print(quiz)

    else:
        print("No data to display.")


if __name__ == "__main__":
    main()
