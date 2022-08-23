function solution(n, arr1, arr2) {
  const answer = []
  const parseArr1 = []
  const parseArr2 = []
  let temp
  for (let i = 0; i < arr1.length; i++) {
      temp = arr1[i].toString(2)                                        // 이진수 변환
      while (temp.length < n) {                                         // 길이가 n보다 짧으면, 앞에 0 추가
          temp = '0' + temp
      }
      parseArr1.push([...temp])
  }
  for (let i = 0; i < arr2.length; i++) {
      temp = arr2[i].toString(2)
      while (temp.length < n) {
          temp = '0' + temp
      }
      parseArr2.push([...temp])
  }
  for (let i = 0; i < parseArr1.length; i++) {
      for (let j = 0; j < parseArr1[i].length; j++) {
          if (parseArr1[i][j] === '0' && parseArr2[i][j] === '0') {     // 둘다 0이면 공백, 그 외 #
              parseArr1[i][j] = ' '
          }
          else {
              parseArr1[i][j] = '#'
          }
      }
      answer[i] = parseArr1[i].join('')                                 // 파이썬과는 다른 쪼인,,,
  }
  return answer
}