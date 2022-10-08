const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "W.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")
const [N, M] = input.shift().split(' ').map(Number)
const arr = input.map(i => i.trim().split(' ').map(Number))

const getCombinations = (arr, n) => {                             // 조합 구하기, 구글링 좀 했습니다...
  if (n === 1) {
    return arr.map(v => [v])
  }
  const result = []
  arr.forEach((fixed, index, origin) => {                         // fixed: 현재 인자, index: 현재 인덱스, origin: arr(기존 배열)
    const rest = origin.slice(index+1)                            // 중복x -> 다음 인덱스부터 자르기
    const combinations = getCombinations(rest, n-1)               // 자른 걸로 다시 재귀
    const attached = combinations.map(v => [fixed, ...v])         // combinations 결과 받아서 현재 인자에 붙이기
    result.push(...attached)
  })
  return result
}

const bfs = (viruses, cnt) => {                                   // bfs
  if (cnt === 0) {                                                // 빈 공간이 없는 경우
    return 0
  }
  const news = []
  const visited = Array.from(Array(N), () => Array(N).fill(0))
  viruses.forEach(virus => {
    news.push(virus)
    visited[virus[0]][virus[1]] = 1
  })
  while (news.length) {
    const now = news.shift()
    for (let m=0; m<4; m++) {
      const newR = now[0] + moves[m][0]
      const newC = now[1] + moves[m][1]
      if (0 <= newR && newR < N && 0 <= newC && newC < N && !visited[newR][newC] && arr[newR][newC] !== 1) {
        news.push([newR, newC])
        visited[newR][newC] = visited[now[0]][now[1]] + 1
        if (arr[newR][newC] === 0) {                              // 0인 경우에만 전염되므로
          cnt--
          if (cnt === 0) {                                        // 빈 공간 없어지면 return
            return visited[newR][newC] - 1
          }
        }
      }
    }
  }
  return -1                                                       // 빈 공간이 남은 경우
}

let cntVirus = 0
const viruses = []
const moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for (let i=0; i<N; i++) {
  for (let j=0; j<N; j++) {
    if (arr[i][j] === 0) {
      cntVirus += 1
    }
    else if (arr[i][j] === 2) {
      viruses.push([i, j])
    }
  }
}

const virusCombis = getCombinations(viruses, M)
let ans = 9999999
let minusCnt = 0
for (let i=0; i<virusCombis.length; i++) {
  const viruses = virusCombis[i]
  const cntCopy = cntVirus
  const temp = bfs(viruses, cntCopy)
  if (temp === -1) {                                                // -1이 virusCombis 갯수와 같으면 ans = -1
    minusCnt++
  }
  else {
    ans = Math.min(ans, temp)
  }
  if (minusCnt === virusCombis.length) {
    ans = -1
  }
}
console.log(ans)
