import tkinter as tk #GUI化するために使用
import tkinter.ttk as ttk #ファイル選択ウィンドウのスクロールバーを調整する為に使用

#ファイル選択ウィンドウの作成
def makeList(programPaths):

    rt_width = 600
    rt_hgt = 300

    #ウィンドウの作成
    makeList_win = tk.Toplevel()

    makeList_win.title("FileSelection")

    #ウィンドウのサイズ設定
    makeList_win.geometry(str(rt_width)+'x'+str(rt_hgt))

    #親ウィンドウを触れなくする
    makeList_win.grab_set()

    #ウィンドウのサイズを固定にする
    makeList_win.resizable(width=False, height=False)

    num_list = len(programPaths)  # リストの数
    list_plot_keyword = [] # チェックされているkeywordを取ってくる

    # Canvas widgetを生成
    cv_width = rt_width - 20
    cv_hgt = rt_hgt - 70
    canvas = tk.Canvas(makeList_win, width=cv_width, height=cv_hgt, bg='white')  # 背景を白に
    canvas.grid(row=1, rowspan=num_list, column=0, columnspan=5)     # 5列分

    # スクロールバー
    vbar = ttk.Scrollbar(makeList_win, orient=tk.VERTICAL)  # 縦方向
    vbar.grid(row=1, rowspan=25, column=5, sticky='ns')

    # スクロールバーの制御をCanvasに通知する処理
    vbar.config(command=canvas.yview)

    # Canvasの可動域をスクロールバーに通知する処理
    canvas.config(yscrollcommand=vbar.set)

    # スクロール可動域＜＝これがないと、どこまでもスクロールされてしまう。
    sc_hgt = 25 * (num_list + 1)
    print(str(sc_hgt))
    canvas.config(scrollregion=(0, 0, cv_width, sc_hgt))

    # Frameを作成
    frame = tk.Frame(canvas, bg='white')  # 背景を白に

    # frameをcanvasに配置
    canvas.create_window((0, 0), window=frame, anchor=tk.NW, width=canvas.cget('width'))  # anchor<=NWで左上に寄せる

    #各ラベルの幅(文字がある場合は文字ユニットとなる)
    c0_width = 5  # チェックボックス
    c1_width = 75 # 検索キーワード


    # header row=1に設定する文字列 余白は0に
    e0 = tk.Label(frame, width=c0_width, text='select', background='white')
    e0.grid(row=1, column=0, padx=0, pady=0, ipadx=0, ipady=0)  # 0列目

    e1 = tk.Label(frame, width=c1_width, text='program', background='white', anchor='w')
    e1.grid(row=1, column=1, padx=0, pady=0, ipadx=0, ipady=0)  # 1列目

    irow = 2
    irow0 = 2
    erow = num_list + irow0

    list_chk = []

    while irow < erow:  # リストの数分ループしてLabelとチェックボックスを設置
        # 色の設定
        if irow % 2 == 0:
            color = '#cdfff7'  # 薄い青
        else:
            color = 'white'

        # チェックボックスの設置
        bln = tk.BooleanVar()
        bln.set(False)
        c = tk.Checkbutton(frame, variable=bln, width=c0_width, text='', background='white')
        list_chk.append(bln)  # チェックボックスの初期値
        c.grid(row=irow, column=0, padx=0, pady=0, ipadx=0, ipady=0)  # 0列目
        # 検索キーワード
        a1 = programPaths[irow - irow0]
        b1 = tk.Label(frame, width=c1_width, text=a1, background=color, anchor='w')
        b1.grid(row=irow, column=1, padx=0, pady=0, ipadx=0, ipady=0)  # 1列目
        # 検索順位
        
        irow=irow+1
        
        #リストの下に設置するボタン
        allSelectButton = tk.Button(makeList_win,text='全て選択',command=lambda:allSelect_click(list_chk))
        allSelectButton.grid(row=erow,column=0)  #1列目
        allClearButton = tk.Button(makeList_win, text='選択解除',command=lambda:allClear_click(list_chk))
        allClearButton.grid(row=erow, column=1)   #1列目
        # plotButton = tk.Button(makeList_win, text='make plot',command=lambda:make_plot(list_plot_keyword,programPaths,list_chk))
        # plotButton.grid(row=erow,column=2)   #2列目
        EndButton = tk.Button(makeList_win, text='選択完了',command=lambda:make_plot(list_plot_keyword,programPaths,list_chk))
        EndButton.grid(row=erow,column=3)   #3列目

#全て選択をクリック
def allSelect_click(list_chk):
	for i in range(len(list_chk)):
		list_chk[i].set(True)

#選択解除をクリック
def allClear_click(list_chk):
	for i in range(len(list_chk)):
		list_chk[i].set(False)

#プロット作成ボタンをクリック（現状はチェックの状態を調べるのみ）
def make_plot(list_plot_keyword, list_keyword, list_chk):
	
	print('make_plot')
	
	num_list = len(list_keyword)
	
	for ilist in range(num_list):
		bln = list_chk[ilist].get()   #checkbuttonの値
		if bln == True:  #チェック済みの行
			list_plot_keyword.append(list_keyword[ilist])