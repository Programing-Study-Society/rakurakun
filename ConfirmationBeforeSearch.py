import Programming_auto_GUI #ファイル分け
import WriteToLog #ファイル分け


#ファイル検索へ送信前にチェックをかける
def Pre_sendCheck(word,teacherMode,log):

    #何も入力されていないとき
    if word == "":
        WriteToLog.writeToLog(log,"検索ワードに何か入力してください",'Black')
        return 50
    #適切な検索ワードが入力されているとき
    else:
        result = Programming_auto_GUI.start(word,teacherMode,log)#ファイル探索・生成機能に移る
        return result