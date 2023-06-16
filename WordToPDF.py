import pythoncom #COMランタイムの制御
import Improved_docx2pdf #wordファイルをpdfに変換する為に使用（ファイル分け）
import WriteToLog #ファイル分け

#wordをpdfに変換する関数
def word_to_pdf(input_path, output_path, log):
    pythoncom.CoInitialize()#COMランタイムを初期化
    for i in range(10):#エラーが起こった場合、再挑戦を10回まで行う
        WriteToLog.writeToLog(log, input_path + " => PDFに変換中...",'Black')
        try:
            Improved_docx2pdf.convert(input_path, output_path)#ワードファイルをPDFに変換する
            pythoncom.CoUninitialize()#COMランタイムの終了処理
            WriteToLog.writeToLog(log, "変換が完了しました",'Black')
            return
        except Exception as e:
            WriteToLog.writeToLog(log, f"変換中にエラーが発生しました: {str(e)}",'Black')
            WriteToLog.writeToLog(log, "再チャレンジを行います " + str(i + 1) + "回目 / 10回",'Black')
    WriteToLog.writeToLog(log, "エラーを解消できませんでした",'Red')
    WriteToLog.writeToLog(log, "該当ファイルを別アプリで開いていませんか？",'Red')