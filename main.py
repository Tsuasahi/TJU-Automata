import time
import requests

def main():
    f = open("config.txt", 'r')
    url =f.readline().strip('\n').strip()
    classid = f.readline().strip('\n').strip()
    cookie = f.readline().strip('\n').strip()
    headers    = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
        'Referer': 'http://classes.tju.edu.cn/eams/stdElectCourse!defaultPage.action',
        'Cookie':  "'" + cookie + "'"
    }
    data={
        'optype': 'true',
        'operator0': classid + ':true:0'
    }

    while True:
        print('课程代码' + str(classid))
        sto = requests.post(url, headers = headers, data = data)
        res=str(sto.content, 'utf-8')
        f.close
        if '成功' in res:
            print('选课成功')
            break
        elif '已经' in res:
            print('已选该课')
            break
        else:
            print('选课失败')
            break

if __name__ == '__main__':
    main()