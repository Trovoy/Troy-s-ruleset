import requests

rawApple = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Apple/Apple.list").text

result = rawApple.split("\n")

with open("./Apple.conf", "w") as f:
    f.write("\n".join(result))
