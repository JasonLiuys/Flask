from flask import Flask, render_template, request, flash #导入Flask拓展
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)  #创建Flask实例
#需要传入__name__,作用是为了确定资源所在的路径

app.secret_key = 'jason'

#Flask中定义路由是通过装饰器实现的
#路由默认只支持GET，如果需要增加，需要自行指定

# 目的：实现一个简单的登陆的逻辑处理
# 1.路由需要判断请求方式（get与post）
# 2.获取请求的参数
# 3.判断参数是否填写 & 密码是否相同
# 4.如果判断没有问题，那么返回一个success

#给模板传消息用flash,模板中需要遍历消息，flash需要对内容加密->设置secret_key

#使用WTF实现表单，自定义表单类

class LoginForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码:', validators=[DataRequired(), EqualTo('password', '密码填入不一致')])
    submit= SubmitField('提交')

@app.route('/form' , methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # 1.判断请求方式
    if request.method == 'POST':

        # 2.获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 3. 验证参数.WTF可以一句话实现所有校验
        if login_form.validate_on_submit():
            print ("success")
            return 'success'

        else:
            flash('参数有误')

    return render_template('WTF.html', form = login_form)

@app.route('/', methods=['GET', 'POST']) #定义路由及视图函数
def index():
    #request : 请求对象 --> 获取请求方式，数据
    # 1.判断请求方式
    if request.method == 'POST':
        # 2.获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print (username)

        # 3.判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            #print ("参数不完整")
            flash(u"参数不完整")

        elif password != password2:
            #print("密码不一致")
            flash(u"密码不一致")

        else:
            return 'success'

    return render_template('WTF.html')


#启动程序
if __name__ == '__main__':
    #执行了app.run.就会将Flask程序运行在一个简易的服务器
    app.run()
