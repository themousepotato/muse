#!/usr/bin/python3

from gi.repository import Notify, GdkPixbuf
import time, random, ast

def main():
    with open('/usr/share/muse/quotes.txt', 'r') as f:
        data = f.read().split('\n')
        f.close()

    quote, author = ast.literal_eval(data[random.randint(0,len(data))])

    Notify.init("muse")
    notification = Notify.Notification.new(quote, author)

    image = GdkPixbuf.Pixbuf.new_from_file("/usr/share/muse/img/%s.png" % random.randint(1, 6))

    notification.set_icon_from_pixbuf(image)
    notification.set_image_from_pixbuf(image)

    time.sleep(3)
    notification.show()

if __name__ == '__main__':
    main()
