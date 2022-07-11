import requests,json,time


school_code_list=[  2001,2002,2003,7949,2004,2005,2008,2009,\
                    2010,2083,2013,2014,7647,2091,2019,2020,\
                    2021,2024,2026,2028,2029,2033,2034,2036,\
                    8081,2099,2114,2100,2101,2112,2097,2113,\
                    7579,2063,2086,2080,2030,8022,8021,2092,\
                    2087,2089,2090,7879,7911,2109,2093,8082,\
                    2094,7908,8056,7967]
                                      
types = ["instruction","directional","guide"]  #非定向，定向，指导

def getbytype(schoolcode,t):
    d = {}
    d["schoolCode"] = schoolcode
    d["type"] = t
    d["status"] = 4

    url="http://www.nnzkzs.com/api/services/app/publicityDetail/GetGeneralDetail?schoolCode=%s&type=%s&status=4"%(str(schoolcode),t)
    res=requests.post(url,data=d)
    return res.json()
    
def getbyschoolcode(school_code):
	# 教育局的数据中，result键对应的数据形式是str
	school_data = {}
	for t in types:
		school_data[t] = getbytype(school_code,t)
	
	try:
		info = json.loads(school_data["instruction"]["result"])
	except:
		try:
			info = json.loads(school_data["directional"]["result"])
		except:
			info = json.loads(school_data["guide"]["result"])
	name = info["schoolName"]
	id = int(info["schoolCode"])
	
	print("NOW LOADING: {} ; PROGRESS: {:.4f} ".format( name, school_code_list.index(id)/len(school_code_list)))
	return school_data
		
def getall():
	r_d={}
	for school_code in school_code_list:
		#print("Now: " +str(school_code))
		r = getbyschoolcode(school_code)
		r_d[school_code] = r
	save = {"time":time.time(),"data":r_d}
	with open(str(int(time.time())) + ".json","w",encoding = "utf8") as f:
		f.write(str(save))

getall()
print("Finish")