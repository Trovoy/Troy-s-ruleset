import requests

rawRejectnonip = requests.get("https://ruleset.skk.moe/List/non_ip/reject.conf").text
rawRejectip = requests.get("https://ruleset.skk.moe/List/ip/reject.conf").text

result = rawRejectnonip.split("\n") + rawRejectip.split("\n")

with open("./Reject.conf", "w") as f:
    f.write("\n".join(result))
