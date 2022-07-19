# ExaminationOfHighSchoolEntranceInformation
 Use API provided by Education Administration to log current enroling data

## API list:

#### Get list of vocational schools:
method:post
http://www.nnzkzs.com/api/services/app/vocationalPublicity/GetPublicity
#### Get list of general schools:
method:post
http://www.nnzkzs.com/api/services/app/generalPublicity/GetPublicity
#### Get enroling information of general schools:
http://www.nnzkzs.com/api/services/app/publicityDetail/GetGeneralDetail?schoolCode={1}&type={2}status={3}
need post header: 
explain:
{1}: school code -  can find in SchoolCode.xlsx. A code corresponds to a school.
{2}: enroling method - instruction,directional,guide.
{3}: status - unknown but is 2 while enroling and is four after ending.
#### Get enroling information of vocational schools:
http://www.nnzkzs.com/api/services/app/publicityDetail/GetVocationalDetail?schoolCode={1}
{1} identical as above


## default naming method
(time stamp).json
loading a sequence of data, use file name as time order.

