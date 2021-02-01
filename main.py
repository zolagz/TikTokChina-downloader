import douyin_api

html='''
<!DOCTYPE html>
<html>

<head>
    <script>
        function copyToClipboard(s) {
            if (window.clipboardData) {
                window.clipboardData.setData('text', s);
                alert("复制成功！请粘贴到浏览器地址栏。");
            } else {
                (function(s) {
                    document.oncopy = function(e) {
                        e.clipboardData.setData('text', s);
                        e.preventDefault();
                        document.oncopy = null;
                    }
                })(s);
                document.execCommand('Copy');
            }
        }
    </script>
</head>


<body onload="copyToClipboard('%s')">
    <a onclick="copyToClipboard('%s')">点我复制链接</a>
</body>

</html>
'''

from flask import Flask, request
app=Flask(__name__)
'''
@app.route('/<url>')
def index(url):
    global html
    url="https://v.douyin.com/%s/"%(url)
    url=douyin_api.get_url_0(url)[1]
    print(url)
    return html%(url)
'''
@app.route('/')
def index():
    global html
    url=request.args.get('url')
    print(url)
    url=douyin_api.get_url_1(url)[1]
    #print(url)
    return html%(url, url)
if __name__ == '__main__':
    app.debug=True
    app.run()