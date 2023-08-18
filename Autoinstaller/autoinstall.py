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
from tkinter import ttk
import threading
import getpass
from tkinter import *
import os
import webbrowser
import winreg as wrg
import elevate
import urllib.request

elevate.elevate(show_console=False)

root_dir = os.getcwd()
req_mods = {"checkboxx": "automate_checkbox", "oopen": "openeasy"}
req_mods_lnk = {
    "checkboxx": "https://github.com/karthikvvk/make-life-easy-python-packages-auto-checkbox-tkinter/blob/main/make-life-easy-python-packages-auto-checkbox-tkinter/automate_checkbox.py",
    "oopen": "https://github.com/karthikvvk/make-life-easy-python-packages-oopen/blob/main/make-life-easy-python-packages-oopen/openeasy.py"}
for hi in req_mods:
    if os.path.exists(hi):
        pass
    else:
        os.mkdir(hi)
    open(f"{root_dir}\\{hi}\\__init__.py", 'w').close()
    urllib.request.urlretrieve(req_mods_lnk[hi], f"{root_dir}\\{hi}\\{req_mods[hi]}.py")
import checkboxx.automate_checkbox as auch
import oopen.openeasy as op

try:
    os.system('python.exe -m pip install --upgrade pip > NUL')
except:
    pass
os.system('pip install requests > NUL')
import requests

user = getpass.getuser()
theme = '#f0f0f0'
f_theme = 'black'
windisk = ''
disks = []
cpy = False
inst = False
root_dir = os.getcwd()

for i in string.ascii_uppercase:
    if os.path.exists(f'{i}:\\'):
        disks.append(i)
for t in disks:
    if os.path.exists(f'{t}:\\Users'):
        windisk = t


def settings():
    global user
    groot = Tk()
    groot.geometry(f'{groot.winfo_screenwidth() - 500}x{groot.winfo_screenheight() - 300}+100+100')
    groot.title('Auto installer')

    liss = [[], [], [], [], []]

    if os.path.exists('settings.txt'):
        pass
    else:
        os.abort()

    fhh = open('settings.txt')
    ree = fhh.readlines()
    for iglu in ree:
        s = iglu.split(',')
        liss[0].append(s[0])
        liss[1].append(s[1])
        liss[2].append(s[2])
        liss[3].append(s[3])
        liss[4].append(s[4].rstrip("\n"))
    Label(groot, text='Name', bg=theme, fg=f_theme).grid(row=0, column=0)
    regchbx = auch.cr_checkbox(groot, liss[0], bg=theme, fg=f_theme, row_lb=1, column_lb=0)

    def change():
        def regs(hky, key_name='', path=r"", dest_folder="", value=0):
            if hky == "HKEY_CURRENT_USER":
                loc = wrg.HKEY_CURRENT_USER
            elif hky == "HKEY_CLASSES_ROOT":
                loc = wrg.HKEY_CLASSES_ROOT
            elif hky == "HKEY_LOCAL_MACHINE":
                loc = wrg.HKEY_LOCAL_MACHINE
            elif hky == "HKEY_USERS":
                loc = wrg.HKEY_USERS
            elif hky == "HKEY_CURRENT_CONFIG":
                loc = wrg.HKEY_CURRENT_CONFIG
            soft = wrg.OpenKeyEx(loc, path)
            key = wrg.CreateKey(soft, dest_folder)
            wrg.SetValueEx(key, key_name, 0, wrg.REG_DWORD, value)
            if key:
                wrg.CloseKey(key)

        for j in liss[0]:
            au = auch.fetch_cked_val(regchbx[0])
            if j in au:
                valu = 1
            else:
                valu = 0
            ind = liss[0].index(j)
            regs(hky=liss[2][ind], key_name=liss[1][ind], value=valu, path=liss[3][ind], dest_folder=liss[4][ind])

        groot.destroy()
        os.system('taskkill /IM explorer.exe /F')
        os.system('start explorer.exe')

    def add_setting():
        groot.destroy()
        tk = Tk()
        tk.geometry('800x300+100+100')
        tk.title('Auto installer add a setting')
        nam = StringVar(tk, value='')
        nam_sh = StringVar(tk, value='')
        pat = StringVar(tk, value='')
        fold = StringVar(tk, value='')
        hkey = StringVar(tk, value='')

        def submit():
            hkey_name = hkey.get().upper()
            folder = fold.get()
            path = pat.get()
            name = nam.get()
            show_name = nam_sh.get()

            op.o_append('settings.txt', f'{show_name},{name},{hkey_name},{path},{folder}', newline=True)
            tk.destroy()
            settings()

        Entry(tk, textvariable=nam_sh, width=50).grid(row=0, column=1)
        Entry(tk, textvariable=nam, width=50).grid(row=1, column=1)
        Entry(tk, textvariable=pat, width=50).grid(row=2, column=1)
        Entry(tk, textvariable=fold, width=50).grid(row=3, column=1)
        Entry(tk, textvariable=hkey, width=50).grid(row=4, column=1)

        Label(tk, text='enter the name to be displayed:').grid(row=0, column=0)
        Label(tk, text='enter the name of registry:').grid(row=1, column=0)
        Label(tk, text='enter the HKEY name:').grid(row=4, column=0)
        Label(tk, text='enter the name of the folder of the registry:').grid(row=3, column=0)
        Label(tk, text='enter the full path except the destination folder:').grid(row=2, column=0)
        ttk.Button(tk, text='add', command=submit).grid(row=5, column=2)
        tk.mainloop()

    add_b = ttk.Button(groot, text='Add a setting', command=add_setting)
    add_b.grid(row=0, column=4)
    install_b = ttk.Button(groot, text='change', command=change)
    install_b.grid(row=0, column=3)
    skip_b = ttk.Button(groot, text='skip', command=groot.destroy)
    skip_b.grid(row=0, column=5)
    groot.mainloop()


settings()


val = []


def application():
    global user

    root = Tk()
    root.geometry(f'{root.winfo_screenwidth() - 500}x{root.winfo_screenheight() - 300}+100+100')
    root.title('Auto installer')

    lst = []
    d_lst = dict([])

    if os.path.exists('install.txt'):
        pass
    else:
        os.abort()

    fh = open('install.txt')
    re = fh.readlines()
    for ii in re:
        try:
            sp = ii.split(',')
            sp[1] = sp[1].rstrip('\n').strip()
            sp[0] = sp[0].strip()
        except:
            continue
        if not sp[0].startswith("#"):
            lst.append(sp[0])
            d_lst[sp[0]] = sp[1]

    dwnbx = auch.cr_checkbox(root, lst, bg=theme, fg=f_theme)

    def mysql(base_url, app):
        request_sql = str(
            requests.get(url=base_url, allow_redirects=True).content).split(
            ' ')
        req = []
        for iii in request_sql:
            if ('href' in iii or 'https' in iii) and '/downloads/file/?id=' in iii:
                req.append(iii)
        last = str(
            requests.get(url='https://dev.mysql.com/' + req[-1].split('"')[1], allow_redirects=True).content).split(
            ' ')
        for g in last:
            if '.msi' in g and 'href' in g and 'https' not in g:
                fhf = open(f'{windisk}:\\Users\\{user}\\Downloads\\{app}.msi', 'wb')
                fhf.write(requests.get(url='https://dev.mysql.com/' + g.split('"')[1], allow_redirects=True).content)
                fhf.close()

    def vm(base_url, app):
        request_sql = str(
            requests.get(url=base_url, allow_redirects=True).content).split(' ')
        s = 0
        ll = 0
        m = 0
        for ty in request_sql:
            if 'href' in ty:
                try:
                    mv = int(ty.split('"')[1][0])
                    if mv > s:
                        s = mv
                except:
                    continue
        for ti in request_sql:
            if 'href' in ti:
                if ti.split('"')[1].startswith(f'{s}'):
                    try:
                        sv = int(ti.split('"')[1].split(".")[-1].rstrip("/"))

                        if sv > ll:
                            ll = sv
                    except:
                        continue

        for ti in request_sql:
            if 'href' in ti:
                if ti.split('"')[1].startswith(f'{s}') and ti.split('"')[1].endswith(f'{ll}'):
                    try:
                        sv = int(ti.split('"')[1].split(".")[-2])

                        if sv > m:
                            m = sv
                    except:
                        continue
        urls = f'{base_url}/{s}.{m}.{ll}/'
        request_sql = str(requests.get(url=urls, allow_redirects=True).content).split(' ')
        for ti in request_sql:
            if (f'VirtualBox-{s}.{m}.{ll}' in ti and '.exe' in ti) and 'href' in ti:
                open(f'{windisk}:\\Users\\{user}\\Downloads\\{app}.exe', 'wb').write(requests.get(url=urls + ti.split('"')[1], allow_redirects=True).content)
            if (f'Oracle_VM_VirtualBox_Extension_Pack-{s}.{m}.{ll}.vbox-extpack' in ti) and 'href' in ti:
                fhg = open(
                    f'{windisk}:\\Users\\{user}\\Downloads\\Oracle_VM_VirtualBox_Extension_Pack-{s}.{m}.{ll}.vbox-extpack',
                    'wb')
                fhg.write(requests.get(url=urls + ti.split('"')[1], allow_redirects=True).content)
                fhg.close()

    def ext_download(base_url, app):
        ct = str(requests.get(url=base_url, allow_redirects=True).content).split(' ')
        lis_py = []
        for k in ct:
            if 'https' in str(k) and 'href' in str(k) and 'exe' in str(k):
                lis_py.append(k)
        for b in lis_py:
            if '64' in b:
                def res():
                    fhp = open(f'{windisk}:\\Users\\{user}\\Downloads\\{app}.exe', 'wb')
                    fhp.write(requests.get(url=b.split('"')[1], allow_redirects=True).content)
                    fhp.flush()
                    fhp.close()

                th = threading.Thread(target=res)
                th.start()
                th.join()

    def start_down():
        global val, root_dir, inst
        os.chdir(root_dir)
        for j in val:
            if d_lst[j] == "link":
                pass
            else:
                if 'mysql' in j:
                    mysql(d_lst[j], j)
                elif 'python' in j:
                    ext_download(d_lst[j], j)
                elif 'sublime' in j:
                    ext_download(d_lst[j], j)
                elif 'vm' in j:
                    vm(d_lst[j], j)
                else:
                    def rss():
                        fhd = open(f'{windisk}:\\Users\\{user}\\Downloads\\{j}.exe', 'wb')
                        fhd.write(requests.get(url=d_lst[j], allow_redirects=True).content)
                        fhd.close()

                    thar = threading.Thread(target=rss)
                    thar.start()
                    thar.join()
        os.chdir(root_dir)
        fhr = open('webpages.txt')
        lis = fhr.readlines()
        for y in lis:
            lin = y.split(",")
            if lin[0] in val:

                webbrowser.open(url=lin[1].rstrip("\n"), new=2)

        lis_files = os.listdir(f"{windisk}:\\Users\\{user}\\Downloads\\")
        try:
            lis_files.remove('autoinstall.exe')
        except:
            pass
        for idb in lis_files:
            if not idb.endswith(".py") and not idb.endswith(".txt") and "." in idb:
                try:
                    os.startfile(f"{windisk}:\\Users\\{user}\\Downloads\\{idb}")
                except:
                    pass
        inst = True

    def download_selected():
        global val
        val = auch.fetch_cked_val(dwnbx[0])
        root.destroy()
        threading.Thread(target=start_down).start()

    def download_all():
        global val
        val = lst
        root.destroy()
        threading.Thread(target=start_down).start()

    def add_app():
        root.destroy()
        tk = Tk()
        tk.geometry('800x300+200+100')
        tk.title('Auto installer add an app')
        nam = StringVar(tk, value='')
        lnk = StringVar(tk, value='')

        def submit():
            link = lnk.get()
            name = nam.get()
            if len(link) > 0 and len(name) > 0:
                op.o_append('install.txt', name + "," + link, newline=True)
                lst.append(name)
                try:
                    tk.destroy()
                except:
                    pass
                application()
            else:
                Label(tk, text='Please enter both name and link\nto successfully add an app.').grid(row=10, column=10)

        l_e = Entry(tk, textvariable=lnk, width=50)
        l_e.grid(row=0, column=1)
        n_e = Entry(tk, textvariable=nam, width=50)
        n_e.grid(row=1, column=1)
        Label(tk, text='enter the name of the app:').grid(row=0, column=0)
        Label(tk, text='enter the link of the app:').grid(row=1, column=0)
        ttk.Button(tk, text='add', command=submit).grid(row=2, column=2)
        tk.mainloop()

    def remove_app():
        rm_ls = auch.fetch_cked_val(dwnbx[0])
        for y in rm_ls:
            f = open('install.txt').read()
            renam = y + ',' + d_lst[y]
            rep = f.replace(renam, "#" + renam)
            ff = open('install.txt', 'w')
            ff.write(rep)
            ff.close()
        root.destroy()
        application()

    add_b = ttk.Button(root, text='Add app', command=add_app)
    add_b.grid(row=0, column=5)
    remove_b = ttk.Button(root, text='Remove selected apps', command=remove_app)
    remove_b.grid(row=0, column=2)
    install_b = ttk.Button(root, text='Install selected apps', command=download_selected)
    install_b.grid(row=0, column=3)
    install_all_b = ttk.Button(root, text='Install all', command=download_all)
    install_all_b.grid(row=0, column=4)
    root.mainloop()


application()

bxs = []
copyfiles = Tk()
copyfiles.geometry(f'{copyfiles.winfo_screenwidth() - 500}x{copyfiles.winfo_screenheight() - 300}+100+100')
copyfiles.title('Auto installer')


def start_copy():
    global bxs, cpy
    for x in bxs:
        os.chdir(f"{windisk}:\\Users\\{user}\\Downloads\\")
        os.mkdir(x)
        os.chdir(f"{root_dir}\\docopy\\")
        if os.path.isdir(x):
            os.system(f'xcopy "{root_dir}\\docopy\\{x}" "{windisk}:\\Users\\{user}\\Downloads\\{x}" /E /I > NUL')
        elif os.path.isfile(x):
            os.system(f'copy "{root_dir}\\docopy\\{x}" "{windisk}:\\Users\\{user}\\Downloads\\{x}" > NUL')
    cpy = True
    os.chdir(root_dir)
    bxs = []


def copy_selected():
    global bxs
    bxs = auch.fetch_cked_val(dd[0])
    copyfiles.destroy()
    threading.Thread(target=start_copy).start()

def copy_all():
    global bxs
    bxs = os.listdir()
    copyfiles.destroy()
    threading.Thread(target=start_copy).start()

os.chdir('docopy')
dd = auch.cr_checkbox(copyfiles, sequence=os.listdir(), bg=theme, fg=f_theme)
install_b = ttk.Button(copyfiles, text='copy selected', command=copy_selected)
install_b.grid(row=0, column=3)
install_all_b = ttk.Button(copyfiles, text='copy all', command=copy_all)
install_all_b.grid(row=0, column=4)
copyfiles.mainloop()


def close():
    while inst and cpy:
        os.abort()


threading.Thread(target=close).start()

