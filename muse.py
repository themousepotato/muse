#!/usr/bin/python3

from gi.repository import Notify, GdkPixbuf
import time, random, ast

def main():
    with open('/usr/share/muse/quotes.txt', 'r') as f:
        data = f.read().split('\n')
        f.close()

    quote, author = ast.literal_eval(data[random.randint(0,len(data))])

    Notify.init("muse")
    ntn = Notify.Notification.new(quote, author)

    img = GdkPixbuf.Pixbuf.new_from_file("/usr/share/muse/img/%s.png" % random.randint(1, 6))

    ntn.set_icon_from_pixbuf(img)
    ntn.set_image_from_pixbuf(img)

    time.sleep(2)

    ntn.show()

if __name__ == '__main__':
    main()
