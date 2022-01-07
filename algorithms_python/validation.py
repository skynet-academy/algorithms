import re

def code_user_validation(strParam):
    result = ""
    x = re.compile('[\w]*[^_]$')
    if(len(strParam) >= 4 and len(strParam) <= 25 and strParam[0].isalpha() and x.match(strParam)):
        result = "true"
    else:
        result = "false"

    return result


print(code_user_validation("121415_"))
print(code_user_validation("dsa1415_sadg"))
print(code_user_validation("ss21$@5_234"))
