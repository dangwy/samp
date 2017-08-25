# 接口测试
## (30)用户信息查询接口
- GET:
    http://127.0.0.1:8080/sluds/user/?version=1.0&action=get_user_info&UserID=1
- POST:
    http://127.0.0.1:8080/sluds/user/get_user_info
    {
        "version": "1.0",
        "action": "get_user_info",
        "params":{
            "UserID": 1
        }
    }
