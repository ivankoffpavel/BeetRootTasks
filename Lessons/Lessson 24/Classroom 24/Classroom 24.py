# Remove spaces in a String with Recursion
def removespace(str):
    if len(str) == 0 :
        return ""
    if str[0] == " ":
        return removespace(str[1:])
    else :
        return  str[0] +removespace(str[1:])


print(removespace('Hi mom I love you'))