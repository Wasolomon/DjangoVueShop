import re


mobile_regex = re.compile(r'^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,'
                          r'9]))[0-9]{8}$', re.VERBOSE)

email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})$', re.VERBOSE)

username_regex = re.compile(r'^([\u4E00-\u9FA5]|[a-zA-Z0-9_-]){4,16}$', re.VERBOSE)

# 密码强度正则最少6位包括：至少1个大写字母、1个小写字母、1个数字和1个特殊字符
password_regex = re.compile(r'^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*?. ]).*$', re.VERBOSE)


def check_mobile(mobile):
    if mobile_regex.match(mobile):
        return True
    return False


def check_email(email):
    if email_regex.match(email):
        return True
    return False


def check_username(username):
    if username_regex.match(username):
        return True
    return False


def check_password(password):
    if password_regex.match(password):
        return True
    return False


if __name__ == '__main__':
    print(
        mobile_regex.match('18588949187'),
        email_regex.match('solomonwanc@gmail.com'),
        username_regex.match('你好Hello'),
        password_regex.match('123oiuW.')
    )
