import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    
def student2dict(self):
        return {
            'name':self.name,
            'age':self.age,
            'score':self.score
        }
s=Student('Bob',20,88)
eval()
print(type(json.dumps(s,default=student2dict)))
print(json.dumps(s,default=student2dict))
