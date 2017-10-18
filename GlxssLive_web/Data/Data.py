import random


class Data:

    username = "AutoTest@qq.com"
    password = "123456"
    realemail = "102112551@qq.com"

    username_deleted = "test251@qq.com"
    password_deleted = "123456"

    businesscode = "4E7B77"
    businessid = "68"
    businesscode_only = "9BFA21"
    email = "test"+str(random.randint(200, 300))+"@qq.com"
    mobile = "138"+str(random.randint(10000000, 20000000))
    name = "test"

    url = "https://jdev.llvision.com"
    # url = "http://jdev.llvision.com:35012"
    login_url = "https://jdev.llvision.com/login.html"
    register_url = "https://jdev.llvision.com/register.html"
    main_url = "https://jdev.llvision.com/index.html"
    sendemail_url = "https://jdev.llvision.com/mailSend.html"
    fpassword_url = "https://jdev.llvision.com/retrievePassword.html"

    rolename = "role"+str(random.randint(0, 100))
    depname = "dep"+str(random.randint(0, 100))
    devicename = "device"+str(random.randint(0, 1000))
    specialname = "专业"+str(random.randint(0, 1000))
    roomname = "session"+str(random.randint(0, 1000))

    def version(self):
        seed1 = "1234567890"
        seed2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s1 = []
        for i in range(0, 10, 2):
            s1.append(random.choice(seed1))
            s1.append(random.choice(seed2))
        return s1


