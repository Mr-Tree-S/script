from PIL import Image

def saveall(): #把每一帧都保存下来
    im = Image.open('1.gif')
    for i in range(770):
        im.seek(i)
        im.save('123/' + str(i) +'.png') #保存到同级文件夹123 中
    ping()
    
def ping(): #把每一帧拼接起来
    new_one = Image.new('RGB',(770,432))
    for j in range(770):
        ima = Image.open('123/' + str(j) +'.png')
        new_one.paste(ima,(j,0,j+1,432))
    new_one.save("flag.png")

if __name__ ==  "__main__":
    saveall()
