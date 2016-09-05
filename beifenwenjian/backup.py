import tkinter
import os
import time

def backup():
    global entry_source
    global entry_target
    source =entry_source.get()
    target_dir =entry_target.get()

    today_dir = target_dir +time.strftime('%Y%m%d')
    time_dir =time.strftime("%H%M%S")

    touch =today_dir + os.sep +time_dir +'.zip'
    cmd_touch ="zip -qr " +touch+ ' '+source

    print (cmd_touch)
    print (source)
    print (target_dir)
    if os.path.exists(today_dir)==0:
        os.mkdir(today_dir)
        print(today_dir)
    if os.system(cmd_touch)==0:
        print('Succes backup')
    else:
        print ('Failed backup')


root=tkinter.Tk()
root.title('Back up')
root.geometry("200x200")

lb1_source =tkinter.Label(root ,text='Source')
lb1_source.grid(row=0,column=0)
entry_source =tkinter.Entry(root)
entry_source.grid(row=0,column=1)

lb1_target =tkinter.Label(root ,text='Target')
lb1_target.grid(row=1,column=0)
entry_target =tkinter.Entry(root)
entry_target.grid(row=1,column=1)

but_back=tkinter.Button(root,text="BackUp")
but_back.grid(row=3,column=0)
but_back["command"]=backup

root.mainloop()



