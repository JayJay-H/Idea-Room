```PYTHON
def bubble(lst):  # 버블정렬함수
    temp = 0
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
            else:
                continue


def freq_chk(bin_list, alpha_list, freq_list):  # 빈도수를 세는 함수
    k = 0
    for i in alpha_list:
        if i=='ㄱ':
            i='\n'
        for j in bin_list:
            if i == j:
                freq_list[k] += 1
        k += 1


def put_zero(freq_list, alpha_list):  # 빈도수 리스트(freq_list)를 alpha_list요소수 만큼 0으로 초기화 하는 함수
    for i in range(len(alpha_list)):
        freq_list += [0]


def put_zero_to_tree(freq_list, tree_list):  # tree_list를 들어갈 요소 수만큼 0으로 초기화하는 함수.
    for i in range(2 * (len(freq_list) - 1)):
        tree_list += [0]


def show_list(alpha_list, _list):  # 리스트를 볼때 쓰는 함수.
    length = len(alpha_list)
    for i in range(length):
        print("{}:{} ".format(_list[i], alpha_list[i]), end=' ')


def rebubble(alpha_list, lst):  # 빈도수를 내림차순으로 정리하고 빈도수와 매치되는 문자들도 같이 자리를 이동시키는 함수.
    temp = 0
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                temp = 0
                temp = alpha_list[j]
                alpha_list[j] = alpha_list[j + 1]
                alpha_list[j + 1] = temp
            else:
                continue


def make_tree(fl, tl):  # 트리구조를 만드는 함수.
    put_zero_to_tree(fl, tl)
    if fl[0] < fl[1]:
        tl[0] = fl[1]
        tl[1] = fl[0]
    else:
        tl[0] = fl[0]
        tl[1] = fl[1]
    for k in range(1, len(fl) - 1):
        tl[2 * k] = tl[2 * k - 1] + tl[2 * (k - 1)]
        tl[2 * k + 1] = fl[k + 1]


def make_binary(fl, tl, bl):  # 트리구조에 따라 허프만 알고리즘에 따라 0또는 1로 바꿔주는 함수.
    put_zero_to_tree(fl, bl)
    for i in range(0, len(tl) - 1, 2):
        if tl[i] > tl[i + 1]:
            bl[i] = '0'
            bl[i + 1] = '1'
        elif tl[i] < tl[i + 1]:
            bl[i] = '1'
            bl[i + 1] = '0'
        else:
            bl[i] = '0'
            bl[i + 1] = '1'


def make_code_list(al, bl, cl):  # 코드표를 만드는 함수.
    reset_code_list(al, cl)
    i = 0
    for j in range(0, len(bl) - 1, 2):
        for k in range(len(bl) - 2, j - 1, -2):
            cl[i] += bl[k]
        i += 1
    i = len(cl) - 1
    for k in range(len(bl) - 1, 0, -2):
        cl[i] += bl[k]
        i -= 1


def reset_code_list(al, cl):  # code_list를 alpha_list의 요소 수만큼 빈 문자열로 초기화 시키는 함수.
    for i in range(len(al)):
        cl += ['']


def real_alpha_list(al, fl):  # 코드표와 그에 해당하는 alpha_list의 요소를 일치시키는 함수.
    temp = 0
    if fl[0] < fl[1]:
        temp = al[0]
        al[0] = al[1]
        al[1] = temp


def compress_list(name, al, cl, bin_list):  # 코드표에 따라 문자를 문자에 맞는 코드로 바꾸고 compress_article이라는 파일에 변환하여 써줍니다.
    for i in range(len(al)):
        if al[i]=='ㄱ':
            al[i]='\n'
        for j in range(len(bin_list)):
            if al[i] == bin_list[j]:
                bin_list[j] = cl[i]
    f = open(path+name+'\\'+ name+'_compressed_text.txt', 'w')
    for i in bin_list:
        f.write(i)
    f.close()


def make_code_table(name, code_list, alpha_list):  # 복호화를 위한 테이블을 만들어주는 함수.
    f = open(path+name+'\\'+ name+"_code_table.txt", "w")

    for i in code_list:
        f.write(i)
        f.write('2')
    f.write('\n')
    for i in alpha_list:
        if i=='\n':
            f.write('ㄱ')
        else:
            f.write(i)
    f.close()
def filename(): #파일이름을 정하거나 원래있는 파일을 변환하기 위한 함수.
    import os

    print('==========================================')
    print('(1).파일 새로 만들기\n(2).만들어진 파일 이진수로 다시 변환하기')
    print('==========================================')
    print('둘중 실행하고자 하는 번호를 입력해주세요.')
    while(True):
        try:
            q = int(input('-->'))
            if q!=1 and q!=2:
                print('1 과 2 둘중의 하나만 입력해주세요.')
            elif q==1 or q==2:
                break
        except:
            print('숫자로 입력해주세요.')
    if q==1:
        name = input("압축할 내용이 저장될 텍스트 파일 이름을 입력해주세요. : ")
        newPath = path + name
        try:
            os.mkdir(newPath)
        except:
            print('\n이미 존재하는 파일입니다.\n혹시 텍스트를 변경하시고 다시 이진수 변환을 시도하신거라면 2번을 눌러주세요.\n')
            return filename()
        f = open(newPath +'\\'+ name + '.txt', 'w')
        f.write('Basic text')
        f.close()
        print('\n생성되었습니다.\n')
        print('꼭 읽어주세요!!!')
        print('허프만 알고리즘 폴더 안에 있는 ',name, '텍스트 파일의 내용을 수정하고 이 프로그램을 다시 실행시켜 2번으로 변환시켜주세요!! \n 이후 그 내용에 따라 이진수로 변환한 {}_compressed_text 텍스트 파일이 생깁니다.'.format(name))
        return(name)
    else:
        print('이진수를 변환할 때 정했던 텍스트 파일의 이름을 적어주세요(대문자, 소문자 구별하지 않아도 됩니다.)')
        name = input('-->')
        try:
            f = open(path + name +'\\' + name + '.txt', 'r')
            f.close()
            return(name)
        except:
            print('\n존재하지 않는 파일입니다.\n')
            return filename()


 #====================Main======================#
 import os
 desktopPath = os.path.expanduser('~\\desktop\\')
 try:
     os.mkdir(desktopPath+'허프만 알고리즘')
 except:
     path = desktopPath + '허프만 알고리즘\\'

 path = desktopPath + '허프만 알고리즘\\'
 name=filename() #새로 파일을 생성하거나 만들어진 파일을 이진수로 변환합니다.
 newPath = path+name+'\\' #허프 파일 안에 이름정한 그 파일 안에~
 f = open(newPath + name + '.txt', 'r')  # 파일을 열고 내용을 문자열로써 읽어 _list에 저장합니다.
 _list = f.readlines()
 f.close()

 bin_list = []  # 빈 리스트로써 파일에서 읽은 문자들을 하나씩 떼어 리스트에 넣습니다.
 set_list = []  # 빈 리스트를 집합으로 만들어 중복을 제거함으로써 파일의 내용에서 나온 글자들을 알아냅니다.
 ascii_list = []  # 글자들을 아스키 문자로 만들어 넣을 리스트입니다.
 alpha_list = []  # 오름차순으로 정렬된 아스키 코드들을 문자로 바꾸어 넣을 리스트 입니다.
 freq_list = []  # 문자들의 빈도수를 세어 넣을 리스트 입니다.
 tree_list = []  # 트리 구조로 만든 수들을 나열할 리스트 입니다.
 binary_list = []  # 코드로 만들기 위해 허프만 알고리즘에 따라 트리 구조로 만들어진 수들중 큰값에는 0 작은값에는 1을 부여하고 이를 리스트로 저장합니다.
 code_list = []  # binary_list를 활용하여 허프만 알고리즘에 따라 각 문자에 대한 코드를 만들고 이를 저장할 리스트입니다.

 for i in _list:  # 파일의 내용을 한글자씩 떼어 bin_list에 넣습니다.
     for j in i:
         bin_list += [j]

 set_list = set(bin_list)  # bin_list를 집합으로 만들어 중복을 제거함으로써 파일의 내용에서 나온 글자들을 저장합니다.

 for i in set_list:  # set_list에서 한글자씩 읽어 아스키 코드로 변환후 ascii_list에 저장합니다.
     ascii_list += [ord(i)]

 bubble(ascii_list)  # ascii_list를 정렬함으로써 문자들이 오름차순으로 정렬됩니다.

 for i in ascii_list:  # 정렬된 문자들을 alpha_list에 저장합니다.
     if chr(i)=='\n':
         alpha_list+= 'ㄱ'
     else:
         alpha_list += [chr(i)]

 put_zero(freq_list, alpha_list)  # 빈도수를 저장할 freq_list를 alpha_list의 요소 수만큼 0으로 채워줍니다. (초기화)
 freq_chk(bin_list, alpha_list, freq_list)  # 빈도수를 체크합니다.
 rebubble(alpha_list, freq_list)  # 빈도수를 내림차순으로 정리하고 빈도수와 매치되는 문자들도 같이 자리를 이동시킵니다.
 #show_list(alpha_list, freq_list)#현재 파일에 있는 문자와 이 문자의 빈도수를 보여줍니다.
 make_tree(freq_list, tree_list)  # 트리구조를 만들고 이를 일렬로 나열하여 tree_list에 저장합니다.
 make_binary(freq_list, tree_list,binary_list)  # 트리 구조로 정리된 수들을 참고해 허프만 알고리즘에 따라 큰수에는 0 작은수에는 1로 정해 binary_list에 저장 합니다.
 make_code_list(alpha_list, binary_list, code_list)  # 주어진 binary_list를 통해 허프만 알고리즘에 따라 코드를 만들고 이를 저장합니다.
 real_alpha_list(alpha_list, freq_list)  # 코드 순서에 따라 alpha_list에 있는 요소들을 일치시켜줍니다.
 #print()
 #show_list(alpha_list, code_list) #현재의 코드표를 보여줍니다.
 compress_list(name, alpha_list, code_list, bin_list)  # 코드에 따라 파일의 내용을 이진수로 변환합니다.
 make_code_table(name, code_list, alpha_list)  # 복호화를 위한 테이블을 만들어줍니다.
 print()
 done = input("이진수 변환이 완료되었습니다. 마치려면 아무키나 누르세요.......")
```
