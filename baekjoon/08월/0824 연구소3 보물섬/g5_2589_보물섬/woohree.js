const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "W.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")
const [N, M] = input.shift().split(' ').map(Number)
const arr = input.map(i => i.split(''))

const bfs = (r, c) => {
  const news = []
  const moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  const visited = Array.from(Array(N), () => Array(M).fill(0))
  news.push([r, c])
  visited[r][c] = 1
  let maxDist = 0

  while (news.length) {
    const now = news.shift()
    for (let i=0; i<4; i++) {
      const newR = now[0] + moves[i][0]
      const newC = now[1] + moves[i][1]
      if (0 <= newR && newR < N && 0 <= newC && newC < M && !visited[newR][newC] && arr[newR][newC] == 'L') {
        news.push([newR, newC])
        visited[newR][newC] = visited[now[0]][now[1]] + 1
        maxDist = Math.max(maxDist, visited[newR][newC])      // 도달할 수 있는 가장 먼 지점까지의 소요 시간
      }
    }
  }
  return maxDist - 1
}

let ans = 0
for (let i=0; i<N; i++) {                                     // 모든 'L'에 대해 bfs를 다 돌려서, 가장 먼 지점 사이의 소요 시간을 구함
  for (let j=0; j<M; j++) {
    if (arr[i][j] === 'L') {
      ans = Math.max(ans, bfs(i, j))
    }
  }
}
console.log(ans)