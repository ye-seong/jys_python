class Admin:
    admin_pass = '1234'
    admin_value = True
    error_num = 0

class User:
    name = ''
    id = ''
    password = ''

    def __int__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

class Post:
    post_writer = ''
    post_title = ''
    post_detail = ''
    post_reply = []

    def __int__(self, writer, title, detail, reply):
        self.post_writer = writer
        self.post_title = title
        self.post_detail = detail
        self.post_reply = reply

class Reply:
    reply_writer = ''
    reply_detail = ''

    def __int__(self, writer, detail):
        self.reply_writer = writer
        self.reply_detail = detail

        
    

    