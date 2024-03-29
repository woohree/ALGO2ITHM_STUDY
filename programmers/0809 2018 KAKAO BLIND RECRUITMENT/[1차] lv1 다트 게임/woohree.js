function solution(dartResult) {
  let answer = 0
  const scores = []
  let score
  for (let i = 0; i < dartResult.length; i++) {
      if (dartResult[i] >= 0 && dartResult[i] < 10) {         // 숫자인 경우,
          if (dartResult[i] == 1 && dartResult[i+1] == 0) {   // 10인 경우,
              score = 10
              i++
          } 
          else {                                              // 0~9인 경우,
              score = Number(dartResult[i])
          }
      }
      else if (dartResult[i] === 'S') {
          scores.push(score)
      }
      else if (dartResult[i] === 'D') {
          scores.push(score**2)
      }
      else if (dartResult[i] === 'T') {
          scores.push(score**3)
      }
      else if (dartResult[i] === '*') {
          scores[scores.length-1] *= 2
          if (scores.length > 1) {
              scores[scores.length-2] *= 2    
          }
      }
      else if (dartResult[i] === '#') {
          scores[scores.length-1] *= -1
      }
  }
  answer = scores.reduce((acc, score) => acc + score, answer)  // reduce 한 번 써보고 싶었음^^
  return answer
}