

현재 개발 중 (Under construction) 

---

# What is this?

창작물을 위한 세계관의 작성을 돕는 웹 어플리케이션입니다.

# What does this do?

- [ ] 회원 가입 기능
- [ ] 세계관 관리 기능
- [ ] 문서 작성 기능
- [ ] 검색 기능
- [ ] 공유 기능

# How to run?

## Requirements

- Python 3.9
- npm

## Install

```Bash
# clone repository
git clone git@github.com:pjc1991/uniwiki.git

# move to project directory
cd uniwiki

# create virtual environment
python -m venv venv

# Install pipenv
pip install pipenv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pipenv install

# install npm packages
npm install

# migrate django modules
python manage.py migrate

# deactivate virtual environment
deactivate
```


## Run

```Bash
# Activate virtual environment
source venv/bin/activate

# build tailwind css
npx tailwindcss -i ./static/css/base.css -o ./static/css/tailwind.css --watch

# Run server
pipenv run python manage.py runserver
```

---
# Roadmap
\*\ : 필수 구현 사항

- 회원가입 * : 이메일 주소와 비밀번호(암호화)만 저장. (최소의 개인 정보)
    - 이메일 인증 : AWS SES(Simple Email Service) 사용. (권한 필요.)
- 로그인 * : 이메일을 이용한 로그인.
    - SNS 로그인
    - 로그인 정보 캐싱
        - 레디스 캐싱 서버 이용.
- 세계 * : 등장인물 등의 문서를 저장하는 폴더의 개념.
    - 세계 생성 * : 세계 이름.
    - 세계 목록 조회 *
    - 세계 하위 문서 조회 *
    - 세계 수정 *
    - 세계 삭제 *
    - 세계관 공유 *
        - 세계관 URL 생성 *
        - 세계관 공개/비공개 설정
        - 비공개 세계관 초대 *
- 문서 * : 세계의 하위에 속하는 모든 작성물들.
    - 문서 작성 * : 문서 종류, 문서
    - 문서 조회 *
    - 문서 수정 *
    - 문서 삭제 *
    
    - 캐릭터 * : 등장인물
    - 설정 * : 등장인물이 아닌 문서
    - 관계 : 문서와 문사 간의 관계를 나타내는 문서
    
- 통합 검색 기능
    - 모든 문서들을 한번에 검색하여 해당 내용이 포함된 문서들을 리스트함.
    - 제목에 포함된 문서, 내용에 포함된 문서, 위의 문서들과 관계가 있는 문서 순서대로 리스트함.
