import os
import requests

def main():
    print("Input valid absolute path where you want to save convocation photos")
    abs_path=input().strip()
    download(abs_path)
    
def download(abs_path=os.path.dirname(os.path.abspath(__file__))):
    if os.path.exists(abs_path):
        path=abs_path+'\Convocation2017Pics'
        os.makedirs(path)
    else:
        path=abs_path=os.path.dirname(os.path.abspath(__file__))+'\Convocation2017Pics'
        os.makedirs(path)
        print(path)
    base_url='http://www.csre.iitb.ac.in/~alok/Convocation2017/DSC_6'
    
    for i in range(307,484):
        filename='DSC_6'+str(i)+'.JPG'
        urlfilename = base_url+str(i)+'.JPG'
        exist = exists(urlfilename)
        if(exist):
            full_path=path+'\\'+filename
            f=open(full_path,'wb')
            f.write(requests.get(base_url+str(i)+'.JPG').content)
            f.close()
        else:
            pass
        
        print(base_url+str(i)+'.JPG')
        
def exists(path):
    ret = requests.head(path)
    if(ret.status_code == 200):
        print('file exists at the index')
        return True
    else:
        print('file does not exists at the index ')
        return False

if __name__=="__main__":
    main()

