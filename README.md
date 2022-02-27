# ALGO2ITHM STUDY in SEOUL-5

`2022-02-04 알고리즘 스터디 시작 - 공영경, 마주리, 배한빈, 이우현`

## 주의 사항.

- **`작업과 push는 반드시 본인 브랜치에서!`**
- **`$ git pull origin master (본인 브랜치에서)`**
- [**`ALGO2ITHM Notion`**](https://algo2ithm.notion.site/AlGO2ITHM_STUDY-c0ca1a1760fc441da038cf033f7e0b95)

## 언어.

- Python

## 파일명.

- 사이트명\문제명\코드 파일
  - `baekjoon\월\날짜\문제\<이름 혹은 ID>.py`

## 규칙.

- 주 5개 이상 목표!
- 일지 당일 작성 권장!
- merge는 모임끝나고 한번에!
- branch 명은 이름 혹은 ID
- commit -m 는 자유롭게!

## 일정.

- 월요일 - 금토일 동안 푼 문제 피드백
- 목요일 - 화수 동안 푼 문제 피드백
- 일요일 - 별일 있는 경우

## 알고리즘 사이트.

- baekjoon: https://www.acmicpc.net/
- programmers: https://programmers.co.kr/learn/challenges
- hackerrank: https://www.hackerrank.com/
- leetcode: https://leetcode.com/
- codeground: https://www.codeground.org/about
- synap: http://euler.synap.co.kr/
- topcoder: https://www.topcoder.com/
- algospot: https://algospot.com/judge/problem/list/
- swexpertacademy: https://www.swexpertacademy.com/main/main.do
- geeksforgeeks: https://www.geeksforgeeks.org/
- codeforces: [http://codeforces.com](http://codeforces.com/)

## 사용법.

1. ALGO2ITHM_STUDY를 본인의 로컬 PC로 가져갑니다.

   ```bash
   $ git clone https://github.com/woohree/ALGO2ITHM_STUDY.git
   ```

2. 브랜치를 생성합니다. ref) https://goddaehee.tistory.com/274

   ```bash
   $ git branch woohree(예시)  # 브랜치 생성(ID, 이름 등 자유롭게)
   $ git switch woohree  # 생성한 브랜치로 이동
   ```

3. 풀이한 .py 파일을 생성한 브랜치에 업로드합니다. ref) https://victorydntmd.tistory.com/91

   ```bash
   # 현재 브랜치는 생성한 브랜치(woohree)
   $ git add.
   $ git commit -m '성공!'
   
   # 브랜치를 생성하고 처음 푸시하는 경우에만 --set-upstream 명령어가 필요
   $ git push --set-upstream origin woohree
   # 처음 이후
   $ git push origin woohree
   ```

4. Pull request를 작성합니다. ref) https://epicarts.tistory.com/98

   - 깃허브 상단의 Pull requests 클릭
   - Compare & pull request 버튼이 있을 시, 반드시 본인의 브랜치명을 확인하고 클릭
   - 없을 시, New pull request 버튼을 클릭하고, compare 란의 브랜치를 본인의 브랜치명으로 고른 뒤 Create pull request 클릭
   - 내용 작성(optional) 후 Create pull request 클릭

5. 관리자가 모든 request를 merge하면 최신 버전의 ***master***브랜치를 pull 하고, 본인의 브랜치에서 3~5를 반복합니다.

   ```bash
   # 최신 버전 pull
   # 현재 브랜치는 생성한 브랜치
   $ git pull origin master
   ```

