import requests,json

school_code_list=[  2001,2002,2003,7949,2004,2005,2008,2009,\
                    2010,2083,2013,2014,7647,2091,2019,2020,\
                    2021,2024,2026,2028,2029,2033,2034,2036,\
                    8081,2099,2114,2100,2101,2112,2097,2113,\
                    7579,2063,2086,2080,2030,8022,8021,2092,\
                    2087,2089,2090,7879,7911,2109,2093,8082,\
                    2094,7908,8056,7967]
                    
school_code = int(input("请输入学校代码:"))
grade_list = ["A+","A","B+","B","C+","C","D","E"]

types = ["instruction","directional","guide"]  #非定向，定向，指导
respone = []

datas=[]
numberS=[]
gradeSort=[]
scorelist=[]
da=[]

sumStudent=0 #报名总数
scoreDict={}
def dictc(ele,dict):
    
    if ele not in list(dict.keys()):
        dict[ele] = 1
    else:
        dict[ele]+=1

def fill_dict(l:list):
    d = {}
    for i in l:
        d[i] = 0
    
    return d

def bprint(dict):
    # print in a more beautiful style
    s=""
    keys = list(dict.keys())
    for k in keys:
        s+= k +"  :  "+ str(dict[k] ) + "\n"
    return s



for t in types:


    d = {}
    d["schoolCode"] = school_code
    d["type"] = t
    d["status"] = 2

    url="http://www.nnzkzs.com/api/services/app/publicityDetail/GetGeneralDetail?schoolCode=%s&type=%s&status=2"%(str(school_code),t)
    res=requests.post(url,data=d)
    datas.append(res.json())
    #print(json.loads(datas[1]["result"]))

da = []
for data in datas:
    if bool(data["result"]) == 1:
        da+=json.loads(data["result"])["lists"]

for data in datas:
    if bool(data["result"]) == 1:
        info = json.loads(data["result"])
        scores  = info["lists"]
        scorelist.append(scores)
        sumStudent += len(scores)
        numberS.append(len(scores))
        scoreDict={}
        for score in scores:
            dictc(score["CombinedScore"],scoreDict)
        gradeSort.append((scoreDict))
        school_name = info["schoolName"]



#总数

scDict = {}
for sc in da:
    dictc(sc["CombinedScore"],scDict)

print(school_name+"报名信息")
print("总报名数: "+str(sumStudent))
print("非定向："+str(numberS[0]))

try:
    print("定向："+str(numberS[1]))
except:
    print("定向：0")

try:
    print("指导："+str(numberS[2]))
except:
    print("指导：0")



print("非定向：\n"+bprint(gradeSort[0]))

try:
    print("定向：\n"+bprint(gradeSort[1]))
except:
    print("定向：\n"+"None")

try:
    print("指导：\n"+bprint(gradeSort[2]))
except:
    print("指导：\n"+"None")

print("总数：\n"+bprint(scDict))
print("非定向最低一名成绩：" + "总分{} , 语文{} , 数学{} , 英语{} , 物理{} , 化学{} , 政史{} , 实验{}".format(
    scorelist[0][-1]["SumScore"],
    scorelist[0][-1]["ChineseLevel"],
    scorelist[0][-1]["MathLevel"],
    scorelist[0][-1]["EnglishLevel"],
    scorelist[0][-1]["PhysicsLevel"],
    scorelist[0][-1]["ChymistLevel"],
    scorelist[0][-1]["PoliticsLevel"],
    scorelist[0][-1]["Experiment"]
    ))

try:
    print("定向最低一名成绩：" + "总分{} , 语文{} , 数学{} , 英语{} , 物理{} , 化学{} , 政史{} , 实验{}".format(
        scorelist[1][-1]["SumScore"],
        scorelist[1][-1]["ChineseLevel"],
        scorelist[1][-1]["MathLevel"],
        scorelist[1][-1]["EnglishLevel"],
        scorelist[1][-1]["PhysicsLevel"],
        scorelist[1][-1]["ChymistLevel"],
        scorelist[1][-1]["PoliticsLevel"],
        scorelist[1][-1]["Experiment"]
        ))
except:
     print("定向最低一名成绩:None")

try:
    print("指导最低一名成绩：" + "总分{} , 语文{} , 数学{} , 英语{} , 物理{} , 化学{} , 政史{} , 实验{} ".format(
        scorelist[2][-1]["SumScore"],
        scorelist[2][-1]["ChineseLevel"],
        scorelist[2][-1]["MathLevel"],
        scorelist[2][-1]["EnglishLevel"],
        scorelist[2][-1]["PhysicsLevel"],
        scorelist[2][-1]["ChymistLevel"],
        scorelist[2][-1]["PoliticsLevel"],
        scorelist[2][-1]["Experiment"]
        ))
except:
    print("指导最低一名成绩:None")


input("按下回车退出")



    
    






"""
for t in types:
        
    url=  #http://www.nnzkzs.com/#/publicityDetail?schoolCode=%s&type=%s&status=2#%(str(school_code),t)
    html = requests.get(url)

    respone.append(html.text)

print(respone[0])

for r in respone:

    rbs = bs4.BeautifulSoup(r)

    ele = rbs.select(".ng-scope")

    print(ele[0].getText())

"""

    


