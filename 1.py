import requests as req
import json,sys,time
#先注册azure应用,确保应用有以下权限:
#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用

###################################################################
#在下方单引号内填入应用id                                         #
id=r'2157c0ae-6576-48c8-b2b7-7a7b3c469b0f'                         
#在下方单引号内填入应用秘钥                                       #
secret=r'lm4OwDRv[vK0[/5wPtB.18sFSZiT6zQj'                        
###################################################################

num1 = 0
refresh_token = 'OAQABAAAAAABeAFzDwllzTYGDLh_qYbH83fvnsI-ORHE_iZ0edRocSTR3QyrgRg_H0dqgxVlr3Rq2XtYnA5wNLVgvUzwAlI4UZjDI9Yg4oo4jaaFq-1W5DFe0xh-wOD49LQ1D0bbk2iihaGyZFTldsP4WYq4EBBYPnjSK9_CMTR8w-XiE-g76_Ewt1UgOiSE4crr8wM8OSv0oEA2BTk0HDeuzR7Uthw5hhi7BVQhVquYvRPIYxPtUGyqPtyYA_r5YCC8FH1F02j6sO34IGLP9kyPmwW2utf3RA22PCtS7o2Z4eq_7oqHIptrm8poIs3_xDtZq2kjc81rcNDIHsf2b5-y7eV-CiIeIqVjUl1iBjxHpGntH-cB5hIEkn5VtLICsxhXbDxBNAYb15VMq1sei3RMYrocX3z6LsXvuMwpKdP_Yt_TFE105A-wnPkOIKpKKp80TQzLW4R3pOLJnDbqJbj5r5hgt_J5TlfYsKf8A_ffcN7q_IVdRPO5APMdzyyTXMFnhaS3tRlOsCcosFQ8czrjP1kqxm0dsx9E53qIRkLj1BIl7PUKW8I8o9Oo_90K--RZnMgKDjkfuBSCO3DEwt6tMiqaIytWyi6fRjT8YQVPdcNv7ufQY6LdtfnIDVWXcs7U7JmF1a9NvuwAvuuGtP6MJkjHaY9g38Bntr5KVD7VP5hQbdEmIHVxtvg04oi6ZSLvs2sPMkzUTz1eUduxyw1P19NQVJX6DTg2lp_B87j01X-YKke4reAXTK-jkGzhd81UMM77TMEOJYWn5f_V2cfLV6Nmfepqfu5-rny9-EX8mg9NfavQTmvx2K63C0vCp0Rv6N-C_ecYgAA'
# print(refresh_token)
def gettoken(refresh_token):
    headers={'Content-Type':'application/x-www-form-urlencoded'
            }
    data={'grant_type': 'refresh_token',
          'refresh_token': refresh_token,
          'client_id':id,
          'client_secret':secret,
          'redirect_uri':'http://localhost:53682/'
         }
    html = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token',data=data,headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    with open(path, 'w+') as f:
        f.write(refresh_token)
    return access_token
def main():
    global num1
    access_token=gettoken(refresh_token)
    headers={
    'Authorization':access_token,
    'Content-Type':'application/json'
    }
    try:
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root',headers=headers).status_code == 200:
            num1+=1
            print("1调用成功"+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive',headers=headers).status_code == 200:
            num1+=1
            print("2调用成功"+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/drive/root: ',headers=headers).status_code == 200:
            num1+=1
            print('3调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/users ',headers=headers).status_code == 200:
            num1+=1
            print('4调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/messages',headers=headers).status_code == 200:
            num1+=1
            print('5调用成功'+str(num1)+'次')    
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',headers=headers).status_code == 200:
            num1+=1
            print('6调用成功'+str(num1)+'次')    
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',headers=headers).status_code == 200:
            num1+=1
            print('7调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children',headers=headers).status_code == 200:
            num1+=1
            print('8调用成功'+str(num1)+'次')
        if req.get(r'https://api.powerbi.com/v1.0/myorg/apps',headers=headers).status_code == 200:
            num1+=1
            print('8调用成功'+str(num1)+'次') 
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders',headers=headers).status_code == 200:
            num1+=1
            print('9调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories',headers=headers).status_code == 200:
            num1+=1
            print('10调用成功'+str(num1)+'次')
    except:
        print("pass")
        pass
 main()
