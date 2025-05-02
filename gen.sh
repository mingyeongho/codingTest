#!/bin/bash

# 폴더 이름이 제공되었는지 확인
if [ -z "$1" ]; then
    echo "사용법: $0 <폴더이름>"
    exit 1
fi

# 폴더 생성
mkdir -p "$1"

# 빈 solution.py 파일 생성
touch "$1/solution.py"

# 빈 README.md 파일 생성
touch "$1/README.md"

echo "폴더 '$1'와 빈 파일들이 생성되었습니다."