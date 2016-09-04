import pygame
import Image
import StringIO,os


f=open('word.txt','r')

words=f.readlines()[0]
f.close()

def pasteWord(words):
	os.chdir('./word')
	pygame.init()
	font_path="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
	font=pygame.font.Font(font_path,22)

	text_list=words.split(' ')
	length=len(text_list)
	for i in range(length):
		text = text_list[i].decode('utf-8','ignore')
		imgName=text_list[i]+'.png'
		if os.path.isfile(imgName):
			continue
		else:
			paste(text,font,imgName)
def paste(text,font,imgName,area=(5,3)):
	im=Image.new('RGB',(30,30),(255,255,255))
	rtext=font.render(text,True,(0,0,0),(255,255,255))

	sio=StringIO.StringIO()
	pygame.image.save(rtext,sio)
	sio.seek(0)
	line=Image.open(sio)
	im.paste(line,area)
	im.save(imgName)

if __name__ == '__main__':
	pasteWord(words)

