import requests

rawRejectDomain = requests.get("https://ruleset.skk.moe/List/domainset/reject.conf").text

result = list()
for rawresult in [rawRejectDomain]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./RejectDomain.conf", "w") as f:
    f.write("\n".join(result))
   
