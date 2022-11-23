import redis
import random
from common.settings import RedisConfigure1

"""
爬虫 基础信息配置 因为爬虫是多种多样的，这个针对不同的爬虫 构建不同的类  和相关性信息进行配置 

自由的控制信息的变化和封装特定小工具等 

"""

redis_client = redis.Redis(host=RedisConfigure1.HOST, port=RedisConfigure1.PORT, password=RedisConfigure1.PASSWORD)


class Example(object):
    # 请求URL
    url = "https://www.baidu.com/sugrec?prod=pc_his&from=pc_web&json=1&sid=36547_37772_37628_34813_37777_37728_37715_37741_26350_37790&hisdata=%5B%7B%22time%22%3A1668823628%2C%22kw%22%3A%22jadx%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1668823668%2C%22kw%22%3A%22jadx%E5%AE%98%E7%BD%91%22%7D%2C%7B%22time%22%3A1668823679%2C%22kw%22%3A%22google%22%2C%22fq%22%3A6%7D%2C%7B%22time%22%3A1668824880%2C%22kw%22%3A%22aundroid%20studio%E7%9F%A5%E8%AF%86%E6%98%9F%E7%90%83%22%7D%2C%7B%22time%22%3A1668824904%2C%22kw%22%3A%22%E7%9F%A5%E8%AF%86%E6%98%9F%E7%90%83%22%7D%2C%7B%22time%22%3A1668825243%2C%22kw%22%3A%22charles%22%7D%2C%7B%22time%22%3A1668825285%2C%22kw%22%3A%22charles%E5%AE%98%E7%BD%91%22%7D%2C%7B%22time%22%3A1668825340%2C%22kw%22%3A%22charles%20%E6%94%AF%E6%8C%81win%E5%90%97%22%7D%2C%7B%22time%22%3A1668825446%2C%22kw%22%3A%22charles%E4%B8%AD%E6%96%87%E7%A0%B4%E8%A7%A3%E5%85%8D%E8%B4%B9%E7%89%88%22%7D%2C%7B%22time%22%3A1668832779%2C%22kw%22%3A%22java%20%E8%BF%90%E8%A1%8C%20jar%22%7D%5D&_t=1669180769411&req=2&csor=0"
    # 请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'PSTM=1668524297; BD_UPN=12314753; BIDUPSID=19DB0909B768E51AA5D03D3CAF1C964F; newlogin=1; BDUSS=t3Q21kU0pZdzluTG9ZSTNUdTF4c016SFFUODM4fmt3MHl3a2FzVHhaYkhGS0JqSVFBQUFBJCQAAAAAAAAAAAEAAAC89L06xL7X08uuyunAvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeHeGPHh3hjNm; BDUSS_BFESS=t3Q21kU0pZdzluTG9ZSTNUdTF4c016SFFUODM4fmt3MHl3a2FzVHhaYkhGS0JqSVFBQUFBJCQAAAAAAAAAAAEAAAC89L06xL7X08uuyunAvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeHeGPHh3hjNm; BAIDUID=DCFD3CF39349E89EA549D03CB61F2D2F:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=0ha48g2l8k8l002g202k86db1hnr23m1e; delPer=0; BD_CK_SAM=1; PSINO=5; ZFY=mACrvP3eMKiTYQQPe15D8MLQhbAjrUGqFzgt9J8RrC4:C; BAIDUID_BFESS=DCFD3CF39349E89EA549D03CB61F2D2F:FG=1; shifen[447440389606_73331]=1669171877; BCLID=11919200105571742900; BCLID_BFESS=11919200105571742900; BDSFRCVID=Go-OJeC626dgn05jq8M6hw9z5urBozQTH6ao6kXes-hD76skSjWREG0Pyf8g0KubM9GjogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=Go-OJeC626dgn05jq8M6hw9z5urBozQTH6ao6kXes-hD76skSjWREG0Pyf8g0KubM9GjogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJPqoK_ytC-3JRcRqROqbbQH-UIs0-4LB2Q-5KL-JJbJDCtGMRLWXjKJ5NrEtRQH0DOEbxbdJJjoMRvybJ-VMM3WjlbWQ-TULeTxoUJX5DnJhhvG-xFBQPIebPRiB-b9QgbA5hQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjDhjjjL3J; H_BDCLCKID_SF_BFESS=tJPqoK_ytC-3JRcRqROqbbQH-UIs0-4LB2Q-5KL-JJbJDCtGMRLWXjKJ5NrEtRQH0DOEbxbdJJjoMRvybJ-VMM3WjlbWQ-TULeTxoUJX5DnJhhvG-xFBQPIebPRiB-b9QgbA5hQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjDhjjjL3J; H_PS_PSSID=36547_37772_37628_34813_37777_37728_37715_37741_26350_37790; H_PS_645EC=4e8b4T61yqSQkwY5Orl%2BFNwwpQRJWdfEVhHipxgNCYokrEjI6DnOJviQDklXob6h%2FLSj; COOKIE_SESSION=5732_1_9_9_5_8_0_0_9_7_1_0_424_0_0_0_1669174679_1669171878_1669180738%7C9%2373041_30_1669171876%7C9; BD_HOME=1; WWW_ST=1669180768762; sugstore=1',
        'Referer': 'https://www.baidu.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # 任务队列
    def get_task(self):
        tasks = [item.decode() for item in redis_client.spop('maijx_select_goods', 1)]
        return tasks

    # 代理设置
    def get_ip_pool(self):
        ip_all = [item.decode() for item in redis_client.smembers('ip_list')]
        return ip_all
