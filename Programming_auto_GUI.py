import os #ファイル検索に使用
import shelve #設定をデータに保存する用
import tkinter as tk #確認ダイアログを出す用
import WriteToWordAndPDF #ファイル分け
import TextExtraction #ファイル分け
import WriteToLog #ファイル分け
import MakeList #ファイル分け

#ログが変わっていることをわかりやすくするための工夫
#MakeListのタブを終了させたときの処理

#P02-AB_XX.cppのXXが2桁だと引っかからなくなった

#プログラムコードに関しては名前指定無しでも良いのではないか（ファイル分け対策）
#プログラミングの授業範囲を見て、先に対処
#教訓：改ページ位置の調整、画像が複数枚の課題の処理、pdfを連続で作成する処理は大変だった

def start(word,teacherMode,log):
    ImCnt = 0
    ProCnt = 0

    #隠しコマンド
    if word == "erro":
        WriteToLog.writeToLog(log,"疲労困憊のはろやんがerrorを吐いた結果...「eero」えっろ",'Black')
        
    #ファイルからデータを取り出す。
    f = shelve.open('mydata')
    try:
        Program_path = f['Program_Path']
    except KeyError:
        WriteToLog.writeToLog(log,"プログラムファイルのパスが正常に読み込めませんでした。再設定を推奨します",'Red')
        return -2
    try:
        Image_path = f['Image_Path']
    except KeyError:
        WriteToLog.writeToLog(log,"画像ファイルのパスが正常に読み込めませんでした。再設定を推奨します",'Red')
        return -3
    try:
        put_path = f['Storage_Path']
    except KeyError:
        WriteToLog.writeToLog(log,"保存先のパスが正常に読み込めませんでした。再設定を推奨します",'Red')
        return -4
    f.close()

    dir_name = put_path + word#フォルダのパスを設定する(保存先のパス + 検索ワード)

    data_number = 1#整頓するデータの最低数指定



    try:
        ProgramList = os.listdir(Program_path)# プログラムファイルを検索
    except FileNotFoundError:
        WriteToLog.writeToLog(log,"指定されたプログラムファイルのパスが存在しませんでした",'Red')
        return -5
    try:
        Imagelist = os.listdir(Image_path)
    except FileNotFoundError:
        WriteToLog.writeToLog(log,"指定された画像ファイルのパスが存在しませんでした",'Red')
        return -6

    if(len(ProgramList) + len(Imagelist) >= data_number):#データが〇件以上(デフォ1)ヒットしたら検索を続行する
            
        Prdata_files = ProgramList
        Imdata_files = Imagelist

        #画像ファイルの名前を保存するリスト
        imageNames = list()

        #画像ファイルを探す
        for files in Imdata_files:
            if(files.startswith(word) and (files.endswith(".png") or files.endswith(".gif") or files.endswith(".jpe") or files.endswith(".jpg"))):
                imageNames.append(files)
                ImCnt += 1
            else:
                pass
        
        #プログラムファイルのパスを保存するリスト
        programPaths = list()
        #見つかったプログラムのファイル名(.cpp,.c無し)を格納するリスト
        codeNames = list()

        #プログラムファイルを探す
        for files in Prdata_files:
            if(files.startswith(word)):
                codeNames.append(files)
                tmpPr_Path = os.path.join(Program_path, files,files) + '/'
                #ファイルパスが見つかるかトライ
                try:
                    file = os.listdir(tmpPr_Path)
                #ファイルパスが見つからなければそのファイルを飛ばす
                except  FileNotFoundError:
                    continue
                for files2 in file:
                    if(files2.startswith(word) and (files2.endswith(".cpp") or files2.endswith(".c"))):
                        programPaths.append(tmpPr_Path + files2)
                        ProCnt += 1
                    else:
                        pass
            else:
                pass
        
        if(ProCnt == 0 and ImCnt == 0):
            WriteToLog.writeToLog(log,"対象ファイルが1つも見つかりませんでした",'Red')
            return -7
        elif(ProCnt == 0):
            WriteToLog.writeToLog(log,"プログラムファイルが見つかりませんでした",'Red')
            return -8
        
        #対象ファイルを選択するチェックボックスウィンドウを表示する
        decisions = MakeList.makeList(codeNames)#decisionsは(挿入,非挿入),(True,False)の配列

        print(decisions)

        #選択されずに回ってきたら処理をここで終了する
        if(decisions == -1): 
            WriteToLog.writeToLog(log,"プログラムファイルが選択されませんでした",'Red')
            return-13

        #選択されたプログラムを仮代入する配列
        programPaths2 = []
        codeNames2 = []

        #選択されたプログラムだけを取り出す
        ProCnt = 0
        for i in range(len(decisions)):
            if(decisions[i]):
                programPaths2.append(programPaths[i])
                codeNames2.append(codeNames[i])
                ProCnt += 1
        programPaths = programPaths2
        codeNames = codeNames2

        print("選択されたプログラム : ")
        print(codeNames)

        #選択された画像を仮代入するリスト
        imageNames2 = list()
        #選択されたプログラムの画像だけを取り出す
        ImCnt = 0
        for code in codeNames:
            for image in imageNames:
                if((image.startswith(code)) and not(image[len(code)].isdigit())):
                    imageNames2.append(image)
                    imageNames.remove(image)
                    ImCnt += 1
        
        imageNames = imageNames2
        print("image : ")
        print(imageNames2)
        
        if(ProCnt == 0 and ImCnt == 0):
            WriteToLog.writeToLog(log,"対象ファイルが1つも見つかりませんでした",'Red')
            return -7
        elif(ProCnt == 0):
            WriteToLog.writeToLog(log,"プログラムファイルが見つかりませんでした",'Red')
            return -8
        elif(ImCnt == 0):
            WriteToLog.writeToLog(log,"画像ファイルが見つかりませんでした",'Red')
            if not tk.messagebox.askokcancel("確認", "画像ファイルが見つかりませんでした\n続行しますか？"):
                return -10
        elif(ImCnt < ProCnt):
            WriteToLog.writeToLog(log,"画像ファイルがプログラムファイルの数より少ない状態です",'Red')
            if not tk.messagebox.askokcancel("確認", "画像ファイルがプログラムファイルの数より少ないです\n続行しますか？"):
                return -11

        #ファイルを保存するフォルダを作成する
        try:
            os.mkdir(dir_name)

        except FileExistsError:
            WriteToLog.writeToLog(log,"すでに同じ名前のフォルダが存在しています",'Red')
            if not tk.messagebox.askokcancel("確認", "すでに同じ名前のフォルダが存在しています\n続行しますか？"):
                return -12
        except FileNotFoundError:
            WriteToLog.writeToLog(log,"保存先ファイルの指定されたパスが存在しませんでした",'Red')
            return -9

        dir_name_path = dir_name + '/'
        
        #プログラムファイルの中身(プログラム)を格納するリスト
        Destinations = list()

        #プログラムのパスから中身を取り出してリストに格納する
        for programPath in programPaths:
            TextExtraction.textExtraction(Destinations,programPath)
        
        #阪口先生の保存先(ファイル名)を設定
        if(teacherMode == "0"):
            savePaths = dir_name_path + word
        #岩本先生の保存先(ファイル名)を設定
        elif(teacherMode == "1"):
            savePaths = list()
            for codeName in codeNames:
                savePaths.append(dir_name_path + codeName)
        
        #wordファイルとPDFファイルを作成する
        WriteToWordAndPDF.wordWrite(codeNames, Destinations, imageNames, Image_path, savePaths, teacherMode, log)

        WriteToLog.writeToLog(log,"全てのファイルの保存が終了しました",'Black')
        return 0

    else:
        WriteToLog.writeToLog(log,"ファイルが見つかりませんでした",'Red')
        return -1