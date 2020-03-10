# -*- encoding: utf-8 -*-
'''
@File    :   with_test.py
@Time    :   2020/02/24 21:44:33
'''


class File:
    def __init__(self, filename, mode):
        super().__init__()
        self.filename = filename
        self.mode = mode 
    
    def __enter__(self):
        print('进入...')
        self.f =  open(self.filename, self.mode)
        # if self.mode == "a":
        #     print("==={}".format(self.f.read()))
        return self.f

    def __exit__(self, exc_type=None, exc_val=None, exc_tbs=None):
        print('退出...')
        self.f.close()


def main():
    with File('./jj.txt', 'a') as fp:
        fp.write('aa')
        print("type(fp)={}".format(type(fp)))
    print("你好,再见")

if __name__ == "__main__":
    main()
