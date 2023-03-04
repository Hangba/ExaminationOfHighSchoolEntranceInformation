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
- AnalysisVocationalData.py : Almost identical with AnalisisData.py.
- example.py : An example to use the functions.
- GetInformation.py : Get information online and save as a file using time stamp as its name.
- GetInformationLoop.py : The function is like GetInformation.py but it keeps cycling until the time stamp you set in the file.
- GetVocationalInformation.py : Similar to GetInformation.py, but it is for vacational schools.
