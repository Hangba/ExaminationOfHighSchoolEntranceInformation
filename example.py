from re import T
import AnalysisData

example = AnalysisData.SingleData("StandardGeneral.json","GradeOrder.json")
example.init_match()   #初始化学校代码与学校名称


print(example.match[2002]) #从学校代码返回学校名称

print(example.countGradeBySchoolCode(2003 , False))  #返回南宁三中青山校区科目等级

print(example . returnAbove(7949,"2A+4A")) #返回南宁三中五象校区2A+4A以上人数

print(example.estimate(2002,if_index_score=True)) #返回南宁二中生源评分（默认为非线性分数）


input()