"""작은 Git/Python 실습용 인사 프로그램."""

from __future__ import annotations

import argparse


def make_greeting(name: str) -> str:
    """Return a friendly greeting for *name*."""
    return f"안녕하세요, {name}님! Git으로 관리하는 Python 프로젝트입니다."


def main() -> None:
    parser = argparse.ArgumentParser(description="이름을 받아 인사말을 출력합니다.")
    parser.add_argument("name", nargs="?", default="실습자", help="인사할 이름")
    args = parser.parse_args()
    print(make_greeting(args.name))


if __name__ == "__main__":
    main()
