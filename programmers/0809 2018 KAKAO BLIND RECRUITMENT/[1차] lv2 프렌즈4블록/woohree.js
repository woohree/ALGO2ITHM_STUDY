function solution(m, n, board) {
  let answer = 0;
  board = board.map(b => b.split(''))
  while (true) {
      const boomBlocks = []
      for (let i=1; i<m; i++) {                               // 터뜨릴 좌표 찾기
          for (let j=1; j<n; j++) {
              if (board[i][j]
                  && board[i][j] === board[i-1][j]
                  && board[i][j] === board[i][j-1]
                  && board[i][j] === board[i-1][j-1]) {
                  boomBlocks.push([i, j])
              }
          }
      }
      if (!boomBlocks.length) {                               // 종료조건
          return [].concat(...board).filter(v => !v).length   // board 다 합친 다음, 0만 걸러서, 길이 = 답
      }
      boomBlocks.forEach(b => {                               // 터뜨리기
          board[b[0]][b[1]] = 0
          board[b[0]-1][b[1]] = 0
          board[b[0]][b[1]-1] = 0
          board[b[0]-1][b[1]-1] = 0
      })
      for (let i=m-1; i>0; i--) {                             // 재정렬
          if (!board[i].some(v => !v)) {                      // 0이 하나도 없으면, continue
              continue
          }
          for (let j=0; j<n; j++) {
              for (let k=i-1; k>=0 && !board[i][j]; k--) {
                  if (board[k][j]) {                          // 한 줄 씩 내리기
                      board[i][j] = board[k][j]               // 아래거를 위에 있던 놈 값으로,
                      board[k][j] = 0                         // 위에거 0으로 바꾸기
                      break
                  }
              }
          }
      }
  }
}