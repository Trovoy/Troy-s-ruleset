import requests

rawWeChat = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/WeChat/WeChat.list").text
rawTesla = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Tesla/Tesla.list").text
rawXiaoHongShu = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/XiaoHongShu/XiaoHongShu.list").text
rawApple = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Apple/Apple.list").text
rawXianYu = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/XianYu/XianYu.list").text
rawdirect1 = requests.get("https://raw.githubusercontent.com/dler-io/Rules/main/Surge/Surge%203/Provider/Domestic.list").text
rawdirect2 = requests.get("https://raw.githubusercontent.com/dler-io/Rules/main/Surge/Surge%203/Provider/Domestic%20IPs.list").text
rawdirect3 = requests.get("https://ruleset.isagood.day/direct.conf").text

result = list()
for rawresult in [rawWeChat , rawTesla , rawXiaoHongShu , rawApple ,rawXianYu ,rawdirect1 ,rawdirect2 ,rawdirect3]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Direct.list", "w") as f:
    f.write("\n".join(result))
