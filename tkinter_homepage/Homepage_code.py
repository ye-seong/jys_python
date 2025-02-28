class Admin:
    admin_pass = '1234'
    admin_value = True
    error_num = 0

class User:
    name = ''
    id = ''
    password = ''

    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

class Post:
    post_writer = ''
    post_title = ''
    post_detail = ''
    post_reply = []

    def __init__(self, writer, title, detail, reply):
        self.post_writer = writer
        self.post_title = title
        self.post_detail = detail
        self.post_reply = reply

class Reply:
    reply_writer = ''
    reply_detail = ''

    def __init__(self, writer, detail):
        self.reply_writer = writer
        self.reply_detail = detail

user_list=[]
post_list=[]
    
def addToUserDB(items: list):
    f = open('user_db.txt', encoding='utf-8', mode='w')
    for item in items:
        f.write(f'{item.name}|')
        f.write(f'{item.id}|')
        f.write(f'{item.password}\n')

    f.close()

def addToPostDB(items: list):
    f = open('opst_db.txt', encoding='utf-8', mode='w')
    for item in items:
        f.write(f'{item.post_writer}|')
        f.write(f'{item.post_title}|')
        f.write(f'{item.post_detail}|')
        f.write(f'{item.post_reply}')

    f.close()

def LoadUserFromDB(items: list):
    f = open('user_db.txt', encoding='utf-8', mode='r')
    while True:
        line = f.readline().replace('\n', '')
        if not line: break
        
        lines = line.split('|')
        name = lines[0]
        id = lines[1]
        password = lines[2]

        user = User(name, id, password)
        user_list.append(user)
    
    f.close()

def LoadPostFromDB(items: list):
    f = open('post_db.txt', encoding='utf-8', mode='r')
    while True:
        line = f.readline().replace('\n', '')
        if not line: break
        
        lines = line.split('|')
        writer = lines[0]
        title = lines[1]
        detail = lines[2]
        reply = lines[3]

        post = Post(writer, title, detail, reply)
        post_list.append(post)
    f.close()
        
def AdminPass(password):
    if password == Admin.admin_pass:
        return True
    else:
        Admin.error_num += 1
        if (Admin.error_num >= 4): Admin.admin_value = False
        return False
    
def UserAccount(name, id, password):
    if name != '' and id != '' and password != '':
        for user in user_list:
            if user.name == name:
                return "name_error"
            elif user.id == id:
                return "id_error"
        info=User(name, id, password)
        user_list.append(info)
        addToUserDB(user_list)
        return "success"
    else:
        return "empty_error"
        
def UserLogin(id, password):
    for user in user_list:
        if user.id == id and user.password == password:
            return user.name
        else:
            return "error"

def GetUserInfo(name):
    for user in user_list:
        if user.name == name:
            return f"이름 : {name}\n아이디 : {user.id}\n비밀번호 : {user.password}"

def GetUserList():
    users = ''
    for user in user_list:
        users = f'{users}\n{user.name}'
    return users
    