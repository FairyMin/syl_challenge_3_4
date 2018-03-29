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
    url_dic = {}
    
    for info in logs:
        print(info[0],info[1])
        break

    return ip_dict,url_dict

if __name__ == "__main__":
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)
