import urllib.request
import urllib.parse
import sys
import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.Load('wiki-ja.model')

def test(text):
  text = sp.EncodeAsPieces(text)
  text = ' '.join(text)

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
