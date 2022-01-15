from konlpy import Okt

text = "챗봇 프로젝트 형태소 분석기 테스트"

Okt = Okt()
test = Okt.nous(text)
print(test)
