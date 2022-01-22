import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


from konlpy.tag import Okt 
 
Okt = Okt() 

print(Okt.morphs('test'))


