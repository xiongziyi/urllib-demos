
import  urllib.request
import  re
# url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%BF%A8%CD%A8%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
#     "Referer":url
# }
# rep = urllib.request.Request(url=url,headers=headers)
# resp = urllib.request.urlopen(rep).read().decode()
# image_urls = re.findall(r'"thumbURL":"(.*?)"',resp,re.S)
# file_paths = []
# for i in range(0,len(image_urls)):
#     file_paths.append(image_urls[i].split('/')[-1])
# for i in range(0,len(image_urls)):
#     req = urllib.request.Request(image_urls[i],headers=headers)
#     resp = urllib.request.urlopen(req).read()
#     with open(file_paths[i],'wb') as f:
#         f.write(resp)


class Get_picture():
    def __init__(self):
        self.url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%BF%A8%CD%A8%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'
        self.headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                "Referer":self.url
        }

    def get_images_urls(self):
            rep = urllib.request.Request(url=self.url,headers=self.headers)
            resp = urllib.request.urlopen(rep).read().decode()
            image_urls = re.findall(r'"thumbURL":"(.*?)"',resp,re.S)
            return  image_urls
    def get_file_paths(self):
            file_paths = []
            image_urls = self.get_images_urls()
            for i in range(0,len(image_urls)):
               file_paths.append(image_urls[i].split('/')[-1])
            return file_paths
    def save_picture(self):
            image_urls = self.get_images_urls()
            file_paths = self.get_file_paths()
            for i in range(0,len(image_urls)):
                req = urllib.request.Request(url=image_urls[i],headers=self.headers)
                resp = urllib.request.urlopen(req).read()
                with open(file_paths[i],'wb') as f:
                    f.write(resp)


a = Get_picture()
a.save_picture()