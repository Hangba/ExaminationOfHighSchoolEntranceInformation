import json,time
import os


class SingleData:

    def __init__(self,filepath,gradeOrder = None):

        #初始化
        self.types = ["instruction","directional","guide"]
        self.match = {}#code 对应 name
        self.school_code_list=[ 2001,2002,2003,7949,2004,2005,2008,2009,\
                                2010,2083,2013,2014,7647,2091,2019,2020,\
                                2021,2024,2026,2028,2029,2033,2034,2036,\
                                8081,2099,2114,2100,2101,2112,2097,2113,\
                                7579,2063,2086,2080,2030,8022,8021,2092,\
                                2087,2089,8105,7879,7911,2109,8083,8082,\
                                2094,7908,8056,7967]
        self.grades = ["A+","A","B+","B","C+","C","D","E"]
        if bool(gradeOrder):
            with open(gradeOrder) as f:
                self.order = eval(f.read())
        
                


        #读取文件数据，因数据结构过乱，被迫使用eval读取
        file = open(filepath,"r",encoding="utf8")
        content = eval(file.read())
        file.close()

        #存储到self中
        self.time = content["time"]
        self.data = content["data"]

    def init_gradeOrder(self,gradeOrder):
        #初始化等级列表
        with open(gradeOrder) as f:
            self.order = eval(f.read())

    def init_match(self):
        for school in self.school_code_list:
            original_data = self.data[school]
            for t in self.types:
                #循环入学方式
                data = original_data[t]['result']
                if bool(data):  #有些学校不存在三种入学方式之一，需要排除
                    l = json.loads(data)
                    self.match[school] = l["schoolName"]
                    
    
    def getBySchoolCode(self,schoolCode,IFMERGE = False):
        #根据学校代码返回报名数据,{"instruction":[{},{}],"guide":[{},{}]}
        response = {}
        
        try:
            original_data = self.data[schoolCode]
            for t in self.types:
                #循环入学方式
                    data = original_data[t]['result']

                    if bool(data):  #有些学校不存在三种入学方式之一，需要排除
                        l = json.loads(data)
                        response[t] = l["lists"]
            
            """#print学校名
            print("学校名：",l['schoolName'])  
            #print数据获取时间
            timeArray = time.localtime(self.time)
            print(time.strftime("%Y-%m-%d %H:%M:%S", timeArray))"""


        except KeyError as e:
            print("不存在此学校！",str(e))
        
        finally:
            if IFMERGE:
                v = list(response.values())
                sumList = []
                for x in v:
                    sumList+=x
                return sumList
            else:
                return response


    def returnAbove(self,schoolCode,grade):
        #返回给定等级之上的人的个数
        

        #合并三个方式的数据
        data = self.getBySchoolCode(schoolCode,True)
        
        
        try:
            counting = 0
            target_order = self.order.index(grade) #目标等级位置
            for student in data:
                currentOrder = self.order.index(student["CombinedScore"])
                if currentOrder<=target_order:  #如果当前等级更靠前
                    counting+=1  #计数加1

        except KeyError:
            print("等级输入错误！")
        finally:
            return counting
        

    def countGradeBySchoolCode(self,schoolCode,ifsum = False):
        #计数等级
        #ifsum True返回总分等级 False:返回各科等级
        
        count_dict = {}
        def dictc(element,dict):
            #字典计数
            if element not in list(dict.keys()):
                dict[element] = 1
            else:
                dict[element]+=1

        data = self.getBySchoolCode(schoolCode,True)
        for student in data:
            if ifsum:
                dictc(student["SumScore"],count_dict)
            else:
                dictc(student["CombinedScore"],count_dict)

        return count_dict

    

    def estimate(self,schoolCode,if_index_score = True):
        #评价学校分数
        data = self.getBySchoolCode(schoolCode,True)

        summary = 0
        maxmium = len(self.order)
        ratio_l=[1 , 0.9 , 0.8 , 0.7 , 0.6 , 0.5 , 0.4 , 0.3]
        for student in data:
            ratio = ratio_l[self.grades.index(student["SumScore"])]
            summary += self.order.index(student["CombinedScore"])*(1-ratio/2)
        
        avg = summary/len(data)
        linear_score = round((maxmium - summary / len(data)) / maxmium,2)
        #计算指数分数
        base = 0.996
        diff = base**maxmium  #所有等级排列个数
        index_score = round((base**avg - diff) / (1-diff),4)

        #index_score = round(0.992**avg,2)
        if if_index_score:
            return index_score
        else:
            return linear_score

        



class SequenceData:
    def __init__(self,startTime,endTime, interval = 0):
        #读取数据文件
        self.fileList = list(os.walk("."))[0][2]
        self.DATA = []   #SingleData类列表

        
        print("数据起始时间：")
        timeArray = time.localtime(startTime)
        print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
        timeArray = time.localtime(endTime)
        print("结束时间：",time.strftime("%Y-%m-%d %H:%M:%S", timeArray))

        for filename in self.fileList:
            #遍历文件
            if filename[-5:] == ".json":
                #确认时间
                if startTime < int(filename[:-5]) < endTime:
                    #时间间隔interval(s)
                    data = 0
                    if self.DATA!=[]:
                        if self.DATA[-1].time+interval<int(filename[:-5]):
                            data = SingleData(filename)
                            self.DATA.append(data) 
                    else:
                        data = SingleData(filename)
                        self.DATA.append(data)
                    del data


    def getAboveBySchoolCode(self,schoolCode,grade,gradeOrder):
        #返回按时间顺序排列的已加载数据中给定学校和给定等级以上的人数列表
        res = []
        for single in self.DATA:
            #遍历所有时间顺序的json
            single.init_gradeOrder(gradeOrder)
            res.append(single.returnAbove(schoolCode,grade))
        return res

    def getScoreBySchoolCode(self,schoolCode):
        #返回按时间顺序排列的评估分数
        res = []
        for single in self.DATA:
            score = single.estimate(schoolCode)
            res.append(score)
        return res
            


    
