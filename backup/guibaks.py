from tkinter import *
from tkinter.ttk import *
import socket
import struct


def start(host,port):
	pass

class MyFrame(Frame):
	"""docstring for ClassName"""
	def __init__(self, root):
		super().__init__(root)
		self.root=root
		self.grid()
		self.local_ip='127.0.0.1'
		self.server_ports=[10888,20888,30888]
		self.init_components()

	def init_components(self):
		proj_name=Label(self,text='远程备份服务器')
		proj_name.grid(columnspan=2)

		server_ip_label=Label(self,text='服务地址')
		server_ip_label.grid(row=1)

		self.server_ip=Combobox(self,values=self.get_ipaddr())
		self.server_ip.set(self.local_ip)
		self.server_ip.grid(row=1,column=1)

		server_ports_label=Label(self,text='服务端口')
		server_ports_label.grid(row=2)


		self.server_port=Combobox(self,values=self.server_ports)
		self.server_port.set(self.server_ports[0])
		self.server_port.grid(row=2,column=1)

		self.start_server_btn=Button(self,text='启动服务',command=self.start_server)
		self.start_server_btn.grid(row=3)

		self.start_exit_btn=Button(self,text='退出服务',command=self.root.destroy)
		self.start_exit_btn.grid(row=3,column=1)

	def get_ipaddr(self):
		host_name=socket.gethostname()
		info=socket.gethostbyname_ex(host_name)
		info=info[2]
		info.append(self.local_ip)
		return info

	def start_server(self):
		print(self.server_ip.get(),self.server_port.get())
		start(self.server_ip.get(),self.server_port.get())

if __name__ == '__main__':
	root=Tk()
	root.title('备份服务器')
	root.resizable(False,False)
	app=MyFrame(root)
	app.mainloop()