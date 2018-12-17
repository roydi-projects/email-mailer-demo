from mailer import Mailer
import time

def main():
    m = Mailer()
    m.send({
        'to': 'john.doe@hotmail.com',
        'subject': 'Hi man'
    })
    m.send({
        'to': 'dane.doe@hotmail.com',
        'subject': 'Hello...'
    })
    m.send({
        'to': 'john.doe@hotmail.com',
        'subject': 'Bye man'
    })
    m.cancel(1)

if __name__ == "__main__":
    main()
    time.sleep(100)