import os

def notify():
    from onepush import notify
    notify('serverchanturbo', sctkey=os.environ['KEY'], title='核酸检测提醒', content='核酸结果已三天')
    
if __name__ == '__main__':
    notify()
