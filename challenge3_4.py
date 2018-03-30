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
    total_ipdict = {}

    for info in logs:

        ip_set.add(info[0])
        
        time_info =  info[1].split("+",1)

        time_info1 = time_info[0].split(":",1)
        
        print(time_info1)

    #创建字典将数据存入内存
    for i in ip_set:
        total_ipdict.setdefault(i,{})
        total_ipdict[i]['times'] = 0
        total_ipdict[i]['404'] = 0
        
    #计算访问次数最多的ip 以及 访问状态为404次数最多的ip  以及相应的访问次数
    for j in logs:
        total_ipdict[j[0]]['times'] += 1
        if j[3] == '404':
            total_ipdict[j[0]]['404'] += 1

    m_key = ""
    m_value = 0

    key_nf = ""
    value_nf = 0

    for k,v in total_ipdict.items():
        if v['times'] > m_value:
            m_key = k
            m_value = v['times']

        if v['404'] > value_nf:
            value_nf = v['404']
            key_nf = k

    ip_dict[m_key] = m_value

    url_dict[key_nf] = value_nf

    return ip_dict,url_dict

if __name__ == "__main__":
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)
