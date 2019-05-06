import urllib.request
import urllib.parse
import sys
import MeCab

args = sys.argv

text = args[1]
text = MeCab.Tagger("-Owakati").parse(args[1])

#リクエストパラメータをエンコード
params = {"input":text}
encodedParams = urllib.parse.urlencode(params)

print(params)

#エンコードしたリクエストパラメータを付加してAPIコール
with urllib.request.urlopen("http://localhost:5000/?" + encodedParams) as res:
    html = res.read().decode("unicode-escape")
    print(html)
