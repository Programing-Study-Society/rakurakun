#第一引数のString型Listに、第二引数のパスの中身をコピーする関数
def textExtraction(Destination, textPath):

    #ファイルを開く
    try:#エラー処理
        f = open(textPath, 'r', encoding='CP932')#CP932(shift_jis(Windowsの標準コード))で開けるか試みる(大体ここで通る)
        #ファイルの内容を文字列で受け取る
        data = f.read()

    except UnicodeDecodeError:#開けなかったら別のコーディング方式で試みる
        try:
            f = open(textPath, 'r', encoding='shift_jis')#shift_jis(shift_jis(Windowsの標準コード))で開けるか試みる
            #ファイルの内容を文字列で受け取る
            data = f.read()
            
        except UnicodeDecodeError:#開けなかったら別のコーディング方式で試みる
            try:
                f = open(textPath, 'r', encoding='utf-8')#utf-8で開けるか試みる
                data = f.read()

            except UnicodeDecodeError:#開けなかったら別のコーディング方式で試みる
                try:
                    f = open(textPath, 'r', encoding='utf-16')#utf-16で開けるか試みる
                    data = f.read()

                except UnicodeDecodeError as e:
                    return
                
                except OSError as e:#正常に開けなかったら処理を終了する
                    return
            
            except OSError as e:#正常に開けなかったら処理を終了する
                return
        except OSError as e:#正常に開けなかったら処理を終了する
            return

    except OSError as e:#正常に開けなかったら処理を終了する
        return

    #文字列のリストに格納する
    Destination.append(data)

    f.close()