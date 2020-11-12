import os

template="![alt text](https://raw.githubusercontent.com/lefevrej/icons/main/icons/"
readme_file="README.md"

res=""
for img_name in os.listdir("icons"):
    res=res+template+img_name+") "

#read lines of readme
f=open(readme_file, 'r')
lines=f.readlines()
lines[-1]=res
f.close()

#replace last line
f=open(readme_file, 'w')
f.writelines(lines)
f.close()
