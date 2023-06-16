# import threading#マルチスレッド
# import time

# #文字の色をsec秒だけ変える関数
# def ColorChange(log,sec,color):

#     log['state'] = 'normal' #logを書き込み可能にする
#     log['foreground'] = 'White'#文字の色を白に変える
#     log['state'] = 'disabled'#logを書き込み不可能にする

#     time.sleep(sec)#sec秒待機

#     log['state'] = 'normal' #logを書き込み可能にする
#     log['foreground'] = color#文字の色をcolorに変える
#     log['state'] = 'disabled'#logを書き込み不可能にする

#logにmsg出力する関数
def writeToLog(log,msg,color): 

    log['state'] = 'normal' #logを書き込み可能にする
    if log.index('end-1c')!='1.0': #もし最後の行が空白ではなければ
        log.insert('end', '\n') #改行する
    log.insert('end', msg) #最後の行にmsgを追加する
    log.see("end")
    log['foreground'] = color#文字の色をcolorに変える
    log['state'] = 'disabled'#logを書き込み不可能にする

    #文章が更新されたことがわかるように一瞬だけ文字の色を変える（文字が反映されないエラーが多いので機能削除）
    #thread = threading.Thread(target=ColorChange, args=(log,0.25,color)) 
    #thread.start()