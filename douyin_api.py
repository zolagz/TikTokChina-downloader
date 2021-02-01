import requests, json, os


########## 解析函数定义 ##########

def get_url_0(in_url=''):
    if in_url == '':
        global url
        in_url=url
    r = requests.post('http://api.btstu.cn/dyjx/api.php', data={'url':in_url})
    text = json.loads(r.text)
    name = text['data']['title']
    url_return = text['data']['videourl']
    return name, url_return

def get_url_1(in_url=''):
    if in_url == '':
        global url
        in_url=url
    r = requests.post('http://qsy.nostr.cn/?url=%s'%(in_url))
    text = json.loads(r.text)
    name = text['data']['title']
    url_return = text['data']['video']
    return name, url_return

def get_url_2(in_url=''):
    if in_url == '':
        global url
        in_url=url
    r = requests.get('http://liuxingw.com/api/douyin/api.php?url=%s'%(in_url))
    start = r.text.index('<video src="')+12
    end = r.text.index('"', start)
    url_return = r.text[start:end]
    if 'http' not in url_return:
        url_return+=1
    return '抖音视频', url_return

def get_url_3(in_url=''):
    if in_url == '':
        global url
        in_url=url
    r = requests.get('http://tool.vast.codes/douyin/?url=%s'%(in_url))
    text = json.loads(r.text)
    url_return = text['resulturl']
    return '抖音视频', url_return

########## 解析函数定义 ##########



########## 主程序 ##########
if __name__=='__main__':
    from time import sleep
    from pyperclip import copy, paste
    import winreg

    def get_desktop():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        return winreg.QueryValueEx(key,"Desktop")[0]
    desktop_path = get_desktop().replace('\\', '/')

    url = input("请输入抖音获取的视频分享链接：")
    if url=='':
        url=paste()

    print('正在解析链接...')
    filename, url_final = '', ''
    for i in range(3):
        if i==0:
            try:
                filename, url_final = get_url_0()
                print("接口编号：%s"%(i))
                break
            except:
                pass
        elif i==1:
            try:
                filename, url_final = get_url_1()
                print("接口编号：%s"%(i))
                break
            except:
                pass
        elif i==2:
            try:
                filename, url_final = get_url_2()
                print("接口编号：%s"%(i))
                break
            except:
                pass
        elif i==3:
            try:
                filename, url_final = get_url_3()
                print("接口编号：%s"%(i))
                break
            except:
                print('所有接口均无正常返回值！即将退出程序...')
                sleep(2)
                os._exit(0)
    print('解析完成！视频链接将会写入您的剪切板，以备后续使用。')
    copy(url_final)

    print('正在下载视频...')
    file = requests.get(url_final)
    print('下载完成！')
    print('正在将视频写入文件...')
    f=open('%s/%s.mp4'%(desktop_path, filename), 'wb')
    f.write(file.content)
    f.close()
    print('写入完成！视频文件在您的桌面上。')

    print('All Done！\n\n'
        '©2021 异想之旅 yixiangzhilv.top & yxzl.top 版权所有'
    )
    input()
########## 主程序 ##########

#https://v.douyin.com/J3yQPNe/