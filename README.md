# 功能说明
- 应用名称：sluds(用户认证系统)
- 模型说明：
    - 用户注册：根据用户提交的注册信息到相应的表中查看是否重复，如果没有重复，则先向User_LocalAuth或User_OpenAuth表中插入相应的记录，而后再向Users表中插入相应的记录。
    - 用户登录：
    - 用户信息查询

# 运行方法
- 测试环境
- 生产环境

# TodoList
- 用户相关数据需要加载到redis中
- 请求方式修改为GET方式（接口文档、程序）

# CommandList
- 升级数据库：python manage.py db upgrade
- 生产包文件：pip freeze >requirements.txt
- 按照包文件：pip install -r requirements.txt
-----
- 进入命令行：python manage.py shell
- 创建项目：django-admin startproject mysite
- 创建应用：python manage.py startapp polls
- 生成数据迁移文件：python manage.py makemigrations polls
- 查看模型SQL：python manage.py sqlmigrate polls 0001
- 检查数据库和模型SQL一致性：python manage.py check
- 将改变更新到数据库：python manage.py migrate

---
- 运行开发环境：python manage.py runserver [0.0.0.0:8080]

# 测试命令
- curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book"""}" http://localhost:5000/todo/api/v1.0/tasks

# 管理账号
admin/dwl1234567890