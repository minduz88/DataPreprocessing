# Min-Gyu Kim Latest Update 2022.01.16
원천(Row) 데이터에 대한 여러가지 방법의 정제와 분석에 대해 관심이 많아왔던 터에, 업무에서 사용해보거나 배웠던 것들 위주로 하나하나 정리해 보고자 한다.

## 1. CSV파일은 콤마(Comma) 단위로 구분되어진 데이터이며, TSV파일은 탭(Tab) 단위로 구분되어진 데이터이다 아래의 두 코드는 CSV파일을 TSV파일로 변환시켜준다.
converter_CSVtoTSV
: CSV파일을 TSV파일로 변환하는 스크립트.

converter_CSVtoTSV2
: converter_CSVtoTSV와 기능은 동일하나 내부적으로 split(), join() 함수로 바꿔서 만들어 봄.

## 2. 
splitColum
: CSV파일을 행 단위로 읽는 스크립트.

splitColum2
: 기존 open을 with open으로 바꿈

splitColum3
: 행 단위가 아닌 문서 내 텍스트 전체를 통으로 읽어낸다.

## 3. 
converter_SplitColumn&Row
: CSV파일 2차원 행, 열 분절 코드

converter_SplitColumn&Row2
: CSV파일, reader() 사용

converter_SplitColumn&Row3
: CSV파일, dictionary() 사용

converter_SplitColumn&Row4
: TSV파일 행, 열 분절

converter_SplitColumn&Row5
: collection 모둘의 defaultdict() 사용

converter_DictionarytoJSON
: 딕셔너리를 JSON파일로 저장

converter_JSONtoDictionary
: JSON파일을 딕셔너리로 저장

converter_JSONtoTSV
: 딕셔너리를 JSON파일로 저장

## 4. 
split_fromUnstructuredText
: 문장 어절 분리

split_fromUnstructuredText2
: 분리 된 어절에 대한 빈도 카운트

split_fromUnstructuredText3
: 행 바꿈 문자에 의한 분리는 단락의 분리이며, 한 단락에는 여러 문장이 포함되어 있음, 각 단락에 포함 된 여러 문장을 추가로 분리해야 됨.

split_fromUnstructuredText4
: 문장 추가 분리 부분을 모듈화


## 5.데이터를 정제하다보니 행 단위로 분절하는 여러가지 경우들에 대해선 여러 소스코드가 존재했지만 반대로 행 단위로 한줄로 이어 붙이는 방법이 필요할 때도 있었다. 나같은 경우는 학습모델에 대해 학습시킬 대상의 Row data에 쓸데없이 많은 개행과 탭 구분이 들어가 있는 바람에 온전히 하나의 문장으로 인식시키는게 어려운 경우가 있었고 이를 해결해보기 위해 아래와 같은 removeEnterLine, removeEnterLine2와 같은 방법들이 필요하게 되었다.
removeEnterLine
: 엑셀 한 셀 내에 엔터라인이 들어가는 경우 각 엔터라인들을 모두 제거하고 한줄로 바꿔주는 코드.

removeEnterLine2
: removeEnterLine의 문제는 엔터라인이 없는 내용은 노트패드 등에서 ""로 안 묶임 이를 해결하기 위해 작성. 주의 할점은 먼저 엑셀에서 엔터라인이 없는 문장들을 위해 모든 문장들을 엑셀함수 concatenate로 ""를 양쪽에 다 붙여 준 뒤 이를 노트패드에서 "로 replace 해준다. 그 뒤 전체복사하여 저장 후 해당 코드를 실행.
(+ removeEnterLine과 removeEnterLine2를 합쳐서 만들 수 있을듯.. 더해서 removeEnterLine2의 ""를 붙이는 엑셀 작업도 녹여내면 더 좋을듯하다.)

## 6.
webCrawler
: 공공데이터 웹 수집기

## 7.
callGetTag
: 설정한 태깅 대상 추출