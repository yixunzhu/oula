前言：
基于python（3.0系列）开发，通过pytest进行脚本的统一管理和调度，并实现了持续集成功能！

1、case_demo
    用例demo
2、tins
    所有非业务底层的封装
    1、common：公共包
    allureHandler：生成allure测试报告的模块
    excel.py:处理配置和excel文件的模块
    helper：所有底层非业务的方法封装
    log.py:处理日志的模块
    requestsHandler.py:处理请求的模块
    sql.py:处理sql的模块
    wechat.py:企业微信机器人发送消息的模块

    2、api
    所有和业务相关的封装
    pub.py：公共业务的封装

    3、config：配置

3、logs：日志包
    追加存放每日产生的日志

4、report：测试报告
    覆盖存放allure的测试报告

5、testcases：测试用例
    存放测试用例

6、pytest.ini：pytest配置文件
    配置pytest执行规则

7、run.py：总运行文件
    根据pytest.ini执行测试用例

8、conftest.py:测试固件
    测试固件集合

9、持续集成使用方法：
    1、打开url地址：
    2、点击构建
    3、填写选项，开始构建

#####################################################################
#### 安装依赖

环境 python3 (>3.6)

pip3 install httprunner

pip3 install "allure-pytest"

安装allure: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

**环境变量:  pip安装的默认命令路径 ~/.local/bin **

#### 执行 SQL 测试并生成报告
make test_all

#### 查看测试报告
allure serve ./reports

#### 清除测试过程中的临时文件
make clean_all

## 添加测试用例
  用例文档格式参考: https://docs.httprunner.org/user/write_testcase 例子为 python 格式, yml 格式是对应的
  参考目前项目里的 yml 文件写就行了

#### 文件命名规范(不以规范命名也行,系统会自动替换,如果出错请检查命名)
  文件命名支持中文,如果遇到 ~!@#$%^&*())-/*?\""''[]{}:; 等特殊字符,请统一替换为下划线 _
  一个接口对应一个文件夹,一个接口有多个测试用例
  同一接口,添加不同用例,请以下划线_命名隔开

  例子:
       数据转储/导出 改为 数据转储_导出
       test-controller 改为 test_controller
       添加用户_必要参数
       添加用户_全部参数

#### 组合接口用例
  组合用例必须是一个完整的流程,将多个用例进行整合

  例子:
       ps：先创建需要测试的权限，比如x表的select权限
       1.enmoadmin登录用例
        enmoadmin创建用户用例
        enmoadmin绑定用户到默认角色用例
        enmoadmin绑定权限与用户到新建角色用例
        退出登录用例
       2.普通用户登录用例
        执行有权限sql用例
        执行无权限sql用例
        退出登录用例
       3.enmoadmin登录用例
        enmoadmin删除角色用例
        enmoadmin删除用户用例
        退出登录用例

#### SQL执行测试集合
  通常一组用例为一个文件夹,用文件夹是为了区分每个人各自的提交,保证提交的文件夹可以单独运行起来,文件夹中包含
    config.sql (库表初始化,可选)
    xxx.yml (测试用例描述文件,必选)
    xxx.csv (测试用例的数据来源,可选)

  例子:
    我需要添加一条 select * from student 语句,作为执行接口的测试用例
    在 SQL执行测试集合/mysql/dml/select/ 文件夹下面创建新的文件夹,名字随意,比如 select_student
    然后在新建的文件夹 select_student 中添加上面的三个文件
    这样可以通过 SQL执行测试集合/mysql/dml/select/select_student 这个路径单独运行测试用例

#### SQL解析测试集合
  存放解析接口的测试用例,目前判断解析出的表名对不对




