import requests
import json
class api:
    def __init__(self):
        self.url = 'http://192.168.100.30:5000/v3/auth/tokens'  # url访问api地址
        body = {
            "auth": { # 认证信息
                "identity": { # 认证参数
                    "methods": ["password"], # 认证方法
                    "password": {
                        "user": {
                            "domain": {"name": "demo"},
                            "name": "admin",
                            "password": "0"
                        }
                    }
                },
                "scope": { # Token的使用范围
                    "project": {
                        "domain": {"name": "demo"}, # scope设置为domain，该Token适用于全局级服务，如果是project，适用>于项目级服务
                        "name": "admin"
                    }
                }
            }
        }  # 字典，信息
        headers = {
            "Content-Type": "application/json" # 消息体的类型（格式）
        }  # json读取格式
        token = requests.post(url=self.url, data=json.dumps(body), headers=headers)  # post请求，token身份认证
        print(token.headers['X-Subject-Token']) # 获取令牌
        print(token.json()) # 以json文件显示信息

if __name__ == "__main__":  # 运行
    ch = api()
