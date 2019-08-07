```PYTHON
def load_code_table(name, cl, al):  # 코드 테이블을 불러오는 함수.
    f = open(path+name+'\\'+name+"_code_table.txt", "r")
    lines = f.readlines()
    f.close()
    not_code_list = []

    for i in lines[0]:  # code_list를 만듭니다.
        not_code_list += [i]
    del not_code_list[len(not_code_list) - 1]
    make_code_list(not_code_list, cl)

    for i in lines[1]:  # alpha_list를 만듭니다.
        if i=='ㄱ':
            al += ['\n']
        else:
            al += [i]


def make_code_list(ncl, cl):  # code_list를 만들때 필요한 함수.
    size = 0
    for i in range(len(ncl)):
        if ncl[i] == '2':
            size += 1
    for i in range(size):
        cl += ['']
    j = 0
    for i in range(len(ncl)):
        if ncl[i] == '2':
            j += 1
            continue
        cl[j] += ncl[i]


def change(name, cl, al):  # 이진수 코드를 문자로 다시 바꾸는 함수.
    f = open(path+name+'\\'+name+'_compressed_text.txt', 'r')
    lines = f.readlines()
    f.close()

    from_list = []
    temp = ['']
    to_list = []

    for i in lines:
        for j in i:
            from_list += [j]

    for i in range(len(from_list)):
        temp[0] += from_list[i]
        if from_list[i] == '1':
            compare(temp, cl, to_list, al)
            temp[0] = ''

        elif temp[0] == cl[0]:
            to_list += [al[0]]
            temp[0] = ''

    f = open(path+name+'\\'+name+'_decode_list.txt', 'w')
    for i in to_list:
        f.write(i)
    f.close()
    done = input('복호화 되었습니다. \n마치려면 아무키나 누르세요.......')


def compare(tmp, cl, tl, al):  # 코드표와 이진코드를 비교하여 그에 맞는 문자로 바꾸는 함수.
    index = 0
    for i in range(len(cl)):
        if cl[i] == tmp[0]:
            index = i
            break
    tl += [al[index]]

#-----------Main-----------#
import os
desktopPath = os.path.expanduser('~\\desktop\\')
path = desktopPath + '허프만 알고리즘\\'
code_list = []
alpha_list = []
name = input('이진수를 변환할 때 정했던 텍스트 파일의 이름을 적어주세요(대문자, 소문자 구별하지 않아도 됩니다.)\n-->')
try:
    load_code_table(name, code_list, alpha_list) #복호화를 위한 코드 테이블을 로드합니다.
    change(name, code_list, alpha_list) #복호화합니다.
except:
    print('{}이라는 파일 이름은 존재하지 않습니다.'.format(name))
