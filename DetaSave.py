import shelve #設定をデータに保存する用
import WriteToLog #ファイル分け

#modeで受け取る値一覧
#'Storage_Path'
#'Program_Path'
#'Image_Path'

#パスを保存する関数
def detaSave(mode,Path):
    
    #先頭に"が付いていたら"を外す
    if(Path.startswith('"')):
        Path = Path[1:]
    #最後尾に"が付いていたら"を外す
    if(Path.endswith('"')):
        Path = Path[:-1]
    #最後尾に/や\\が付いていなかったら\\を付け加える
    if(not(Path.endswith("/") or Path.endswith("\\"))):
        Path += '\\'
    #mydataファイルを開く
    f = shelve.open('mydata')
    #ファイルにパスを保存する
    f[mode] = Path
    #ファイルを閉じる
    f.close()

#ファイルからデータを取り出す。
def detaLoad(mode, log):

    f = shelve.open('mydata')#ファイルを開く
    try:
        path = f[mode]#ファイルからデータ祖取り出す
        f.close()#ファイルを閉じる
        return path
    except KeyError:#取り出せなかった時の処理
        WriteToLog.writeToLog(log, mode + "が正常に読み込めませんでした。再設定を推奨します",'Red')
        f.close()#ファイルを閉じる
        return '読み込みエラー'