function solution(str1, str2) {
  let answer = 0
  const regex = /^[a-z]+$/                    // 정규표현식!!
  str1 = str1.toLowerCase()                   // 전부 소문자로 바꾸기
  str2 = str2.toLowerCase()
  const regexStr1 = []
  const regexStr2 = []
  let temp
  for (let i = 0; i < str1.length-1; i++) {   // 정규표현식 체크(알파벳만 있는지)
      temp = str1[i]+str1[i+1]
      if (regex.test(temp)) {
          regexStr1.push(temp)        
      }
  }
  for (let i = 0; i < str2.length-1; i++) {
      temp = str2[i]+str2[i+1]
      if (regex.test(temp)) {
          regexStr2.push(temp)        
      }
  }
  const intersection = []
  regexStr1.forEach(str => {
      let idx = regexStr2.indexOf(str)        // 같은게 있으면, 교집합에 추가하고 str2에서는 제거
      if (idx >= 0) {                         // 합집합을 두 배열 그대로 더하기 때문
          intersection.push(str)
          regexStr2.splice(idx, 1)
      }
  })
  const union = [...regexStr1, ...regexStr2]
  if (regexStr1.length === 0 && regexStr2.length === 0) {
      return 65536
  }
  answer = Math.floor((intersection.length / union.length) * 65536)
  return answer
}