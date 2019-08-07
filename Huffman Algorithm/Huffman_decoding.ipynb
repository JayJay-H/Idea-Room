{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_code_table(name, cl, al):  # 코드 테이블을 불러오는 함수.\n",
    "    f = open(path+name+'\\\\'+name+\"_code_table.txt\", \"r\")\n",
    "    lines = f.readlines()\n",
    "    f.close()\n",
    "    not_code_list = []\n",
    "\n",
    "    for i in lines[0]:  # code_list를 만듭니다.\n",
    "        not_code_list += [i]\n",
    "    del not_code_list[len(not_code_list) - 1]\n",
    "    make_code_list(not_code_list, cl)\n",
    "\n",
    "    for i in lines[1]:  # alpha_list를 만듭니다.\n",
    "        if i=='ㄱ':\n",
    "            al += ['\\n']\n",
    "        else:\n",
    "            al += [i]\n",
    "\n",
    "\n",
    "def make_code_list(ncl, cl):  # code_list를 만들때 필요한 함수.\n",
    "    size = 0\n",
    "    for i in range(len(ncl)):\n",
    "        if ncl[i] == '2':\n",
    "            size += 1\n",
    "    for i in range(size):\n",
    "        cl += ['']\n",
    "    j = 0\n",
    "    for i in range(len(ncl)):\n",
    "        if ncl[i] == '2':\n",
    "            j += 1\n",
    "            continue\n",
    "        cl[j] += ncl[i]\n",
    "\n",
    "\n",
    "def change(name, cl, al):  # 이진수 코드를 문자로 다시 바꾸는 함수.\n",
    "    f = open(path+name+'\\\\'+name+'_compressed_text.txt', 'r')\n",
    "    lines = f.readlines()\n",
    "    f.close()\n",
    "\n",
    "    from_list = []\n",
    "    temp = ['']\n",
    "    to_list = []\n",
    "\n",
    "    for i in lines:\n",
    "        for j in i:\n",
    "            from_list += [j]\n",
    "\n",
    "    for i in range(len(from_list)):\n",
    "        temp[0] += from_list[i]\n",
    "        if from_list[i] == '1':\n",
    "            compare(temp, cl, to_list, al)\n",
    "            temp[0] = ''\n",
    "\n",
    "        elif temp[0] == cl[0]:\n",
    "            to_list += [al[0]]\n",
    "            temp[0] = ''\n",
    "\n",
    "    f = open(path+name+'\\\\'+name+'_decode_list.txt', 'w')\n",
    "    for i in to_list:\n",
    "        f.write(i)\n",
    "    f.close()\n",
    "    done = input('복호화 되었습니다. \\n마치려면 아무키나 누르세요.......')\n",
    "\n",
    "\n",
    "def compare(tmp, cl, tl, al):  # 코드표와 이진코드를 비교하여 그에 맞는 문자로 바꾸는 함수.\n",
    "    index = 0\n",
    "    for i in range(len(cl)):\n",
    "        if cl[i] == tmp[0]:\n",
    "            index = i\n",
    "            break\n",
    "    tl += [al[index]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이진수를 변환할 때 정했던 텍스트 파일의 이름을 적어주세요(대문자, 소문자 구별하지 않아도 됩니다.)\n",
      "-->new\n",
      "복호화 되었습니다. \n",
      "마치려면 아무키나 누르세요.......\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#-----------Main-----------#\n",
    "import os\n",
    "desktopPath = os.path.expanduser('~\\\\desktop\\\\')\n",
    "path = desktopPath + '허프만 알고리즘\\\\'\n",
    "code_list = []\n",
    "alpha_list = []\n",
    "name = input('이진수를 변환할 때 정했던 텍스트 파일의 이름을 적어주세요(대문자, 소문자 구별하지 않아도 됩니다.)\\n-->')\n",
    "try:\n",
    "    load_code_table(name, code_list, alpha_list) #복호화를 위한 코드 테이블을 로드합니다.\n",
    "    change(name, code_list, alpha_list) #복호화합니다.\n",
    "except:\n",
    "    print('{}이라는 파일 이름은 존재하지 않습니다.'.format(name))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
