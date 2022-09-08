# ALGO2ITHM STUDY in SEOUL-5

> 2022-02-04 알고리즘 스터디 1기 - 공영경, 마주리, 배한빈, 이우현
> 
> 2022-06-30 공영경, 마주리 - 신한은행 입행
> 
> 2022-07-11 알고리즘 스터디 2기 - 배한빈, 이우현, 이재익, 이종훈
> 
> 2022-09-01 이우현 - 우리은행 입행
> 
> 2022-09-01 알고리즘 스터디 3기 - 배한빈, 이재익, 이종훈



## 요약

- **`작업과 push는 반드시 본인 Branch에서!`**
- **`$ git pull origin master (본인 Branch에서)`**
- [**`ALGO2ITHM Notion`**](https://algo2ithm.notion.site/AlGO2ITHM_STUDY-c0ca1a1760fc441da038cf033f7e0b95)

## 언어

- `Python`

## 파일명

- 사이트명/문제명/코드 파일
  
  ex) `baekjoon/월/날짜/문제/<이름 혹은 ID>.py`

## 규칙

- 주 5개 이상 목표!
- 일지 당일 작성 권장!
- `Merge`는 모임끝나고 한번에!
- `Branch`명은 이름 혹은 ID
- `commit -m`는 자유롭게!

## 일정

- 화요일 - 문제 피드백 및 새로운 문제 선택

## 알고리즘 사이트

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

## 사용법

1. `ALGO2ITHM_STUDY`를 본인의 로컬 PC로 가져갑니다.
   
   ```bash
   $ git clone https://github.com/woohree/ALGO2ITHM_STUDY.git
   ```

2. `Branch`를 생성합니다. *ref) https://goddaehee.tistory.com/274*
   
   ```bash
   $ git switch -c <생성할 Branch명>  # Branch 생성 및 이동
   ```

3. 풀이한 `.py` 파일을 생성한 `Branch`에 업로드합니다. *ref) https://victorydntmd.tistory.com/91*
   
   ```bash
   # 현재 Branch는 생성한 Branch
   $ git add .  # 현재 폴더 기준, 하위 모든 파일 추가(혹은 특정 경로를 지정해 주어도 무방)
   $ git commit -m '성공!'
   $ git push origin <생성한 Branch명>
   ```

4. `Pull request`를 작성합니다. *ref) https://epicarts.tistory.com/98*
   
   - 깃허브 상단의 `Pull requests` 클릭
   - `Compare & pull request` 버튼이 있을 시, 반드시 본인의 `Branch`명을 확인하고 클릭
   - 없을 시, `New pull request` 버튼을 클릭하고, `compare`란의 `Branch`를 본인의 `Branch`명으로 고른 뒤 `Create pull request` 클릭
   - 내용 작성(optional) 후 `Create pull request` 클릭

5. 관리자가 모든 `request`를 `merge`하면 최신 버전의 ***master*** Branch를 `pull` 하고, 본인의 `Branch`에서 3~5를 반복합니다.
   
   ```bash
   # 최신 버전 pull
   # 현재 Branch는 생성한 Branch
   $ git pull origin master
   ```
