from app import app,db,lm
from app import models
from flask import render_template,flash,redirect,session,url_for,request,g,send_from_directory
from flask_login import login_user,logout_user,current_user,login_required 
# import机制：可以采用app.xxx，也可以使用.xxx，app在此处为一个包
from app.forms import LoginForm,JumpNotice
from app.registe import RegisteForm
from .forget import ForgetForm
from .models import User
from .attach import AttachForm
from .edit import EditForm
from .manage_notices import Add_Notices_Form,Edit_Notices_Form,Jump_Notices_Form,Button_Add,Button_Edit,Button_Delete
from PIL import Image
import os.path
from datetime import datetime
from time import strftime
from config import LIST_NUM_PER_PAGE
import urllib3

dir_path = os.path.join(app.root_path,'uploads')

#index网页访问入口
@app.route('/index')
@login_required
def index():
    user = g.user
    notice_count = models.Notices.query.count()
    notice = dict()
    for i in range(5):
        notice[i+1] = models.Notices.query.all()[notice_count-i-1]
     
    return render_template('index.html',user=user,notice1=notice[1],notice2=notice[2],notice3=notice[3],notice4=notice[4],notice5=notice[5])
    print(notice)

#登录网页访问入口
@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        input_user = form.username.data.lower()
        user = User.query.filter_by(username=input_user).first()
        if user == None:
            msg ="The user is not registed!"
            return render_template('login.html',title='UserName Error',form=form,msg_username=msg)
        else:
            password_in_db = user.password
            if password_in_db == form.password.data:
                login_user(user)
                return redirect('/index')
            msg ="The password is not right!"
            return render_template("login.html",title='Password Error',form=form,msg_password=msg)

    return render_template('login.html',title='Login',form=form)

#用户注册网页访问入口
@app.route('/registe',methods=['GET','POST'])
@app.route('/registe.html',methods=['GET','POST'])
def registe():
    form = RegisteForm()
    if form.validate_on_submit():
        newuser = models.User(username=form.username.data.lower(),
                              password=form.password.data,
                              workid=form.workid.data,
                              email=form.email.data.lower(),
                              phone=form.phone.data,
                              section=form.section.data,
                              gender=form.gender.data,
                              user_img=form.user_image.data,
                              old_password=form.password.data,
                              old_email=form.email.data.lower(),
                              old_phone=form.phone.data,
                              old_section=form.section.data,
                              old_user_img=form.user_image.data)
        db.session.add(newuser)
        db.session.commit()
        return redirect('/login')
    return render_template('registe.html',title='Registe',form=form)

#账号密码找回网页访问入口
@app.route('/forget',methods=['GET','POST'])
@app.route('/forget.html',methods=['GET','POST'])
def forget():
    form = ForgetForm()
    if form.validate_on_submit():
        input_username = form.username.data.lower()
        username = User.query.filter_by(username=input_username).first()

        input_workid = form.workid.data
        workid = User.query.filter_by(workid=input_workid).first()

        input_email = form.email.data.lower()
        email = User.query.filter_by(email=input_email).first()

        input_password = form.password.data
        
        if username == None:
            return render_template('forget.html',title='Username Wrong',form=form,error_msg='The username is not exist!')
        elif workid == None:
            return render_template('forget.html',title='WorkID Wrong',form=form,error_msg='The workid is wrong!')
        elif email == None:
            return render_template('forget.html',title='Eamil Wrong',form=form,error_msg='The email is wrong!')
        else:
            username.password = input_password
            db.session.commit()
            return redirect('/login')
    return render_template('forget.html',title='Forget',form=form)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
@login_required
def logout():
    #print(g.user)
    logout_username = g.user.username
    #print(logout_user)
    logout_user()
    return render_template('logout.html',title='Logout',username=logout_username)

#用户信息网页访问入口
@app.route('/user_info/<username>')
@login_required
def user_info(username):
    user = g.user
    return render_template('user_info.html',title='User Info',user=user)

#上传网页访问入口
@app.route('/upload',methods=['GET','POST'])
def upload():
    form = AttachForm()
    if form.validate_on_submit():
        filename = form.attach.data.filename
        form.attach.data.save('app/uploads/' + filename)
        return 'Upload Successfully!'
    return render_template('upload.html',title='Upload',form=form)

#文件上传网页访问入口
@app.route('/app/uploads/<filename>')
@app.route('/user_info/app/uploads/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory(dir_path,filename)

#用户信息编辑网页访问入口
@app.route('/edit/<username>',methods=['GET','POST'])
@login_required
def edit(username):
    username = g.user.username
    form = EditForm()
    olddata_dict = {
              'password':g.user.password,
              'email':g.user.email,
              'phone':g.user.phone,
              'section':g.user.section.upper(),
              'user_img':g.user.user_img
              }
    user = models.User.query.filter_by(username=username).first()
    if form.validate_on_submit():        
        user.password = form.password.data
        user.email = form.email.data
        user.phone = form.phone.data
        user.section = form.section.data.lower()
        user.user_img = form.user_img.data
        db.session.commit()
        logout_user()
        return redirect(url_for("login"))  
    return render_template('edit.html',title='Edit',form=form,username=username,olddata=olddata_dict)

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html')

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html')

#Manage网页访问入口
@app.route('/manage/<int:page_index>',methods=['GET','POST'])
@login_required
def manage_news(page_index):
    form_add = Add_Notices_Form()
    form_edit = Edit_Notices_Form()
    form_jump = Jump_Notices_Form()
    button_add = Button_Add()
    button_edit = Button_Edit()
    button_delete = Button_Delete()
    display = ["none","none"]
    checked_data = []
    notices_list = models.Notices.query.paginate(page_index,LIST_NUM_PER_PAGE,False)
    notices_list_num = models.Notices.query.count()
    notices_current_num = len(notices_list.items)
    #print(notices_current_num)
    oldlist=[]

    #判断当前数据库里面notices的数量，和最大显示数做比较，并根据结果进行显示
    if notices_list_num < 10:
        for i in range(0,notices_list_num):
            checked_data.append("")
        checked_data = checked_data[::-1]
    else:
        for i in range(0,LIST_NUM_PER_PAGE):
            checked_data.append("")
        checked_data = checked_data[::-1]

    if form_jump.validate_on_submit():
        print(form_jump.jump_num.data)
        return redirect("/manage/"+str(form_jump.jump_num.data))

    if form_add.validate_on_submit():
        dt = datetime.now()
        current_time = dt.strftime('%Y-%m-%d %H:%M:%S')
        print(current_time)
        print("检测到提交了")
        new_notice = models.Notices(
                                   title=form_add.title.data,
                                   author=form_add.author.data,
                                   content=form_add.content_add.data,
                                   species=form_add.species.data
                                   )
        new_notice.create_date = current_time
        db.session.add(new_notice)
        db.session.commit()

        if notices_current_num == LIST_NUM_PER_PAGE:
            return redirect("/manage/"+str(page_index+1))
        return redirect("/manage/"+str(page_index))
                     
    if notices_list.has_next:
        notices_num=[]
        for i in range(LIST_NUM_PER_PAGE*(page_index-1),LIST_NUM_PER_PAGE*(page_index)):
            notices_num.append(i)
        notices_num = notices_num[::-1]
        return render_template("manage.html",notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form1=form_jump,form2=form_add,form3=form_edit,form4=button_add,form5=button_edit,form6=button_delete,display=display,checked_data=checked_data,oldlist=oldlist)
        #return render_template("manage.html",notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form1=form_jump,form2=form_add,form3=form_edit,form4=button_add,form5=button_edit,form6=button_delete,display=display)

    elif notices_list.has_prev:
        notices_count = models.Notices.query.count()
        notices_count_current = notices_count-(page_index-1)*LIST_NUM_PER_PAGE
        notices_num=[]
        for i in range(LIST_NUM_PER_PAGE*(page_index-1),LIST_NUM_PER_PAGE*(page_index-1)+notices_count_current):
            notices_num.append(i)
        notices_num = notices_num[::-1]
        print(notices_num)
        return render_template("manage.html",notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form1=form_jump,form2=form_add,form3=form_edit,form4=button_add,form5=button_edit,form6=button_delete,display=display,checked_data=checked_data,oldlist=oldlist)
        #return render_template("manage.html",notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form1=form_jump,form2=form_add,form3=form_edit,form4=button_add,form5=button_edit,form6=button_delete,display=display)


    return render_template('manage.html',notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form1=form_jump,form2=form_add,form3=form_edit,form4=button_add,form5=button_edit,form6=button_delete,display=display,checked_data=checked_data,oldlist=oldlist) 
    #return render_template("manage.html",notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form1=form_jump,form2=form_add,form3=form_edit,form4=button_add,form5=button_edit,form6=button_delete,display=display)

#单个通知列表网页访问入口        
@app.route('/notices/<id>')
@login_required
def get_notices(id):
    notice = models.Notices.query.get(id)
    return render_template('notice.html',notice=notice)

#通知列表网页访问入口
@app.route('/notices_list/<int:page_index>',methods=['GET','POST'])
@login_required
def get_notices_list_index(page_index = 1):
    form = JumpNotice()
    notices_list = models.Notices.query.paginate(page_index,LIST_NUM_PER_PAGE,False)
    
    for i in (notices_list.items):
        print(i.id)

    if form.validate_on_submit():
        #print("Submit OK")
        return redirect("/notices_list/"+str(form.page_num.data))
    elif notices_list.has_next:
        notices_num=[]
        for i in range(LIST_NUM_PER_PAGE*(page_index-1),LIST_NUM_PER_PAGE*(page_index)):
            notices_num.append(i)
        notices_num = notices_num[::-1]
        return render_template("notices_list.html",notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form=form)
    else:
        notices_count = models.Notices.query.count()
        notices_count_current = notices_count-(page_index-1)*LIST_NUM_PER_PAGE
        notices_num=[]
        for i in range(LIST_NUM_PER_PAGE*(page_index-1),LIST_NUM_PER_PAGE*(page_index-1)+notices_count_current):
            notices_num.append(i)
        notices_num = notices_num[::-1]
        #print(notices_num)
        return render_template("notices_list.html",notices_num=notices_num,notices_list=notices_list,page_index=page_index,page_full_num=LIST_NUM_PER_PAGE,form=form) 

#通知删除网页访问入口
@app.route('/delete_notices/<number_list>')
@login_required
def delete_notices(number_list):
    #print(number_list[0:2])
    length = len(number_list)
    #print(length)
    list_delete = []
    list_douhao_num = []

    #获取number_list里面逗号所在index
    for i in range(length):
        if number_list[i] == ",":
            list_douhao_num.append(i)
    
    #如果没有逗号，就是参数只有一个数字，直接转给删除列表list_delete
    if len(list_douhao_num) == 0:
        list_delete.append(int(number_list))
    #只有1个逗号的情况
    elif len(list_douhao_num) == 1:
        list_delete.append(int(number_list[:list_douhao_num[0]]))
        list_delete.append(int(number_list[list_douhao_num[0]+1:]))
    else:
        for j in range(len(list_douhao_num)):
            if j == 0:
                list_delete.append(int(number_list[:list_douhao_num[j]]))
            elif j == len(list_douhao_num)-1:
                list_delete.append(int(number_list[list_douhao_num[j]+1:]))
            else:
                list_delete.append(int(number_list[list_douhao_num[j-1]+1:list_douhao_num[j]]))
                list_delete.append(int(number_list[list_douhao_num[j]+1:list_douhao_num[j+1]]))

    print(list_delete)

    notices_list = models.Notices.query.all()
    notices_list_num = []
    for every in notices_list:
        notices_list_num.append(every.id) 
 
    for each in list_delete:
        temp_delete = models.Notices.query.filter_by(id=notices_list_num[each-1]).first()
        db.session.delete(temp_delete)
        db.session.commit()
    return redirect('/manage/1')

#通知编辑网页访问入口
@app.route('/edit_notice/<int:page_num>:<int:notice_num>:<int:checkbox_num>',methods=['GET','POST'])
@login_required
def edit_notice(page_num,notice_num,checkbox_num):

    form_add = Add_Notices_Form()
    form_edit = Edit_Notices_Form()
    form_jump = Jump_Notices_Form()
    button_add = Button_Add()
    button_edit = Button_Edit()
    button_delete = Button_Delete()
    display = ["none","block"]

    notices_count = models.Notices.query.count()
    notices_list = models.Notices.query.all()
    notice_edit = notices_list[notice_num-1]
    notices_list_current_page = models.Notices.query.paginate(page_num,LIST_NUM_PER_PAGE,False)

    notices_list_page_total = notices_count//LIST_NUM_PER_PAGE
    notices_num=[]

    if page_num <= notices_list_page_total:
        for i in range((page_num-1)*LIST_NUM_PER_PAGE,page_num*LIST_NUM_PER_PAGE):
            notices_num.append(i)
        notices_num = notices_num[::-1]
    else:
        for i in range((page_num-1)*LIST_NUM_PER_PAGE,notices_count):
            notices_num.append(i)
        notices_num = notices_num[::-1]

    print(notices_num)
    checked_data=[]
    for each in notices_num:
        checked_data.append("")
    checked_data[len(notices_num)-checkbox_num]="checked"
    checked_data=checked_data[::-1]   
    print(checked_data)

    oldlist = {
               "title_edit":notice_edit.title,
               "content_edit":notice_edit.content,
               "species_edit":notice_edit.species 
               }
    if form_edit.validate_on_submit():
        notice_update = models.Notices.query.get(notice_num)
        #print(notice_update.title)
        notice_update.title = form_edit.title_edit.data
        notice_update.content = form_edit.content_edit.data
        notice_update.species = form_edit.species_edit.data
        print(form_edit.title_edit.data)
        print(form_edit.content_edit.data)
        print(form_edit.species_edit.data)
        db.session.commit()
        return redirect("/manage/1")

    return render_template("manage.html",notices_num=notices_num,notices_list=notices_list_current_page,page_index=page_num,page_full_num=LIST_NUM_PER_PAGE,form1=form_jump,form2=form_add,form3=form_edit,form4=button_add,form5=button_edit,form6=button_delete,display=display,checked_data=checked_data,oldlist=oldlist)    


