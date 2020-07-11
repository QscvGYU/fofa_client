# encoding = 'utf-8'
import base64
import json
import requests
import urllib.parse as urlparse

class FofaClient(object):
    def __init__(self):
        self.config_path = "/fofa"
        self.base_url = "https://fofa.so"
        self.search_api_url = "/api/v1/search/all"
        self.login_api_url = "/api/v1/info/my"
        self.api_key = ""
        self.email = ""
        self.init_config()
        self.headers = {}
        self.timeout = 60
        self.api_key = "api_key"
        self.email = "email"
        self.session = requests.Session()


    def __http_get(self, url, param):
        param = urlparse.urlencode(param)
        url = f"{url}?{param}"
        try:
            resp =  self.session.get(url, headers=self.headers,timeout=self.timeout)
            if  "errmsg" in resp.text:
                raise FofaClientError(error_msg= f"get_error: {resp.text}")
        except Exception as e:
            raise FofaClientError(error_msg=str(e))
        return resp.text

    def get_data(self,query_str,page=1,fields=""):
        res = self.get_json_data(query_str,page,fields)
        return json.loads(res)

    def get_json_data(self, query_str: str, page=1, fields=""):
        api_full_url = "%s%s" % (self.base_url, self.search_api_url)
        param = {"qbase64": base64.urlsafe_b64encode(query_str.encode('utf-8')), "email": self.email, "key": self.api_key, "page": page,
                 "fields": fields}
        res = self.__http_get(api_full_url, param)
        return res


    def get_user_info(self):
        api_full_url = f"{self.base_url}{self.login_api_url}"
        param = {"email": self.email, "key": self.api_key}
        res = self.__http_get(api_full_url, param)
        return json.loads(res)



class FofaClientError(Exception):

    def __init__(self, error_msg: str) -> object:
        self.msg = error_msg

    def __str__(self):
        return(f"fofa_client_error: {self.msg}")
