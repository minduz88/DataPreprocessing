# Mingyu-Kim

2021-12-04

removeEnterLine
: 엑셀 한 셀 내에 엔터라인이 들어가는 경우 각 엔터라인들을 모두 제거하고 한줄로 바꿔주는 기능.

removeEnterLine2
: removeEnterLine의 문제는 엔터라인이 없는 내용은 노트패드 등에서 ""로 안 묶임 이를 해결하기 위해 작성.
  주의 할점은 먼저 엑셀에서 엔터라인이 없는 문장들을 위해 모든 문장들을 엑셀함수 concatenate로 ""를 양쪽에 다 붙여 준 뒤
  이를 노트패드에서 "로 replace 해준다. 그 뒤 전체복사하여 해당 스크립트를 실행.
  // removeEnterLine과 removeEnterLine2를 합쳐서 만들 수 있을듯.. 더해서 removeEnterLine2의 ""를 붙이는 엑셀 작업도 녹여내면 더 좋을듯하다.
