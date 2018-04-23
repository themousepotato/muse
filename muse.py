#!/usr/bin/python3

from gi.repository import Notify, GdkPixbuf
import time, random, ast,os

def main():
    # selecting with probablity e
    e = 0.5
    if random.uniform(0, 1) < e :
        with open('/usr/share/muse/quotes.txt', 'r') as f:
            data = f.read().split('\n')
            f.close()
        quote, author = ast.literal_eval(data[random.randint(0,len(data))])
    else:
        os.system('fortune > ~/temp')
        home = os.path.expanduser("~")
        with open(home+'/temp', 'r') as f:
            data = f.read().split('\n')[:-1]
            f.close()
        if len(data) == 1:
            data = str([' '.join(data[0]),'']).replace('\\t','').replace('-- ','')
        else:
            data = str([' '.join(data[:-1]),data[-1]]).replace('\\t','').replace('-- ','')
        os.system('rm  ~/temp')
        quote, author = ast.literal_eval(data)

    Notify.init("muse")
    ntn = Notify.Notification.new(quote, author)

    img = GdkPixbuf.Pixbuf.new_from_file("/usr/share/muse/img/%s.png" % random.randint(1, 6))

    ntn.set_icon_from_pixbuf(img)
    ntn.set_image_from_pixbuf(img)

    time.sleep(2)

    ntn.show()

if __name__ == '__main__':
    main()
