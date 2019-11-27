import ipinfo
from tkinter import *
from bs4 import BeautifulSoup
import getpass
import socket
import urllib.request

def infoip():#API ipinfo
    try:
        access_token = '6da13029b22db7'
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails()
        x = details.all
        for k,v in x.items():
            print("[*]",k,":",v)
        print("[*] ")
    except :
        print('[*] COMPRUEBE SU CONEXION A INTERNER')
    finally:
        pass

def web():#web scraping (solo link)
    try:
        x = input('[¡] INTRODUSCA UN SOLO LINK :')
        urllib.request.urlopen(x).read().decode()
    except ValueError:
        print('[*] Error de Link')
    except urllib.error.HTTPError:
        print('[*] Error 403 la Extraccion es Prohibida')
        print("[*]_INTENTE CON OTRO LINK_")
    finally:
        pass

def web_etiqueta():#web scraping (con etiqueta)
    try:
        print('\n\t OBTENCION DE DATOS CON LA ETIQUETA: <a href="ejemplo">')
        y = input('[¡] INTRODUSCA UN SOLO LINK :')
        my_data = urllib.request.urlopen(y).read().decode()
        sopa = BeautifulSoup(my_data)
        tags = sopa('a')
        for tag in tags:
            print(tag.get('href'))
        print(my_data)
    except ValueError:
        print('[*] Error de Link')
    except urllib.error.HTTPError:
        print('[*] Error 403 la Extraccion es Prohibida')
        print("[*]_INTENTE CON OTRO LINK_")
    finally:
        print('[*] OBTENCION EXITOSA')
        
def web_scraping():#menu web scraping
    root = Toplevel()
    root.geometry('180x230')
    root.configure(bg='yellow')
    root.configure(cursor='X_cursor')
    root.iconbitmap('bomb.ico')
    root.title('WEBSPG')
    root.resizable(False,False)
    Button(root,text='Web-Scraping',command=web,bg='#ECF15C',bd=8).pack(fill=X)
    Button(root,text='Web Scraping tags<a>',command=web,bg='#ECF15C',bd=8).pack(fill=X)
    Button(root,text='salir',command=lambda root=root:quit(root),bg='red',bd=8).pack(fill=X)
    img1 = PhotoImage(file='webscraping.png')
    Label(root,image=img1).pack()
    root.mainloop()


    
#MASTER()
#activeforeground = color del texto.
#bd = creacion de bordes
#cursosr = imagen del cursor
#relief="sunken" = boton undido
#relief="raised" = boton saliente
#relief="groove" = boton undido/saliente
root = Tk()
cadena = StringVar()
root.geometry('446x260')
root.iconbitmap('deth.ico')
root.configure(bg='black')
root.configure(cursor='X_cursor')
root.title('MULTI-SHIT')
root.resizable(False,False)
Button(root,text='IPINFO',command=infoip,activeforeground="green",bg='green',bd=6,relief="groove").pack(fill=X)
Button(root,text='Web-Scraping',command=web_scraping,bg='green',activeforeground="green",bd=6,relief="groove").pack(fill=X)
Button(root,text='Salir',command=lambda root=root:quit(root),bg='red',activeforeground="red",bd=6,relief="groove").pack(fill=X)
img0 = PhotoImage(file='nbj.png')
Label(root,image=img0).pack(padx=80,pady=20)
root.mainloop()

