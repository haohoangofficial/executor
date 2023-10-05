import requests
from bs4 import BeautifulSoup as bs
from executor.utils.option import random_user_agents
def get(url, params=None, **kwargs):
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS='ALL:@SECLEVEL=1'  # Fix [SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:997)
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)  # Disable SSL error warning
    
    default_headers = {
        'User-Agent': random_user_agents()
    }
    
    if 'headers' not in kwargs:
        headers = default_headers
    else:
        for key, value in headers.items():
            default_headers[key] = value
        headers = default_headers
    
    kwargs.setdefault("headers", headers)

    if 'timeout' not in kwargs:
        kwargs.setdefault("timeout", 10)
    
    if 'allow_redirects' not in kwargs :
        kwargs.setdefault("allow_redirects", False)
    
    if 'verify' not in kwargs:
        kwargs.setdefault("verify", False)
        
    return requests.request('get', url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):
    return requests.request("post", url, data=data, json=json, **kwargs)

def put(url, data=None, **kwargs):
    return requests.request("put", url, data=data, **kwargs)

def patch(url, data=None, **kwargs):
    return requests.request("patch", url, data=data, **kwargs)

def delete(url, **kwargs):
    return requests.request("delete", url, **kwargs)

def head(url, **kwargs):
    kwargs.setdefault("allow_redirects", False)
    return requests.request("head", url, **kwargs)

def options(url, **kwargs):
    return requests.request("options", url, **kwargs)