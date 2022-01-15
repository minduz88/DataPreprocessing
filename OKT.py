import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from konlpy.tag import Twitter 
from konlpy.tag import Okt 
twitter = Twitter() 
okt = Okt() 
print(twitter.morphs(u'단독입찰보다 복수입찰의 경우')) 
print(okt.morphs(u'단독입찰보다 복수입창의 경우'))


