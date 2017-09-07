# 接口测试
## (13)用户信息查询接口
- [GET](http://127.0.0.1:8080/sluds/user/?version=1.0&action=get_user_info&UserID=1)
- [POST](http://127.0.0.1:8080/sluds/user/get_user_info.luds/)

`
{
    "version": "1.0",
    "action": "get_user_info",
    "params":{
        "UserID": 1
    }
}`

## (14)用户基本信息更新接口
[POST](http://127.0.0.1:8080/sluds/user/update_user_info.luds/)

`{
	"version": "1.0",
	"action": "update_user_info",
	"params": {
		"UserID": 1,
		"NickName": "肉大3爷",
		"SelfIntroduction": "总理",
		"Gender": 1,
		"LocationProvince": "浙江",
		"LocationCity": "杭州"
	}
}`

## (20)邮箱注册接口
[POST](http://127.0.0.1:8080/sluds/user/localregist_user_email.luds/)

`{
    "version" : "1.0",
    "action" : "localregist_user_email",
    "params" :{
        "UserName" : "dang_wenyun@163.com",
        "Password" : "123456"
    }
}`

## (21)邮箱注册验证接口
[POST](http://127.0.0.1:8080/sluds/user/checkin_email.luds/)

`{
    "version" : "1.0",
    "action" : "checkin_email",
    "params" :{
        "UserName" : "dangwenyun@163.com",
        "Password" : "123456",
        "authcode" : "9584"
    }
}`