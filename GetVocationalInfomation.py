import requests,json,time


school_code_list=[45010006,45010007,45010008,45010009,45010010,45010011,45010027,45010028,45010014,45010015,\
                    45010016,45010017,45010018,45010029,45010020,45010030,45010022,45010023,45010024,45010025,45010026,45010031,45010032,\
                    45010033,45010034,45010035,45010036,45010037]
                                      
types = ["instruction","directional","guide"]  #非定向，定向，指导

def getbytype(schoolcode,t):
    
    url="http://www.nnzkzs.com/api/services/app/publicityDetail/GetVocationalDetail?schoolCode=%s"%str(schoolcode)
    res=requests.post(url)
    return res.json()
    
def getbyschoolcode(school_code):
    #根据学校代码返回学校报名数据
    # 教育局的数据中，result键对应的值数据形式是str
    school_data = {}
    #school_data={"instruction":{},"directional":{}...}
    for t in types:
        school_data[t] = getbytype(school_code,t)
    
    #获取学校名 由于测试环节有某些学校无非定向数据 所以需要使用try嵌套
    try:
        info = json.loads(school_data["instruction"]["result"])
    except:
        try:
            info = json.loads(school_data["directional"]["result"])
        except:
            info = json.loads(school_data["guide"]["result"])
    try:
        name = info["schoolName"]
        id = int(info["schoolCode"])
            
        print("NOW LOADING: {} ; PROGRESS: {:.4f} ".format( name, school_code_list.index(id)/len(school_code_list)))
    except:
        pass
    return school_data
        
def getall():
    r_d={}
    #r_d = {2002:{},2003:{}...}
    #循环整个学校代码列表
    for school_code in school_code_list:
        #print("Now: " +str(school_code))
        r = getbyschoolcode(school_code)
        r_d[school_code] = r
    
    save = {"time":time.time(),"data":r_d}
    with open(str(int(time.time())) + ".json","w",encoding = "utf8") as f:
        f.write(str(save))

getall()
