import requests
import json


def get_data(province, sub_district):
    url = "https://lbs.amap.com/service/api/restapi?keywords="+province+"&subdistrict="+sub_district+"&extensions=base"
    response_data = requests.post(url, {
        "type": "config/district",
        "version": "v3"
    })
    json2python = json.loads(response_data.text)
    result = get_child([], json2python['districts'][0])
    print(json.dumps(result, ensure_ascii=False))


# 递归赋值
def get_child(result, datas):
    for index in range(len(datas["districts"])):
        data = datas["districts"][index]
        result.append({"value": data["name"]})
        if len(data["districts"]) > 0:
            result[index]["childs"] = []
            get_child(result[index]["childs"], data)
    return result
