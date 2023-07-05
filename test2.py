import tkinter as tk

app = tk.Tk()
# Windowの画面サイズを設定する。
app.geometry("600x400")

# Windowを親要素として、label Widgetを作成する。
# width : 幅の設定
# height : 高さの設定
# bg : 背景色の設定
label1 = tk.Label(app, width=10, height=10, bg="blue")
# Windowを親要素として、label Widgetを作成する。
# width : 幅の設定
# height : 高さの設定
# bg : 背景色の設定
# 色について　: https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
label2 = tk.Label(app, width=10, height=10, bg="green")
# Windowを親要素として、label Widgetを作成する。
# width : 幅の設定
# height : 高さの設定
# bg : 背景色の設定
# 色について　: https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
label3 = tk.Label(app, width=10, height=10, bg="red")
# Windowを親要素として、label Widgetを作成する。
# width : 幅の設定
# height : 高さの設定
# bg : 背景色の設定
# 色について　: https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
label4 = tk.Label(app, width=10, height=10, bg="purple")

# Windowを親要素として、label Widgetをどのように配置するのか？
label1.grid(column=0, row=0, sticky=tk.NSEW)
# Windowを親要素として、label Widgetをどのように配置するのか？
label2.grid(column=1, row=0, sticky=tk.NSEW)
# Windowを親要素として、label Widgetをどのように配置するのか？
label3.grid(column=0, row=1, sticky=tk.NSEW)
# Windowを親要素として、label Widgetをどのように配置するのか？
label4.grid(column=1, row=1, sticky=tk.NSEW)

# もしくは、app.grid_columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

# Windowをループさせて、継続的にWindow表示させる。
# mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
app.mainloop()