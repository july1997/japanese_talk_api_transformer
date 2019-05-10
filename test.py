import urllib.request
import urllib.parse
import sys
import MeCab

def test(text):
  text = MeCab.Tagger("-Owakati").parse(text)
  
  #リクエストパラメータをエンコード
  params = {"input":text}
  encodedParams = urllib.parse.urlencode(params)
  
  print(params)

  #エンコードしたリクエストパラメータを付加してAPIコール
  with urllib.request.urlopen("http://localhost:5000/?" + encodedParams) as res:
    html = res.read().decode("unicode-escape")
    print(html)

if __name__ == '__main__':
  args = sys.argv
  test(args[1])
