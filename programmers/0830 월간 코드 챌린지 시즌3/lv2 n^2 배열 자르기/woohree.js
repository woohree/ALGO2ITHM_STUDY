/*
각 칸마다 수는,
max(rIdx, cIdx) + 1

이때, 각 좌표는,
r = floor(left / n)
c = left % n

따라서, 아래 코드로 구현!
*/

function solution(n, left, right) {
  const answer = []
  while (left <= right) {
      const number = Math.max(Math.floor(left / n), left % n) + 1
      left ++
      answer.push(number)
  }
  return answer
}