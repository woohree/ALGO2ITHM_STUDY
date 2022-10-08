const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "W.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")
const N = Number(input.shift())
const inings = input.map(i => i.trim().split(' ').map(Number))

const permutation = (arr, selectNum) => {                         // 순열 구하기 구글링!!
  let result = []
  if (selectNum === 1) return arr.map((v) => [v])
  arr.forEach((v, idx, arr) => {
    const fixer = v
    const restArr = arr.filter((_, index) => index !== idx)
    const permuationArr = permutation(restArr, selectNum - 1)
    const combineFixer = permuationArr.map((v) => [fixer, ...v])
    result.push(...combineFixer)
  })
  return result
}

const baseball = (ining, idx, score, batters) => {                // 야구 시작
  let [outCnt, base1, base2, base3] = [0, 0, 0, 0]                // 아웃 카운트, 1, 2, 3루 주자
  while (outCnt < 3) {
    if (ining[batters[idx]] === 0) {                              // 아웃
      outCnt ++
    }
    else if (ining[batters[idx]] == 1) {                          // 1루타
      score += base3
      base3 = base2
      base2 = base1
      base1 = 1
    }
    else if (ining[batters[idx]] == 2) {                          // 2루타
      score += (base3 + base2)
      base3 = base1
      base2 = 1
      base1 = 0
    }
    else if (ining[batters[idx]] == 3) {                          // 3루타
      score += (base3 + base2 + base1)
      base3 = 1
      base2 = 0
      base1 = 0
    }
    else if (ining[batters[idx]] == 4) {                          // 4루타
      score += (base3 + base2 + base1 + 1)
      base3 = 0
      base2 = 0
      base1 = 0
    }
    idx = (idx+1) % 9                                             // 타선 + 1
  }
  return [idx, score]                                             // [현재 타자, 현재 점수] 반환
}

const oneToEight = [1, 2, 3, 4, 5, 6, 7, 8]
const permBatters = permutation(oneToEight, 8)                    // 1 ~ 8로 순열 만들어 놓고,
let ans = 0
for (let i=0; i<permBatters.length; i++) {
  let batters = permBatters[i]
  batters = [...batters.slice(0, 3), 0, ...batters.slice(3)]      // 4번 타자 위치에 0번 집어넣기
  let [idx, score] = [0, 0]
  for (let j=0; j<N; j++) {
    const ining = inings[j]
    const result = baseball(ining, idx, score, batters)
    idx = result[0]
    score = result[1]
  }
  ans = Math.max(ans, score)
}
console.log(ans)