#!/Users/caroline_physic/PycharmProjects/pythonProject
# -*- coding: utf-8 -*-


import tkinter as tk  # 使用Tkinter前需要先导入
import sys
import tkinter.messagebox
import pickle
from tkinter import ttk
from csv import DictWriter
import os

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('粘滞系数计算系统')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
l = tk.Label(window, width=50, fg='red', font=('Arial', 20), text='''欢迎来到粘滞系数计算系统
本系统主要用于计算特定实验仪器的粘滞系数
请按键选择是否进入系统''')
l.pack()


# 第6步，定义选项触发函数功能

def calculate_two():
    # 界面设计
    window_new2 = tk.Toplevel(window)
    window_new2.geometry('500x500')
    window_new2.title('计算粘滞系数')
    var_t = tk.StringVar()
    tk.Label(window_new2, text='t(小球下落时间s):', font=('Arial', 14)).place(x=10, y=10)
    tk.Label(window_new2, text='L(小球下落高度cm):', font=('Arial', 14)).place(x=10, y=50)
    tk.Label(window_new2, text='rho(小球密度g/cm^3):', font=('Arial', 14)).place(x=10, y=90)
    tk.Label(window_new2, text='rho1(液体密度g/cm^3):', font=('Arial', 14)).place(x=10, y=130)
    tk.Label(window_new2, text='d(小球直径mm):', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(window_new2, text='D(圆筒内直径mm):', font=('Arial', 14)).place(x=10, y=210)
    tk.Label(window_new2, text='H(液体高度cm):', font=('Arial', 14)).place(x=10, y=250)
    var_vis = tk.StringVar()
    vis = tk.Label(window_new2, textvariable=var_vis, bg='yellow', fg='red', font=('Arial', 14), width=35,
                   height=2).place(x=10, y=290)
    var_re = tk.StringVar()
    vis = tk.Label(window_new2, textvariable=var_re, bg='yellow', fg='blue', font=('Arial', 14), width=35,
                   height=2).place(x=10, y=320)

    var_t.set('xx.xx')
    entry_var_t = tk.Entry(window_new2, textvariable=var_t, font=('Arial', 14))
    entry_var_t.place(x=150, y=10)
    var_L = tk.StringVar()
    var_L.set('xx.xx')
    entry_var_L = tk.Entry(window_new2, textvariable=var_L, font=('Arial', 14))
    entry_var_L.place(x=150, y=50)
    var_rho = tk.StringVar()
    var_rho.set('xx.xx')
    entry_var_rho = tk.Entry(window_new2, textvariable=var_rho, font=('Arial', 14))
    entry_var_rho.place(x=150, y=90)
    var_rho_yeti = tk.StringVar()
    var_rho_yeti.set('xx.xx')
    entry_var_rho_yeti = tk.Entry(window_new2, textvariable=var_rho_yeti, font=('Arial', 14))
    entry_var_rho_yeti.place(x=150, y=130)
    var_d = tk.StringVar()
    var_d.set('xx.xx')
    entry_var_d = tk.Entry(window_new2, textvariable=var_d, font=('Arial', 14))
    entry_var_d.place(x=150, y=170)
    var_D = tk.StringVar()
    var_D.set('xx.xx')
    entry_var_D = tk.Entry(window_new2, textvariable=var_D, font=('Arial', 14))
    entry_var_D.place(x=150, y=210)
    var_H = tk.StringVar()
    var_H.set('xx.xx')
    entry_var_H = tk.Entry(window_new2, textvariable=var_H, font=('Arial', 14))
    entry_var_H.place(x=150, y=250)

    def calculate():
        t = var_t.get()
        L = var_L.get()
        rho = var_rho.get()
        rhoye = var_rho_yeti.get()
        d = var_d.get()
        D = var_D.get()
        H = var_H.get()
        if ((t == 'xx.xx') | (L == 'xx.xx') | (rho == 'xx.xx') | (rhoye == 'xx.xx') | (d == 'xx.xx') | (
                D == 'xx.xx') | (H == 'xx.xx')):
            tkinter.messagebox.showerror('Error', '未输入完整数据')
        else:

            t = float(t)
            L = float(L)
            rho = float(rho)
            rhoye = float(rhoye)
            d = float(d)
            D = float(D)
            H = float(H)
            calculate_vis(t, L, rho, rhoye, d, D, H)

    def calculate_vis(t, L, rho, rhoye, d, D, H):
        t = t
        L = L
        rho = rho
        rhoye = rhoye
        d = d
        D = D
        H = H
        vis_key = 0
        vis_key = (2 * (rho - rhoye) * 9.8 * (d / 2) * (d / 2) * 0.1) / (9 * (L / t))
        re_key = 0
        re_key = int(d * (L * 0.01 / t) * rhoye / (vis_key))

        if (int(vis_key) != 0):

            if ((re_key < 1) & (re_key >= 0)):
                re = d * (L * 0.01 / t) * rhoye / (vis_key)
                vis_key = str(vis_key)

                re = str(re)
                var_vis.set('粘滞系数为：' + vis_key)
                var_re.set('雷诺系数' + re)
            elif ((re_key >= 1) & (re_key <= 5)):
                re = d * (L * 0.01 / t) * rhoye / (vis_key)
                vis_xiuzheng = vis_key * (1 + (3 / 16 * re_key))
                vis_xiuzheng = str(vis_xiuzheng)
                re = str(re)
                var_vis.set('修正后的粘滞系数为：' + vis_xiuzheng)
                var_re.set('雷诺系数' + re)
            elif ((re_key >= 5) | (re_key <= 0)):
                tkinter.messagebox.showerror('请重新实验', '雷诺系数过大或者过小实验有误差')
                vis_xiuzheng = vis_key * (1 + (3 / 16 * re_key))
                vis_xiuzheng = str(vis_xiuzheng)
                re_key = str(re_key)
                var_vis.set('修正后的粘滞系数为：' + vis_xiuzheng)
                var_re.set('雷诺系数' + re_key)
            else:
                re_key = 0
                vis_key = str(vis_key)
                re_key = str(re_key)
                var_vis.set(vis_key)
                var_re.set(re_key)

        else:
            vis_key = str(vis_key)
            var_vis.set('粘滞系数' + vis_key)

    def calculate_re():
        t = var_t.get()
        L = var_L.get()
        rho = var_rho.get()
        rhoye = var_rho_yeti.get()
        d = var_d.get()
        D = var_D.get()
        H = var_H.get()
        if ((t == 'xx.xx') | (L == 'xx.xx') | (rho == 'xx.xx') | (rhoye == 'xx.xx') | (d == 'xx.xx') | (
                D == 'xx.xx') | (H == 'xx.xx')):
            tkinter.messagebox.showerror('Error', '未输入完整数据')
        else:

            t = float(t)
            L = float(L)
            rho = float(rho)
            rhoye = float(rhoye)
            d = float(d)
            D = float(D)
            H = float(H)

            vis_key = 0
            vis_key = (2 * (rho - rhoye) * 9.8 * (d / 2) * (d / 2) * 0.1) / (9 * (L / t))
            re_key = 0
            re_key = d * (L * 0.01 / t) * rhoye / (vis_key)
            var_re.set('雷诺系数' + str(re_key))



    def action():

        window_new3 = tk.Toplevel(window)
        window_new3.geometry('300x300')
        window_new3.title('提交数据')

        tem_label = ttk.Label(window_new3, text="输入温度: ")
        tem_label.grid(row=0, column=0, sticky=tk.W)

        # email label
        vis_label = ttk.Label(window_new3, text="输入粘滞系数: ")
        vis_label.grid(row=1, column=0, sticky=tk.W)

        # age label
        ye_label = ttk.Label(window_new3, text="输入液体密度 : ")
        ye_label.grid(row=2, column=0, sticky=tk.W)

        temperture_var = tk.StringVar()
        tem_entrybox = tk.Entry(window_new3, width=16, textvariable=temperture_var)
        tem_entrybox.grid(row=0, column=4)

        vis_var = tk.StringVar()
        vis_entrybox = tk.Entry(window_new3, width=16, textvariable=vis_var)
        vis_entrybox.grid(row=1, column=4)

        ye_var = tk.StringVar()
        ye_entrybox = tk.Entry(window_new3, width=16, textvariable=ye_var)
        ye_entrybox.grid(row=2, column=4)


        def baocun():

            temperture = temperture_var.get()
            rhoye = ye_var.get()
            vis = vis_var.get()

            with open('file_vis.csv', 'a') as f:
                dict_writer = DictWriter(f, fieldnames=['温度', '液体密度', '粘滞系数'])

                if os.stat('file_vis.csv').st_size == 0:
                    dict_writer.writeheader()
                else:
                    dict_writer.writerow({
                        '温度': temperture,
                        '液体密度': rhoye,
                        '粘滞系数': vis
                    })


            tkinter.messagebox.showerror('保存成功', '已经将数据写入文件')




        baocunanjian=tk.Button(window_new3,text='确认保存',font=('Arial',14),width=15,height=2,command=baocun).place(x=100,y=150)

        # 界面按键设计

    b = tk.Button(window_new2, text='开始计算粘滞系数', font=('Arial', 14), width=15, height=2, command=calculate).place(x=100,
                                                                                                                 y=400)
    c = tk.Button(window_new2, text='雷诺系数', font=('Arial', 14), width=15, height=2, command=calculate_re).place(x=100,
                                                                                                                y=430)
    submit_button = tk.Button(window_new2, text='保存数据', font=('Arial', 14), width=15, height=2, command=action).place(
        x=100, y=460)


def tuichu():
    window.quit()


# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable

r1 = tk.Radiobutton(window, text='计算粘滞系数', variable=var, value='粘滞系数', command=calculate_two)
r1.pack()
r2 = tk.Radiobutton(window, text='退出', variable=var, value='退出', command=tuichu)
r2.pack()

# 第7步，主窗口循环显示
window.mainloop()