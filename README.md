Prior to get output data using input text , I have tested by code using dataset websiteData.txt. We read websiteData.txt as a test file as:
with open('input.txt') as f:
    lines = f.readlines()
   
and we get output as
{
    "Jobs@linkedin.com": {
        "occurance": 1,
        "EmailType": "Non-Human"
    },
    "gregor@mxanalytics.com": {
        "occurance": 1,
        "EmailType": "Non-Human"
    },
    "susan.daniels@moo.com": {
        "occurance": 1,
        "EmailType": "Human"
    },
    "hr@vancuemonics.com": {
        "occurance": 1,
        "EmailType": "Non-Human"
    },
    "syneca.gregory@gmail.com": {
        "occurance": 1,
        "EmailType": "Human"
    },
    "REALTORS\u00ae;realtors@bbn.com": {
        "occurance": 1,
        "EmailType": "Non-Human"
    },
    "info@content.linkedin.com": {
        "occurance": 1,
        "EmailType": "Non-Human"
    }
}.
After this we can read given input data and can get the output which is saved in result.json file.
