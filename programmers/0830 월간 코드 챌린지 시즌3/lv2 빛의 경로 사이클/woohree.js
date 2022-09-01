function solution(grid) {
  const answer = []
  const moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  const visited = Array.from(Array(grid.length), () =>
                             Array.from(Array(grid[0].length), () => 
                                        Array(4).fill(0)
                                       )
                            )                           // [[[0, 0, 0, 0], [0, 0, 0, 0]], ... ] => 각 방향마다 visited 체크해서 4방향 모두 방문했으면 사이클 돈 것으로 판단
  const check = (r, c, i) => {
      let cnt = 0
      while (1) {
          if (visited[r][c][i]) break

          visited[r][c][i] = 1
          r += moves[i][0]
          c += moves[i][1]
          cnt ++
          
          if (r < 0) r = grid.length - 1                // 상하좌우 벗어나는 애들 조정
          if (r >= grid.length) r = 0
          if (c < 0) c = grid[0].length - 1
          if (c >= grid[0].length) c = 0
          
          if (grid[r][c] === 'L') i = [3, 0, 1, 2][i]   // -1%4 하면 js는 -1이 나옴... 그래서 억지로 배열 만들어서 좌우 방향 정함
          if (grid[r][c] === 'R') i = [1, 2, 3, 0][i]
      }
      return cnt
  }
      
  visited.forEach((row, rowIdx) => {
      row.forEach((col, colIdx) => {
          col.forEach((route, routeIdx) => {
              if (!route) answer.push(check(rowIdx, colIdx, routeIdx))
          })
      })
  })
  
  return answer.sort((a, b) => a - b)
}