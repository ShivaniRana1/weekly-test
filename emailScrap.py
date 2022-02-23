import json
with open('input.txt') as f:
    lines = f.readlines()
stringList = []
for line in lines:
    strings = line.split()    
    stringList.extend(strings)

emailList = []
for string in stringList:
    result = string.find('.com')
    result2 = string.find('@')
    count = 0
    if result != -1 and result2 != -1:
        #strip
        if string[-1] == '.':
            string = string.strip(".")
        emailList.append(string)
 
Dict = { }
dict_of_counts = {item:emailList.count(item) for item in emailList}
for key in dict_of_counts:
    splitList =  key.split('@')
    if splitList[0].find('.') != -1 and len(splitList[0]) >= 8:
        Dict[key] = {"occurance": dict_of_counts[key], "EmailType":"Human"} 
        
    else:
        Dict[key] = {"occurance": dict_of_counts[key], "EmailType":"Non-Human"}  


with open("result.json", "w") as outfile:
    json.dump(Dict, outfile)

        
    
    