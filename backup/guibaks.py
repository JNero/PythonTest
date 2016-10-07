from tkinter import *
from tkinter.ttk import *
import socket
import struct
import os
import pickle

BAK_PATH=r'/home/qiao/桌面/bak'

def recv_unit_data(clnt,infos_len):
	data=b''
	if 0<infos_len<=1024:
		data+=clnt.recv(infos_len)
	else:
		while True:
			if infos_len>1024:
				data+=clnt.recv(1024)
				infos_len-=1024
			else:
				data+=clnt.recv(infos_len)
				break
	return data

def get_files_info(clnt):
	fmt_str='Q'
	headsize=struct.calcsize(fmt_str)
	data=clnt.recv(headsize)
	infos_len=struct.unpack(fmt_str,data)
	data=recv_unit_data(clnt,infos_len)
	return pickle.load(data)

def mk_path():
	paths=filepath.split(os.path.seq)[:-1]
	p=BAK_PATH
	for path in paths:
		p=os.path.join(p,path)
		if not os.path.exists(p):
			os.mkdir

def recv_file(clnt,infos_len,filepath):
	mk_path(filepath)
	filepath=os.path.join(BAK_PATH,filepath)
	f=open(filepath,'wb+')
	try:
		if 0<infos_len<=1024:
			data=clnt.recv(infos_len)
			f.write(data)
		else:
			while True:
				if infos_len>1024:
					data=clnt.recv(1024)
					f.write(data)
					infos_len-=1024
				else:
					data =clnt.recv(1024)
					f.write(data)
					break
	except:
		peint('error')
	else:
		return True
	finally:
		f.close()


def start(host,port):
	if not os.path.exists(BAK_PATH):
		os.mkdir(BAK_PATH)
	st=socket.socket()
	st.bind((host,port))
	st.listen(1)
	client,addr=st.accept()
	files_lst=get_files_info(client)
	for size,filepath in files_lst:
		res=recv_file(client,size,filepath)
		send_echo(client,res)

	client.close()
	st.close()

def send_echo(clnt,res):
	if res:
		clnt.sendall(b'success')
	else:
		clnt.sendall(b'failure')


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
		start(self.server_ip.get(),int(self.server_port.get()))

if __name__ == '__main__':
	root=Tk()
	root.title('备份服务器')
	root.resizable(False,False)
	app=MyFrame(root)
	app.mainloop()