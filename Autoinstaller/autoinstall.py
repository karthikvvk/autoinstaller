"""
>The way this project work is by accessing the application's direct download link to download them.

>But many websites use section cookies which requires visiting or clicking the download button.

>Thus, for those kind of websites this project can only take you to the download page and the user needs to manually
download the application.

>Despite this disadvantage this project have features:
    * GUI
    * Adding and removing application list
    * Make your initial windows setup lot easier
    * Can run any executables which is saved in the directory this program is downloaded
    * Can also be used to open set of websites when logining into your PC.
**NOTE THIS PROJECT ONLY WORKS IN 64 BIT
"""
import string
import subprocess
from tkinter import ttk
import threading
import time
import getpass
from tkinter import *
import os
import webbrowser
import oopen.openeasy as op

os.system('pip install pyinstaller')
os.system('pip install requests')
import requests

theme = '#1e1e1e'
f_theme = 'white'
user = getpass.getuser()
windisk = ''
apps = []

disks = []
for i in string.ascii_uppercase:
    if os.path.exists(f'{i}:\\'):
        disks.append(i)
for t in disks:
    if os.path.exists(f'{t}:\\Users'):
        windisk = t


root = Tk()
root.configure(bg=theme)
root.geometry(f'{root.winfo_screenwidth() - 500}x{root.winfo_screenheight() - 300}')
root.title('Auto installer')


def mysql():
    request_sql = str(
        requests.get(url='https://dev.mysql.com/downloads/installer/', allow_redirects=True).content).split(
        ' ')
    lis_sql = []
    for t in request_sql:
        if 'href' in t and 'https' not in t:
            lis_sql.append(t)
    req = []
    for i in lis_sql:
        if '/downloads/file/?id=' in i:
            req.append(i)
    last = str(requests.get(url='https://dev.mysql.com/' + req[-1].split('"')[1], allow_redirects=True).content).split(
        ' ')
    for g in last:
        if '.msi' in g and 'href' in g and 'https' not in g:
            fh = open('mysql.exe', 'wb')
            fh.write(requests.get(url='https://dev.mysql.com/' + g.split('"')[1], allow_redirects=True).content)
            fh.close()


def vm(base_url, app):
    request_sql = str(
        requests.get(url=base_url, allow_redirects=True).content).split(' ')
    s = 0
    l = 0
    m = 0
    for t in request_sql:
        if 'href' in t:
            try:
                mv = int(t.split('"')[1][0])
                if mv > s:
                    s = mv
            except:
                continue
    for t in request_sql:
        if 'href' in t:
            if t.split('"')[1].startswith(f'{s}'):
                try:
                    sv = int(t.split('"')[1].split(".")[-1].rstrip("/"))

                    if sv > l:
                        l = sv
                except:
                    continue

    for t in request_sql:
        if 'href' in t:
            if t.split('"')[1].startswith(f'{s}') and t.split('"')[1].endswith(f'{l}'):
                try:
                    sv = int(t.split('"')[1].split(".")[-2])

                    if sv > m:
                        m = sv
                except:
                    continue
    urls = f'{base_url}/{s}.{m}.{l}/'
    request_sql = str(requests.get(url=urls, allow_redirects=True).content).split(' ')
    for t in request_sql:
        if (f'VirtualBox-{s}.{m}.{l}' in t and '.exe' in t) and 'href' in t:
            open(f'{app}.exe', 'wb').write(requests.get(url=urls + t.split('"')[1], allow_redirects=True).content)
        if (f'Oracle_VM_VirtualBox_Extension_Pack-{s}.{m}.{l}.vbox-extpack' in t) and 'href' in t:
            fh = open(f'Oracle_VM_VirtualBox_Extension_Pack-{s}.{m}.{l}.vbox-extpack', 'wb')
            fh.write(requests.get(url=urls + t.split('"')[1], allow_redirects=True).content)
            fh.close()


def ext_download(base_url, app):
    ct = str(requests.get(url=base_url, allow_redirects=True).content).split(' ')
    lis_py = []
    for k in ct:
        if 'https' in str(k) and 'href' in str(k) and 'exe' in str(k):
            lis_py.append(k)
    for b in lis_py:
        if '64' in b:
            fh = open(f'{app}.exe', 'wb')
            fh.write(requests.get(url=b.split('"')[1], allow_redirects=True).content)
            fh.flush()
            fh.close()


def afters():
    global root
    root.destroy()
    vikings = Tk()
    vikings.configure(bg=theme)
    vikings.geometry('530x200')
    vikings.title('Auto installer')
    Label(vikings,
          text='Auto installer starts to download the selected applications and install the in background after 40sec\n\n'
               'Make sure the system is plugged in and have internet access.\n\n'
               'If any specific application or package or any kind of executables needs to be run\n'
               f'   can be added to this directory by clicking "Add": \n"{os.getcwd()}"', bg=theme, fg=f_theme, justify=LEFT).grid()

    def disable_event():
        pass

    def des():
        time.sleep(40)
        vikings.destroy()

    def add():
        subprocess.run(['explorer', os.getcwd()])
    vikings.protocol("WM_DELETE_WINDOW", disable_event)
    threading.Thread(target=des).start()
    ttk.Button(vikings, text='Add', command=add).grid()
    vikings.mainloop()


def main():
    global root, user
    lst = []

    if os.path.exists('install.txt'):
        pass
    else:
        os.abort()

    fh = open('install.txt')
    re = fh.readlines()
    for i in re:
        sp = i.split(',')
        try:
            sp[1] = sp[1].rstrip('\n')
        except:
            continue
        if not sp[0].startswith("#"):
            lst.append(sp)
    vari = []
    for i in range(len(lst)):
        vari.append('a' + str(i))
        vari[i] = IntVar(root, value=0)

    for i in range(len(lst)):
        Checkbutton(root, variable=vari[i], bg=theme, justify='left').grid(row=i + 1, column=0)
    val = []
    for i in range(len(lst)):
        Label(root, text=lst[i][0], bg=theme, fg=f_theme, justify='left').grid(row=i + 1, column=1)

    def download_selected():
        for ind in range(len(lst)):
            x = vari[ind].get()
            val.append(x)
        if 1 in val:
            afters()
            for k in range(len(val)):
                if val[k]:
                    apps.append(lst[k][0].lower())
                    if 'mysql' in lst[k][0].lower():
                        mysql()
                    elif 'python' in lst[k][0].lower():
                        ext_download(lst[k][1], 'python')
                    elif 'sublime' in lst[k][0].lower():
                        ext_download(lst[k][1], 'sublime')
                    elif 'vm' in lst[k][0].lower():
                        vm(lst[k][1], 'vm')
                    else:
                        fh = open(lst[k][0] + '.exe', 'wb')
                        fh.write(requests.get(url=lst[k][1], allow_redirects=True).content)
                        fh.close()
            root.destroy()
        else:
            pass

    def download_all():
        afters()
        for j in range(len(lst)):
            apps.append(lst[j][0].lower())
            if 'mysql' in lst[j][0].lower():
                mysql()
            elif 'python' in lst[j][0].lower():
                ext_download(lst[j][1], 'python')
            elif 'sublime' in lst[j][0].lower():
                ext_download(lst[j][1], 'sublime')
            elif 'vm' in lst[j][0].lower():
                vm(lst[j][1], 'vm')
            else:
                try:
                    fh = open(lst[j][0] + '.exe', 'wb')
                    fh.write(requests.get(url=lst[j][1], allow_redirects=True).content)
                    fh.close()
                except:
                    continue
        root.destroy()

    def add_app():
        root.destroy()
        tk = Tk()
        tk.configure(bg=theme)
        tk.geometry('500x100')
        tk.title('Auto installer add an app')
        lnk = StringVar(tk, value='')

        def submit():
            link = lnk.get()
            op.o_append('install.txt', link, newline=True)
            lst.append([link])
            try:
                tk.destroy()
            except:
                pass
            main()

        e = Entry(tk, textvariable=lnk, width=50)
        e.grid(row=0, column=1)
        e.focus_set()
        Label(tk, text='enter the name, link:', bg=theme, fg=f_theme).grid(row=0, column=0)
        Button(tk, text='add', command=submit).grid(row=1, column=0)
        tk.mainloop()

    def remove_app():
        for ind in range(len(lst)):
            x = vari[ind].get()
            val.append(x)
        for k in range(len(val)):
            if val[k]:
                f = open('install.txt').read()
                rep = f.replace(lst[k][0] + ',' + lst[k][1], "#" + lst[k][0] + ',' + lst[k][1])
                ff = open('install.txt', 'w')
                ff.write(rep)
                ff.close()
        for k in range(len(val)):
            if val[k]:
                lst.remove(lst[k])
        root.destroy()
        main()

    add_b = ttk.Button(root, text='Add app', command=add_app)
    add_b.grid(row=0, column=5)
    remove_b = ttk.Button(root, text='Remove app', command=remove_app)
    remove_b.grid(row=0, column=2)
    install_b = ttk.Button(root, text='Install', command=download_selected)
    install_b.grid(row=0, column=3)
    install_all_b = ttk.Button(root, text='Install all', command=download_all)
    install_all_b.grid(row=0, column=4)
    root.mainloop()

    lis = [
        'https://apps.microsoft.com/store/detail/adobe-acrobat-reader-dc/XPDP273C0XHQH2?hl=en-in&gl=in&icid=CNavAppsWindowsApps',
        'https://apps.microsoft.com/store/detail/whatsapp/9NKSQGP7F2NH?hl=en-in&gl=in&icid=CNavAppsWindowsApps',
        'https://www.google.com/chrome/',
        'https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC']
    web_apps = ['adobe', 'whatsapp', 'chrome', 'pycharm']

    cn = 0
    for i in web_apps:
        if i in apps:
            webbrowser.open_new_tab(url=lis[cn])
        cn += 1

    lis_files = os.listdir()
    try:
        lis_files.remove('autoinstall.exe')
    except:
        pass
    for i in lis_files:
        if not i.endswith(".py") and not i.endswith(".txt") and "." in i:
            try:
                os.startfile(i)
            except:
                pass

    if os.path.exists(f'{windisk}:\\Users\\{user}\\autoinstaller'):
        pass
    else:
        os.mkdir(f'{windisk}:\\Users\\{user}\\autoinstaller')
    os.chdir('docopy')
    pd = os.getcwd()
    for i in os.listdir():
        os.chdir(f'{windisk}:\\Users\\{user}\\autoinstaller')
        os.mkdir(i)
        os.chdir(pd)
        os.system(f'xcopy {i} {windisk}:\\Users\\{user}\\autoinstaller\\{i} /E /I')
    subprocess.run(['explorer', f'{windisk}:\\Users\\{user}\\autoinstaller'])
    os.abort()


main()
