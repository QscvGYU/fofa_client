# coding = 'utf-8'
from fofa_client import FofaClient

if __name__ =="__main__":
    fofa_client = FofaClient()
    """【可选参数】字段列表，默认为host，用逗号分隔多个参数，如(fields=ip,title)，
    可选的列表有：
    host title ip domain port country province city country_name header server protocol
     banner cert isp as_number as_organization latitude longitude lastupdatetime
    """
    query_str = f'ip="xxx.xxx.xxx.xx"'
    for page in range(1, 51):
        user_info = fofa_client.get_user_info()
        print(f"fcoin : {user_info['fcoin']}", end="")
        data = fofa_client.get_data(query_str, page=page,
                                         fields="host,title,domain,ip,country,province,city,country_name,header,server,protocol,banner,cert,isp")
        print(data)