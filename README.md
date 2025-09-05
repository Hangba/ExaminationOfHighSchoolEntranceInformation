## 写在前面
由于nnsksz.com加入反爬系统，没有登陆cookie无法使用原来的详细报名信息api，且本人已于2024年高中毕业，故不再更新

作为二三大战曾经的参与者和见证者，真心希望两所学校越来越好

唯我校友 星聚南邕

<h1>Examination of High School Entrance Information in Nanning</h1>
 Use API provided by Education Administration to log current enroling data

## Limitations
1. School codes may change every year, you need to post to get the list of schools.
2. The functions of "status" is now unknown. But it may influence the topicality of data.

## API list:

#### Get list of vocational schools:
method:post
<http://www.nnzkzs.com/api/services/app/vocationalPublicity/GetPublicity>
#### Get list of general schools:
method:post
http://www.nnzkzs.com/api/services/app/generalPublicity/GetPublicity
#### Get enroling information of general schools:
http://www.nnzkzs.com/api/services/app/publicityDetail/GetGeneralDetail?schoolCode={1}&type={2}status={3}
need post header: 
explain:
1. {1}: **school code** -  can find in SchoolCode.xlsx. A code corresponds to a school.
2. {2}: **enroling method** - instruction,directional,guide.
3. {3}: **status** - unknown but is 2 while enroling and is 4 after ending.
#### Get enroling information of vocational schools:
http://www.nnzkzs.com/api/services/app/publicityDetail/GetVocationalDetail?schoolCode={1}
{1} identical as above


## default naming method
(time stamp).json
loading a sequence of data, use file name as time order.

## File Introduction
- GetInformationandPrint.py : Unavailiable in April and May probably. Get information online from the post's return, and print.
- AnalisisData.py
    1. It includes 2 classes.They are used for single data and sequence data respectively.
    2. The methods in class SingleData are:
        - init_gradeOrder(gradeOrder) : is used for initialise grade order
        - init_match() use for initialise the match of school code with school name
        - getBySchoolCode(schoolCode,IFMERGE = False) returns data with school code. Argument IFMERGE decides whether merge all the enroling method students whose grade is identical.
        - returnAbove(schoolCode,grade) returns the amount of the student whose grade is above the grade given(include).
        - return a dict of grade and amount of the given school by providing school code.
        - estimate(schoolCode,if_index_score=True) estimates a comprehensive school's students source.
    3. The methods in class SequenceData are (you need to put this script with all the data file):
        - getAboveBySchoolCode(self,schoolCode,grade,gradeOrder) returns a chronological list of the number of people in the data for a given school and above a given grade.
        - getScoreBySchoolCode(self,schoolCode) returns a chronological list of the estimated score for a given school code.
- AnalysisVocationalData.py : Almost identical with AnalysisData.py.
- example.py : An example to use the functions.
- GetInformation.py : Get information online and save as a file using time stamp as its name.
- GetInformationLoop.py : The function is like GetInformation.py but it keeps cycling until the time stamp you set in the file.
- GetVocationalInformation.py : Similar to GetInformation.py, but it is for vacational schools.


<h1>南宁中考报名信息</h1>
用nnzksz.com提供的api来记录当前中考报名信息

## 限制
1. 学校代码每年都有可能变化，你需要post下面的网址获取最新的school code
2. 参数“status“的功能未知，但是可能影响数据的实时性。

## API 列表:

#### 获取职校列表:
方法:post
<http://www.nnzkzs.com/api/services/app/vocationalPublicity/GetPublicity>
#### 获取普高列表:
方法:post
http://www.nnzkzs.com/api/services/app/generalPublicity/GetPublicity
#### 获取普高的报名信息:
http://www.nnzkzs.com/api/services/app/publicityDetail/GetGeneralDetail?schoolCode={1}&type={2}status={3}
需要同时post header: 
explain:
1. {1}: **school code** - 可以在SchoolCode.xlsx找到，一个代码对应一个学校
2. {2}: **enroling method** - instruction,directional,guide 指导，定向，指导
3. {3}: **status** - 一般在报名时用2，在结束后用4.
#### 获取职高的报名信息:
http://www.nnzkzs.com/api/services/app/publicityDetail/GetVocationalDetail?schoolCode={1}
{1} 与普高相同


## 默认命名方式
(时间戳).json
加载一个数据系列，用文件名作时间顺序。

## 文件介绍
- GetInformationandPrint.py : 在线获取信息并且打印，在四月和五月不可用。
- AnalisisData.py
    1. 包括了2个类，分别用作单独的数据和数据序列。
    2. 类SingleData的方法如下:
        - init_gradeOrder(gradeOrder) : 初始化等级顺序。
        - init_match() 初始化学校代码和学校名字的配对，需要自己调用。
        - getBySchoolCode(schoolCode,IFMERGE = False) 根据学校代码返回数据。参数IFMERGE决定了是否混合同等级的学生。
        - returnAbove(schoolCode,grade) 返回高于或等于已知等级的学生数量
        - countGradeBySchoolCode(schoolCode,ifsum = False) 返回一个字典，键为给学校代码的学校的学生的等级，值为其数量。
        - estimate(schoolCode,if_index_score=True) 综合评价一个学校的学生来源。
    3. 类SequenceData的方法如下 (你需要把这个脚本和所有数据放在一起):
        - getAboveBySchoolCode(self,schoolCode,grade,gradeOrder) 返回一个按时间顺序排列的列表，包括数据中给定学校和给定等级以上的人数。
        - getScoreBySchoolCode(self,schoolCode) #返回按时间顺序排列的评估分数。
- AnalysisVocationalData.py : 几乎与AnalysisData.py相同.
- example.py : 一个使用函数的例子.
- GetInformation.py : 在nnzkzs.com获取信息，并且保存到一个.json文件，用时间戳命名。
- GetInformationLoop.py : 这个脚本类似GetInformation.py， 但是它将循环至特定的时间戳
- GetVocationalInformation.py : 与GetInformation.py相似，但是它用于职高。

