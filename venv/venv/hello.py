from flask import Flask #导入Flask拓展

app = Flask(__name__)  #创建Flask实例
#需要传入__name__,作用是为了确定资源所在的路径

#Flask中定义路由是通过装饰器实现的
#路由默认只支持GET，如果需要增加，需要自行指定
@app.route('/', methods=['GET', 'POST']) #定义路由及视图函数
def index():
    return 'hello flask'

#使用同一个视图函数，来显示不同用户的订单信息
#<>定义路由参数，<>内需要起个名字
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    #需要在视图函数括号内填入参数名，后面的代码才能使用

    #有时需要对路由做访问优化，订单ID应该是int类型
    return 'order_id %s' % order_id

#启动程序
if __name__ == '__main__':
    #执行了app.run.就会将Flask程序运行在一个简易的服务器
    app.run()

