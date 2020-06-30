from tkinter import *
from tkinter import font
import tkinter.messagebox
from io import BytesIO
import urllib
import urllib.request
import xml.etree.ElementTree as etree

host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

loopFlag = 1

## global
conn = None

g_Tk = tkinter.Tk()
g_Tk.title(" 11번가에서 어떤 물건을? ")
g_Tk.geometry("400x630+500+20")
g_Tk.config(bg = "white", cursor = "heart")

#======================================================================================================================#
def SearchGoods(keyword, num):
    #global ImageURL
    kwd = urllib.parse.quote(keyword)
    #kwd=hangul_utf8.replace("%","%25") #한글 검색어 변환 안되면 이걸로 시도 
    
    if num == 0:#인기도순
        url = "https://openapi.11st.co.kr/openapi/OpenApiService.tmall?key=655b0300e450d5c70b6c2a4b2c5c9891&apiCode=ProductSearch&keyword=%s&sortCd=CP&pageSize=20&pageNum=1" % kwd
    elif num == 1:#낮은가격순
        url = "https://openapi.11st.co.kr/openapi/OpenApiService.tmall?key=655b0300e450d5c70b6c2a4b2c5c9891&apiCode=ProductSearch&keyword=%s&sortCd=L&pageSize=20&pageNum=1" % kwd
    elif num == 2:#높은가격순
        url = "https://openapi.11st.co.kr/openapi/OpenApiService.tmall?key=655b0300e450d5c70b6c2a4b2c5c9891&apiCode=ProductSearch&keyword=%s&sortCd=H&pageSize=20&pageNum=1" % kwd
    elif num == 3:#후기/리뷰많은순
        url = "https://openapi.11st.co.kr/openapi/OpenApiService.tmall?key=655b0300e450d5c70b6c2a4b2c5c9891&apiCode=ProductSearch&keyword=%s&sortCd=I&pageSize=20&pageNum=1" % kwd
    else:#최근등록순
        url = "https://openapi.11st.co.kr/openapi/OpenApiService.tmall?key=655b0300e450d5c70b6c2a4b2c5c9891&apiCode=ProductSearch&keyword=%s&sortCd=N&pageSize=20&pageNum=1" % kwd

    data = urllib.request.urlopen(url).read()

    fileName = "shop.xml"
    etree.ElementTree(etree.fromstring(data.decode('EUC-KR'))).write(fileName,encoding="UTF-8",xml_declaration=True)

    # 파싱하기
    tree = etree.parse(fileName)
    root = tree.getroot()
    
    for a in root.findall('Products/Product'):
        RenderText.insert(INSERT, "제 품 명: ")
        RenderText.insert(INSERT, a.findtext('ProductName'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "가     격: ")
        RenderText.insert(INSERT, a.findtext('ProductPrice'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "배송정보: ")
        RenderText.insert(INSERT, a.findtext('Delivery'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "판 매 자: ")
        RenderText.insert(INSERT, a.findtext('SellerNick'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "리 뷰 수: ")
        RenderText.insert(INSERT, a.findtext('ReviewCount'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "만 족 도: ")
        RenderText.insert(INSERT, a.findtext('BuySatisfy'))
        RenderText.insert(INSERT, "\n\n")

#======================================================================================================================#

def lol1():
    lol1 = Label(g_Tk, text = "                                                                                                     "
                 , bg="peach puff", height = 1)
    lol1.pack()

def lol2():
    lol2 = Label(g_Tk, text = "                                                                                                     "
                 , bg="peach puff")
    lol2.pack()
    lol2.place(y=60)

def InitTopText():#제목
    TempFont = font.Font(g_Tk, size=20, weight='normal', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text = "  11번가에서 어떤 물건을? ", bg = "white", fg = "gray14")
    MainText.pack()
    MainText.place(x=20, y=22)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='normal', family = 'Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=26, selectbackground = "orange",
                       borderwidth=0.5, relief = 'solid', bg = "white")
    InputLabel.pack()
    InputLabel.place(x=25, y=100)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12,weight='normal', family='Consolas')
    SearchButton = Button(g_Tk, bd = "1", font=TempFont, relief = "flat", fg = "gray14",
                          text="검색", command=SearchButtonActionPOP, bg = "coral")
    SearchButton.pack()
    SearchButton.place(x=325, y=98)

def InitMailLabel():
    global InputMailLabel
    TempFont = font.Font(g_Tk, size=15, weight='normal', family = 'Consolas')
    InputMailLabel = Entry(g_Tk, font=TempFont, width=26, selectbackground = "orange",
                       borderwidth=0.5, relief = 'solid', bg = "white")
    InputMailLabel.pack()
    InputMailLabel.place(x=80, y=590)

def InitSearchButton1():
    TempFont = font.Font(g_Tk, size=12, weight='normal', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont,
                          text="인기",  relief = "flat", fg = "white", command=SearchButtonActionPOP, bg = "coral")
    SearchButton.pack()
    SearchButton.place(x=25, y=145)

def InitSearchButton2():
    TempFont = font.Font(g_Tk, size=12, weight='normal',family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont,
                          text="최저가", relief="flat", fg="white", command=SearchButtonActionMIN, bg="coral")
    SearchButton.pack()
    SearchButton.place(x=75, y=145)

def InitSearchButton3():
    TempFont = font.Font(g_Tk, size=12, weight='normal', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont,
                          text="최고가", relief="flat", fg="white", command=SearchButtonActionMAX, bg="coral")
    SearchButton.pack()
    SearchButton.place(x=140, y=145)

def InitSearchButton4():
    TempFont = font.Font(g_Tk, size=12, weight='normal', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont,
                          text="리뷰순", relief="flat", fg="white", command=SearchButtonActionRE, bg="coral")
    SearchButton.pack()
    SearchButton.place(x=205, y=145)

def InitSearchButton5():
    TempFont = font.Font(g_Tk, size=12, weight='normal', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont,
                          text="등록일순", relief="flat", fg="white", command=SearchButtonActionDATE, bg="coral")
    SearchButton.pack()
    SearchButton.place(x=270, y=145)

def InitMailButton():
    TempFont = font.Font(g_Tk, size=10, weight='normal', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont,
                          text="수신주소", relief="flat", fg="white",  bg="coral", command = ButtonActionMAIL)
    SearchButton.pack()
    SearchButton.place(x=20, y=590)

def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=29, borderwidth=12, relief='solid',
                      highlightcolor = "coral",
                      yscrollcommand=RenderTextScrollbar.set, bg = "white", bd = 1)
    RenderText.pack()
    RenderText.place(x=20, y=195)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

def SearchButtonActionPOP():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    SearchGoods(InputLabel.get(), 0)
    RenderText.configure(state='disabled')

def SearchButtonActionMIN():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    SearchGoods(InputLabel.get(), 1)

    RenderText.configure(state='disabled')

def SearchButtonActionMAX():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    SearchGoods(InputLabel.get(), 2)

    RenderText.configure(state='disabled')


def SearchButtonActionRE():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    SearchGoods(InputLabel.get(), 3)

    RenderText.configure(state='disabled')

def SearchButtonActionDATE():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    SearchGoods(InputLabel.get(), 4)
    RenderText.configure(state='disabled')

def sendMail(gogo):

    global host, port
    html = ""
    title = "11번가에서 어떤 물건을? 상품 검색 결과"
    senderAddr = "cimchakman@gmail.com"
    recipientAddr = gogo

    passwd = "0sikisgoodprof"

    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    text = "안녕하세용"
    part1 = MIMEText(text, _charset='UTF-8')
    msg.attach(part1)

    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

def ButtonActionMAIL():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    sendMail(InputMailLabel.get())
    RenderText.configure(state='disabled')


lol1()
lol2()
InitTopText()
InitInputLabel()
InitMailLabel()
InitMailButton()
InitSearchButton()
InitRenderText()
InitSearchButton1()
InitSearchButton2()
InitSearchButton3()
InitSearchButton4()
InitSearchButton5()

g_Tk.mainloop()