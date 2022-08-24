import requests

rawRejectDomain = requests.get("https://ruleset.skk.moe/List/domainset/reject.conf").text

result = rawRejectDomain.split("\n")

with open("./RejectDomain.conf", "w") as f:
    f.write("\n".join(result))
   
