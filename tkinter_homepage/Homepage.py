import os # 운영체제 모듈


class User:
    name = ''
    id = ''
    password = ''


    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

    def SameInfo(self, name, id):
        if self.name and self.id == id:
            print('같은 이름과 아이디가 있습니다. 다시 설정해주세요.')
            return True
        elif self.name == name:
            print('같은 이름이 있습니다. 다시 설정해주세요.')
        elif self.id == id:
            print('같은 아이디가 있습니다. 다시 설정해주세요.')
            return True
        else:
            return False

class Admin:
    admin_pass = '1234'
    admin_value = True
    error = 0

class Reply:
    reply_writer = ''
    reply_detail = ''

class Post:
    post_title = ''
    post_writer = ''
    post_detail = ''
    post_reply = []
    

    def __init__(self,title,writer,detail, reply):
        self.post_title = title
        self.post_writer = writer
        self.post_detail = detail
        self.post_reply = reply

def clearScreen(): # os 에 특화된 팁.
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'

    os.system(command)


def addToUserDB(items: list):
    f = open('user_db.txt', encoding='utf-8', mode='w')
    for item in items:
        f.write(f'{item.name}|')
        f.write(f'{item.id}|')
        f.write(f'{item.password}\n')

    f.close()


def addToPostDB(items: list):
    f = open('post_db.txt', encoding='utf-8', mode='w')
    for item in items:
        f.write(f'{item.post_title}|')
        f.write(f'{item.post_writer}|')
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

        user = User(name,id,password)
        user_list.append(user)
    f.close()


def LoadPostFromDB(items: list):
    f = open('post_db.txt', encoding='utf-8', mode='r')

    while True:
        line = f.readline().replace('\n', '')
        if not line: break
        
        lines = line.split('|')
        title = lines[0]
        writer = lines[1]
        detail = lines[2]
        reply = lines[3]

        post = Post(title,writer,detail, reply)
        post_list.append(post)
    f.close()

def adminMode_Service(service):
    clearScreen() # 최초에 화면 클리어
    if service == '유저정보':
        clearScreen() # 최초에 화면 클리어
        for user in user_list:
            print(f'이름 : {user.name}')
            print(f'아이디 : {user.id}')
            print(f'비밀번호 : {user.password}')
            print('====================================================')

    elif service == '조회수':
        clearScreen() # 최초에 화면 클리어
        print('아직 정보가 없습니다.')

    input()
    adminMode()

    
def adminMode():
    clearScreen() # 최초에 화면 클리어
    admin_service = input('유저정보 | 조회수 | 뒤로가기 > ')
    if admin_service == '유저정보' or admin_service == '조회수':
        adminMode_Service(admin_service)
    elif admin_service == '뒤로가기':
        main()
    else:
        print('다시 입력 해주세요.')
        input()
        adminMode()

def addPost(user, num):
    clearScreen() # 최초에 화면 클리어    
    title = input('게시물 제목 : ')
    writer = user.name
    detail = input('내용 : ')
    reply = []

    save = input('저장하시려면 save를 입력해주세요. 원하지 않을시 엔터를 쳐주세요. : ')
    if save == 'save':
        post_info = Post(title,writer,detail,reply)
        post_list.append(post_info)
        addToPostDB(post_list)
        userMode_Service('자유게시판', num)
    else:
        userMode_Service('자유게시판', num)

def writeReply(num):
    clearScreen() # 최초에 화면 클리어
    curr_post = post_list[num]
    while True:
        reply = input('댓글을 입력하세요. (취소는 뒤로가기) > ')
        if reply == '':
            print('다시 입력하세요.')
        elif reply == '뒤로가기':
            showPost(num)
        else:
            curr_post.post_reply.reply_detail.append(reply)
            showReply(num)

def showReply(num):
    curr_post = post_list[num]

    if len(curr_post.post_reply) < 1:
        print('현재 댓글이 없습니다.')
    else:    
        for reply in curr_post.post_reply:
            print(f'ㄴ {reply}')

    while True:
        write_reply = input(' 댓글쓰기 | 뒤로가기 > ')
        if write_reply == '댓글쓰기':
            writeReply(num)
        elif write_reply == '뒤로가기':
            clearScreen() # 최초에 화면 클리어
            showPost(num)
        

def showPost(num):
    clearScreen() # 최초에 화면 클리어
    curr_post = post_list[num]
    title = curr_post.post_title
    writer = curr_post.post_writer
    detail = curr_post.post_detail

    print(f'제목 : {title}')
    print(f'글쓴이 : {writer}')
    print('=============================================')
    print(f'내용 : {detail}')
    print('=============================================')
    print(showReply(num))
    

def userMode_Service(service, num):
    clearScreen() # 최초에 화면 클리어    
    curr_user = user_list[num]

    if service == '개인정보':
            clearScreen() # 최초에 화면 클리어
            print(f'이름 : {curr_user.name}')
            print(f'아이디 : {curr_user.id}')
            print(f'비밀번호 : {curr_user.password}')
            while True:
                go_back = input('뒤로 가시겠습니까? (Y) > ').upper()
                if go_back == 'Y':
                    userMode(num)
                    break
                else:
                    continue

    elif service == '유저리스트':
        clearScreen() # 최초에 화면 클리어
        for user in user_list:
            print(user.name)
        while True:
                go_back = input('뒤로 가시겠습니까? (Y) > ').upper()
                if go_back == 'Y':
                    userMode(num)
                    break
                else:
                    continue

    elif service == '자유게시판':
        number = 0
        clearScreen() # 최초에 화면 클리어
        for post in post_list:
            number += 1
            print(f'[{number}] {post.post_title}')
        work = input('열람을 원하는 게시물 번호를 입력하세요. 게시물 추가를 원할시 0을 입력해주세요. > ')
        if int(work) == 0:
            addPost(curr_user,num)
        else:
            showPost(int(work)-1)

    elif service == '탈퇴':
        clearScreen() # 최초에 화면 클리어
        while True:
                answer = input('정말로 탈퇴 하시겠습니까? (Y) > ').upper()
                if answer == 'Y':
                    del(user_list[num])
                    print('탈퇴 되었습니다.')
                    input()
                    clearScreen()
                    selectLoginAccout()
                    break
                else:
                    print('탈퇴가 취소 되었습니다.')
                    input()
                    clearScreen()
                    userMode(num)
                    break
            
    elif service == '뒤로가기':
        selectLoginAccout()
    
    else:
        print('다시 입력 해주세요.')
        userMode(num)


def userMode(num):
    clearScreen() # 최초에 화면 클리어
    print('=========================파이썬 홈페이지 입니다.===========================')
    mode = input('개인정보 | 유저리스트 | 자유게시판 | 탈퇴 | 뒤로가기 > ')
    userMode_Service(mode, num)


def user_account(mode):
    clearScreen() # 최초에 화면 클리어
    
    if mode == '로그인':
        print('=========================로그인 페이지 입니다.===========================')
        id_input = input('아이디 > ')
        pass_input = input('비밀번호 > ')

        user_num = 0

        for user in user_list:
            if user.id == id_input and user.password == pass_input:
                print(f'{user.name}님. 환영합니다.')
                userMode(user_num)
            else:
                user_num += 1
                if user_num == len(user_list):
                    print('아이디 및 비밀번호를 다시 확인해주세요.')
                    selectLoginAccout()

    elif mode == '회원가입':
        print('=========================회원가입 페이지 입니다.===========================')
        check = False
        while True:
            name_info = input('이름을 입력하세요. > ')
            id_info = input('아이디를 입력하세요. > ')
            pass_info = input('비밀번호를 입력하세요. > ')

            for user in user_list:
                test = User(user.name, user.id, user.password)
                check = test.SameInfo(name_info, id_info)
                if check:
                    user_account('회원가입')

            if name_info == '' or id_info == '' or pass_info == '':
                print('다시 입력 해주세요.')

            else:
                if check == False:
                    print('가입이 완료되었습니다')
                    info = User(name_info, id_info, pass_info)
                    user_list.append(info)
                    addToUserDB(user_list)
            
            input()
            selectLoginAccout()

    elif mode == '뒤로가기':
        selectLoginAccout()


def selectLoginAccout():
    clearScreen() # 최초에 화면 클리어
    choice = input('로그인 | 회원가입 | 뒤로가기 > ')
    if choice == '로그인' or choice == '회원가입':
        user_account(choice)

    elif choice == '뒤로가기':
        main()

    else:
        print('다시 입력 해주세요.')

    input()
    main()

def main():
    clearScreen() # 최초에 화면 클리어

    while True:
        mode = input('접속하실 모드를 입력 해주세요. ( 관리자 | 사용자 ) > ')
        clearScreen()
        if mode == '관리자':
            if Admin.admin_value == False:
                print('비밀번호 3회 오류로 관리자 페이지에 접속 할 수가 없습니다.')
            while Admin.admin_value:
                admin_pass_input = input('관리자 비밀번호 > ')
                if admin_pass_input == Admin.admin_pass:
                    print('관리자 모드에 접속 하셨습니다.')
                    adminMode()
                else:
                    Admin.error += 1
                    if Admin.error >= 3:
                        print('비밀번호가 3회 틀렸습니다. 이전 페이지로 돌아갑니다')
                        Admin.admin_value = False
                        break
                    else:
                        print(f'비밀번호가 맞지 않습니다. (오류 {Admin.error}회. 3회 오류시 닫힙니다.)')
                        input()
                        main()
        elif mode == '사용자':
            selectLoginAccout()
            
        else:
            print('유효하지 않은 페이지 입니다.')

print('========================파이썬에 오신걸 환영합니다.===========================')
user_list = []
post_list = []

LoadUserFromDB(user_list)
LoadPostFromDB(post_list)


main()

