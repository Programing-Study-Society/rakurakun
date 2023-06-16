import tkinter as tk #GUI化するために使用
from tkinter import filedialog #パスデータ保存用
from tkinter import scrolledtext #logボックスを設置する為に使用
import threading #マルチスレッド機能実装用
import ConfirmationBeforeSearch #ファイル分け
import DetaSave #ファイル分け

#画面サイズに応じてテキストのフォントサイズを変換する関数
def resize_font(event):
    # 画面の幅に基づいてフォントサイズを計算
    screen_width = root.winfo_width()
    font_size = int(screen_width / 65)  # 適宜調整
    # ボタンのフォントサイズを変更
    for (object, textSize) in zip(objects, textSizes):
        object.config(font=('Arial', int(font_size * textSize)))

def fileSearch(word,teacherMode,log):
    #logを消去する
    log['state'] = 'normal' #logを書き込み可能にする
    log.delete("1.0", tk.END)#logのテキストボックスの中身を削除する
    log['state'] = 'disabled'#logを書き込み不可能にする

    #ボタン類を押せないようにする
    for object in objects:
        object['state'] = 'disabled'

    #処理を行う
    result = ConfirmationBeforeSearch.Pre_sendCheck(word,teacherMode,log)

    #正常にファイルを作成できたら、入力欄のテキストを消す(ボタン連打対策)
    if result == 0:
        input_box['state'] = 'normal'
        input_box.delete(0, tk.END) 

    #ボタンを押せるように戻す
    for object in objects:    
        object['state'] = 'normal'

#ファイル検索プログラムをマルチスレッドで実行する関数
def executionControl(word,teacherMode,log):

    #マルチスレッド化
    thread = threading.Thread(target=fileSearch, args=(word,teacherMode,log)) 
    result = thread.start()#マルチスレッドで実行（戻り値は今回は使用せず受け取るだけ）

# フォルダ指定の関数
def dirdialog_clicked(entry):
    initial_dir = entry.get()
    iDirPath = filedialog.askdirectory(initialdir=initial_dir)
    if iDirPath:
        entry.set(iDirPath)
    else:
        entry.set(initial_dir)

#データを保存する関数にパスを送って、タブを閉じる関数
def putpath(entry1, entry2, entry3, setting_win):

    DetaSave.detaSave('Storage_Path',entry1.get())
    DetaSave.detaSave('Program_Path',entry2.get())
    DetaSave.detaSave('Image_Path',entry3.get())

    #logを消去する
    log['state'] = 'normal' #logを書き込み可能にする
    log.delete("1.0", tk.END)#logのテキストボックスの中身を削除する
    log['state'] = 'disabled'#logを書き込み不可能にする

    setting_win.destroy()

#設定ウィンドウを閉じようとしたときに呼び出される関数
def click_close(entry1, entry2, entry3, setting_win):
    #設定が最新の状態かチェックする
    if entry1.get() == DetaSave.detaLoad('Storage_Path', log) and entry2.get() == DetaSave.detaLoad('Program_Path', log) and entry3.get() == DetaSave.detaLoad('Image_Path', log):
        setting_win.destroy()#設定が最新の状態なら設定ウィンドウを閉じる
    
    else:#設定が反映されていなければ確認を促す
        if tk.messagebox.askokcancel("確認", "変更が保存されていません\n変更を保存をせずにタブを閉じますか？"):
            setting_win.destroy()


#設定ウィンドウの作成
def settingWindow():

    #ウィンドウの作成
    setting_win = tk.Toplevel()

    setting_win.title("Setting")

    #ウィンドウのサイズ設定
    setting_win.geometry("450x300")

    #親ウィンドウを触れなくする
    setting_win.grab_set()

    #ウィンドウのサイズを固定にする
    setting_win.resizable(width=False, height=False)

    #「設定」という文字を表示する
    setting_text = tk.Label(setting_win, text='設定', font=("Arial", "18"))
    setting_text.place(x = 200, y = 0)


    #「保存先のパス」という文字を表示する
    setting_text = tk.Label(setting_win, text='保存先のパス', font=("Arial", "15"))
    setting_text.place(x = 250, y = 70)

    # 保存先「ファイル参照」エントリーの作成
    entry1 = tk.StringVar()
    entry1.set(DetaSave.detaLoad('Storage_Path', log))
    IFileEntry = tk.Entry(setting_win, textvariable=entry1, width=25,)
    IFileEntry.place(x = 250, y = 100, height=30)

    # 保存先「ファイル参照」ボタンの作成
    IFileButton = tk.Button(setting_win, text="参照", command=lambda:dirdialog_clicked(entry1))
    IFileButton.place(x = 410, y = 100, height=30, width=40)


    #「プログラムファイルのパス」という文字を表示する
    setting_text = tk.Label(setting_win, text='プログラムファイルのパス', font=("Arial", "15"))
    setting_text.place(x = 0, y = 70)

    # プログラムファイルのパス「ファイル参照」エントリーの作成
    entry2 = tk.StringVar()
    entry2.set(DetaSave.detaLoad('Program_Path', log))
    IFileEntry = tk.Entry(setting_win, textvariable=entry2, width=25,)
    IFileEntry.place(x = 0, y = 100, height=30)

    # プログラムファイルのパス「ファイル参照」ボタンの作成
    IFileButton = tk.Button(setting_win, text="参照", command=lambda:dirdialog_clicked(entry2))
    IFileButton.place(x = 160, y = 100, height=30, width=40)


    #「画像ファイルのパス」という文字を表示する
    setting_text = tk.Label(setting_win, text='画像ファイルのパス', font=("Arial", "15"))
    setting_text.place(x = 0, y = 150)

    # 画像ファイルのパス「ファイル参照」エントリーの作成
    entry3 = tk.StringVar()
    entry3.set(DetaSave.detaLoad('Image_Path', log))
    IFileEntry = tk.Entry(setting_win, textvariable=entry3, width=25,)
    IFileEntry.place(x = 0, y = 180, height=30)

    # 画像ファイルのパス「ファイル参照」ボタンの作成
    IFileButton = tk.Button(setting_win, text="参照", command=lambda:dirdialog_clicked(entry3))
    IFileButton.place(x = 160, y = 180, height=30, width=40)

    #保存ボタンの作成
    IFileButton = tk.Button(setting_win, text="保存",font=("Arial", "10"), command=lambda:putpath(entry1, entry2, entry3, setting_win))
    IFileButton.place(x = 180, y = 260, width=100)

    #タブを閉じるときに、データが保存されているかの確認
    setting_win.protocol("WM_DELETE_WINDOW", lambda:click_close(entry1, entry2, entry3, setting_win))



#このスクリプトがメインなら実行
if __name__ == "__main__":

    # ウィンドウの作成
    root = tk.Tk()
    root.title("Program AND Image => Word AND PDF")

    # ウィンドウのサイズ指定
    root.geometry("600x400")

    # ウィンドウサイズの変更を検知するためのフレーム
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)
    frame.bind('<Configure>', resize_font)

    # ボタンを格納
    objects = []
    ##resize_font関数で使う、フォントサイズを決める値を格納
    textSizes = []

    #「ログ」という文字を表示する
    setting_text = tk.Label(root, text='ログ')#テキストの定義
    setting_text.place(relx = 0.075, rely = 0.425)#テキストを配置
    objects.append(setting_text)#テキストをリストに格納(フォントサイズ調整のため)
    textSizes.append(2)#resize_font関数で使う、フォントサイズを決める値

    #「検索ワード」という文字を表示する
    setting_text = tk.Label(root, text='検索ワード')#テキストの定義
    setting_text.place(relx = 0.075, rely = 0.24)#テキストを配置
    objects.append(setting_text)#テキストをリストに格納(フォントサイズ調整のため)
    textSizes.append(2)#resize_font関数で使う、フォントサイズを決める値

    # 入力テキストボックス設置
    input_box = tk.Entry()#入力テキストボックスの定義  
    input_box.place(relx = 0.3, rely = 0.25,relwidth=0.4, relheight=0.064)#入力テキストボックスを配置
    objects.append(input_box)#入力テキストボックスをリストに格納(フォントサイズ調整のため)
    textSizes.append(1)#resize_font関数で使う、フォントサイズを決める値

    #logボックスの設置
    log = scrolledtext.ScrolledText(root,state='disabled',borderwidth=5, background="#dcdcdc")#logボックスの定義
    log.place(relx = 0.08, rely = 0.5,relwidth=0.85, relheight=0.4)#logボックスの配置
    objects.append(log)#logテキストボックスをリストに格納(フォントサイズ調整のため)
    textSizes.append(1)#resize_font関数で使う、フォントサイズを決める値

    # 作成：阪口先生ボタン設置
    sakaguchi_button = tk.Button(root, text = "作成：阪口先生", command = lambda:executionControl(input_box.get(), "0",log))#ボタンの定義
    sakaguchi_button.place(relx = 0.3, rely = 0.325, relwidth=0.15, relheight=0.064)#ボタンの配置
    objects.append(sakaguchi_button)#ボタンをリストに格納(フォントサイズ調整のため)
    textSizes.append(1)#resize_font関数で使う、フォントサイズを決める値

    # 作成：岩本先生ボタン設置
    iwamoto_button = tk.Button(root, text = "作成：岩本先生", command = lambda:executionControl(input_box.get(), "1",log))#ボタンの定義
    iwamoto_button.place(relx = 0.55, rely = 0.325, relwidth=0.15, relheight=0.064)#ボタンの配置
    objects.append(iwamoto_button)#ボタンをリストに格納(フォントサイズ調整のため)
    textSizes.append(1)#resize_font関数で使う、フォントサイズを決める値

    # 設定ボタン設置
    setting_button = tk.Button(root, text = "設定", height = 5, width = 20, command = settingWindow)#ボタンの定義
    # setting_button.place(relx = 0.755, rely = 0.43, relwidth=0.15, relheight=0.064)#ボタンの配置
    setting_button.place(relx = 0.805, rely = 0.05, relwidth=0.15, relheight=0.1)#ボタンの配置
    objects.append(setting_button)#ボタンをリストに格納(フォントサイズ調整のため)
    textSizes.append(1.5)#resize_font関数で使う、フォントサイズを決める値

    # ウィンドウ状態の維持
    root.mainloop()