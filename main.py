# import requests
# import json
# url="https://www.scorebat.com/video-api/v1/"
# r=requests.get(url)
# # print(r)
# # print(r.headers)
# # print(r.text)
# res=json.loads(r.text)
# # res_structured=json.dumps(res, indent=4)
# # print(res_structured)
# # with open("Football.json", 'w') as f:
# #     json.dump(res,f,indent=4)
# print(res[1]['videos'][0]['embed'])
