function solution(files) {
  const re = /(\D+)(\d{1,5})/                           // 정규표현식, 숫자아닌것 1개 이상, 숫자인것 1~5개
  files.sort((a, b) => {
      let [aHead, aNumber] = a.match(re).slice(1, 3)    // 정규표현식으로 찾고, 헤드와 넘버로 지정
      aHead = aHead.toLowerCase()                       // 소문자~
      let [bHead, bNumber] = b.match(re).slice(1, 3)
      bHead = bHead.toLowerCase()
      if (aHead === bHead && aNumber === bNumber) {     // 헤드, 숫자 다 같으면, 그대로(0)
          return 0
      }
      if (aHead === bHead) {                            // 헤드만 같으면, 넘버 기준 오름차순
          return aNumber - bNumber
      }
      if (aHead > bHead) {                              // 헤드 사전순
          return 1
      }
      else {
          return -1
      }
  })
  return files
}