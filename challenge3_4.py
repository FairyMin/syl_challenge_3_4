# -*- coding:utf-8 -*-

import re 
from datetime import datetime

#使用正则表达式解析日志文件，返回数据列表

def open_parser(filename):
    with open(filename) as logfile:
        #使用正则表达式解析日志文件
        pattern =(r''
                r'(\d+.\d+.\d+.\d+.)\s-\s-\s' #IP地址

                r'\[(.+)\]\s'  #时间

                r'"GET\s(.+)\s\w+/.+"\s'   #请求路径

                r'(\d+)\s'     #状态码

                r'(\d+)\s'     #请求头

                r'"(.+)"'      #客户端信息

                )
        parsers = re.findall(pattern,logfile.read())

    return parsers

def main():
    #使用正则表达式解析日志文件
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    '''
    1.解析文件就是分离不同类型数据(IP，时间，状态码等)

    2.从解析后的文件中统计挑战所需要的信息
    '''
    #ip_dict 包含的信息是2017年1月11日期间访问此时最多的IP以及对应的访问次数
    #格式{'IP':'times'}
    ip_dict = {}
    
    #url_dict包含的信息是 GET请求状态为404最多的URL 请求地址以及请求次数
    #格式 {"IP":"times"}
    url_dict = {}
    
    #集合存储ip信息
    ip_set = set()
    url_set = set()

    total_ipdict = {}
    total_urldict = {}

    for info in logs:
        ip_set.add(info[0])
        url_set.add(info[2])

    #创建字典将数据存入内存
    for i in ip_set:
        total_ipdict.setdefault(i,{})
        total_ipdict[i]['times'] = 0
    #    
    for ui in url_set:
        total_urldict.setdefault(ui,{})
        total_urldict[ui]['404'] = 0
        
    #计算访问次数最多的ip 以及 访问状态为404次数最多的ip  以及相应的访问次数
    cons = {
            "Jan":"1",
            "Feb":"2",
            "Mar":"3",
            "Apr":"4",
            "May":"5",
            "Jun":"6",
            "Jul":"7",
            "Aug":"8",
            "Sep":"9",
            "Oct":"10",
            "Nov":"11",
            "Dec":"12"
            }
    for j in logs:
        #获得时间time1 day/mon/year:hour:min:sec

        ti = j[1].split('+',1)
        tif = ti[0]
        for mon in cons.keys():
            if mon in tif:
                time0 = tif.replace(mon,cons[mon])
                time1 = datetime.strptime(time0.strip(),"%d/%m/%Y:%H:%M:%S")

        if time1.year == 2017 and time1.month == 1 and time1.day == 11:
            total_ipdict[j[0]]['times'] += 1
        
        if j[3] == '404':
            total_urldict[j[2]]['404'] += 1

    m_key = ""
    m_value = 0

    key_nf = ""
    value_nf = 0

    for k,v in total_ipdict.items():
        if v['times'] > m_value:
            m_key = k
            m_value = v['times']

    for uk,uv in total_urldict.items():
        if uv['404'] > value_nf:
            value_nf = uv['404']
            key_nf = uk

    ip_dict[m_key] = m_value

    url_dict[key_nf] = value_nf

    return ip_dict,url_dict

if __name__ == "__main__":
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)
