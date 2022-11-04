def notify():
    from onepush import notify
    notify('serverchanturbo', sctkey==os.environ['KEY'], title='OnePush', content='Hello World!')
    
if __name__ == '__main__':
    notify()
