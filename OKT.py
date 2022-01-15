import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


from konlpy.tag import Okt 
 
okt = Okt() 

print(okt.morphs(u'단독입찰보다 복수입창의 경우'))


