from oopconcepts.demoA import A
from oopconcepts.demoB import B

class C(A,B):
    def __init__(self,n1, n2, msg):
        super().__init(n1,n2)
        super().__init(msg)

    def final(self):
        print('Done')