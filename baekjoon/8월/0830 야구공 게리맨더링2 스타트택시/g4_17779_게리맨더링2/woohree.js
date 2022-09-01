const fs = require('fs')
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'W.txt'
const input = fs.readFileSync(filePath).toString().trim().split('\n')
const N = Number(input.shift())
const arr = input.map(i => i.trim().split(' ').map(Number))


const gary = (x, y, d1, d2) => {
  const cnts = [0, 0, 0, 0, 0]
  const mat = Array.from(Array(N), () => Array(N).fill(0))

  for (let i=0; i<=d1; i++) {                       // 경계선(/)
    mat[x+i][y-i] = 5
    mat[x+d2+i][y+d2-i] = 5
  }
  for (let j=0;j<=d2; j++) {                        // 경계선(\)
    mat[x+j][y+j] = 5
    mat[x+d1+j][y-d1+j] = 5
  }

  for (let r=0; r<x+d1; r++) {                      // 1번 선거구
    let c = 0
    while (mat[r][c] === 0 && c <= y) {
      cnts[0] += arr[r][c]
      c ++
    }
  }
  for (let r=0; r<=x+d2; r++) {                     // 2번 선거구
    let c = N-1
    while (mat[r][c] === 0 && c > y) {
      cnts[1] += arr[r][c]
      c --
    }
  }
  for (let r=x+d1; r<N; r++) {                      // 3번 선거구
    let c = 0
    while (mat[r][c] === 0 && c < y-d1+d2) {
      cnts[2] += arr[r][c]
      c ++
    }
  }
  for (let r=x+d2+1; r<N; r++) {                    // 4번 선거구
    let c = N-1
    while (mat[r][c] === 0 && c >= y-d1+d2) {
      cnts[3] += arr[r][c]
      c --
    }
  }
  cnts[4] = total - cnts.reduce((a, b) => a + b, 0) // 5번 선거구(전체(total)에서 1~4번 선거구 인구 빼기)
  return Math.abs(Math.max(...cnts) - Math.min(...cnts))
}


let total = 0
for (let i=0; i<arr.length; i++) {
  for (let j=0; j<arr[0].length; j++) {
    total += arr[i][j]
  }
}

let ans = 99999999
for (let x=0; x<N; x++) {
  for (let y=0; y<N; y++) {
    for (let d1=1; d1<N; d1++) {
      for (let d2=1; d2<N; d2++) {
        if (x+d1+d2 < N && y-d1 >= 0 && y+d2 < N) {
          ans = Math.min(ans, gary(x, y, d1, d2))
        }
      }
    }
  }
}
console.log(ans)