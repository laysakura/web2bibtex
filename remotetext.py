from urllib.request import urlopen
from urllib.error import URLError

class RemoteText:
    """リモートのテキスト形式ファイルを，HTTPプロトコルで取得し，指定したエンコーディングで返す．

    引数:
    url: リモートのテキストファイル
    from_encoding='shift_jis': リモートのテキストファイルのエンコーディング
    to_encoding='utf-8': 返すエンコーディング

    Usage:
    板一覧を取得:
    remotetext = RemoteText('http://menu.2ch.net/bbsmenu.html').read()

    VIPのスレ一覧を取得:
    remotetext = RemoteText('http://raicho.2ch.net/news4vip/subject.txt').read()

    スレの内容を取得:
    remotetext = RemoteText('http://raicho.2ch.net/news4vip/dat/1291281711.dat').read()
    """
    def __init__(self, url,
                 from_encoding='shift_jis', to_encoding='utf-8'):
        self.url = url
        self.from_encoding = from_encoding
        self.to_encoding = to_encoding

    def read(self):
        try:
            text = urlopen(self.url).read()
        except URLError as err:
            print(self.url,'のオープンに失敗しました．')
            print(err.reason)
        else:
            text = text.decode(self.from_encoding, 'ignore')
            if self.from_encoding != self.to_encoding:
                try:
                    return text.encode(self.to_encoding, 'ignore').decode(self.to_encoding, 'ignore')
                except UnicodeError as err:
                    print('UTF-8への変換に失敗しました．')
                    print(err)
            else:
                return text
