import base64
with open("icon.py","w") as f:
  f.write('class Icon(object):\n')
  f.write('\tdef __init__(self):\n')
  f.write("\t\tself.img='")
with open(r"D:\OneDrive\MyCode\Python\根据cnl文件更改dat数据的客户名\line1.ico","rb") as i:
  b64str = base64.b64encode(i.read())
  with open("icon.py","ab+") as f:
    f.write(b64str)
with open("icon.py","a") as f:
  f.write("'")
