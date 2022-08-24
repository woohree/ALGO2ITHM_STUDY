function solution(m, musicinfos) {
  const arr = musicinfos.map(music => {
      const [s, e, title, codes] = music.split(',')
      const hour = e.slice(0, 2) - s.slice(0, 2)
      const minute = e.slice(3) - s.slice(3)
      const t = hour * 60 + minute
      const codesChange = codes.match(/[A-Z]#?/g)                         // 정규표현식 알파벳 + '#'
      let realCodes = codes.repeat(Math.floor(t/codesChange.length))      // 곡 반복
      realCodes += codesChange.slice(0, t % codesChange.length).join('')  // 도중에 멈춘 경우, 그만큼 붙여주기
      return [title, t, realCodes]
  })
  const answer = arr.filter(([title, t, realCodes]) => {
      let idx = realCodes.indexOf(m)                                      // m 포함 여부 확인
      if (idx === -1) {                                                   // 안됐으면 false (filter에서 걸러짐)
          return false
      }
      while (idx !== -1) {                                                // 맨 뒤에 '#'이 있으면, 일치x
          if (realCodes[idx+m.length] !== '#') {
              return true
          }
          idx = realCodes.indexOf(m, idx+1)                               // '#' 건너서 m 다시 탐색
      }
  })
  if (!answer.length) {
      return "(None)"
  }
  answer.sort((a, b) => {                                                 // sort 검색해봄..ㅋ
      if (a[1] === b[1]) {                                                // return 0 이면 순서 유지
          return 0
      }
      return b[1] - a[1]                                                  // 숫자 내림차순 정렬
  })
  return answer[0][0]
}