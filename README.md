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
- 统一的异常处理
- api权限
- 统一的参数校验
- 缓存如何可以做的更简单统一
- 认证
- 统一的查询过滤
- 代码分层

# CommandList
## conda常用命令
- conda list 查看安装了哪些包
- conda list -n env_name
- conda search numpy
- conda update numpy
- conda remove numpy
- conda env list 或 conda info -e 查看当前存在哪些虚拟环境
- conda update conda 检查更新当前conda
- conda create -n your_env_name python=X.X（2.7、3.6等）
- 切换环境
    Linux:  source activate your_env_name(虚拟环境名称)
    Windows: activate your_env_name(虚拟环境名称)
- 退出环境 deactivate env_name
- conda install -n your_env_name [package]即可安装package到your_env_name中
- 关闭虚拟环境(即从当前环境退出返回使用PATH环境中的默认python版本)。
   linux: source deactivate
   Windows: deactivate
- 删除虚拟环境 conda remove -n your_env_name(虚拟环境名称) --all， 即可删除。
- 删除环境中的某个包 conda remove --name $your_env_name  $package_name 即可。
-----
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
- 调试模式: --noreload --traceback

---
- 安装pymysql: conda install pymysql
- 并在mysite/__init__.py中进行初始化:

`
import pymysql
pymysql.install_as_MySQLdb()
`

# 测试命令
- curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book"""}" http://localhost:5000/todo/api/v1.0/tasks

# 管理账号
admin/dwl1234567890
