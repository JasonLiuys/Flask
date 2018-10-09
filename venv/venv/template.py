from flask import Flask, render_template #导入jinja2拓展

app = Flask(__name__)  #创建Flask实例

@app.route('/', methods=['GET', 'POST']) #定义路由及视图函数
def index():

    #比如需要传入网址

    url_str = 'www.baidu.com'

    my_list = [1,3,5,7,9]

    my_dict = {
        'name' : 'jason',
        'url' : 'www.baidu.com'
    }
    #通常，模板中变量名和数据中的变量名保持一致
    return render_template('index.html', url_str=url_str, my_list = my_list, my_dict = my_dict)


#启动程序
if __name__ == '__main__':
    #执行了app.run.就会将Flask程序运行在一个简易的服务器
    app.run()
