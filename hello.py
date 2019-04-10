#TODO: 아래의 반복문을 함수화 한 후, __main__일 때만 동작하도록 구성하시오.

def do_loop_cs():
    for i in range(1,5+1):
        if i%2==0:
            print('hello python with git in another dimension.')
        else:
            print("Nothing to say")


if __name__=='__main__':
    do_loop_cs();
