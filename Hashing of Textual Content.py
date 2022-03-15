{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f894bdb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Implement a hash function for a string\n",
    "\n",
    "# Creating Node Class\n",
    "class Node:\n",
    "    def __init__(self, s, val):\n",
    "        self.strng = s;\n",
    "        self.cnt = val;\n",
    "        self.prev = None;\n",
    "        self.next = None;\n",
    "        \n",
    "# Initialize Linked List\n",
    "class init_Lst:\n",
    "    def __init__(self):\n",
    "        self.head = None;\n",
    "import re        \n",
    "\n",
    "#Creating Radix of string and Hashing\n",
    "def HASH_STRING(s):\n",
    "    hash_var = 0\n",
    "    ctr = 0\n",
    "    hash_val = 0\n",
    "    for c in s:\n",
    "        hash_var = hash_var + ((128 ** ctr) * ord(c))\n",
    "        ctr = ctr + 1\n",
    "    hash_val = hash_var % 23\n",
    "    \n",
    "    return hash_val\n",
    "\n",
    "#Find key in Index Array A\n",
    "def FIND(A, key):\n",
    "    hash_key = HASH_STRING(key);\n",
    "    i = 0;\n",
    "    flag = 0;\n",
    "    add_hash = 0;\n",
    "    add_hash_func = 0;\n",
    "    key_Node = None;\n",
    "    while i < len(A) and flag == 0:\n",
    "        if A[i][0] == hash_key:\n",
    "            add_hash = A[i][1];\n",
    "            add_hash_func = i;\n",
    "            flag = 1;\n",
    "        i = i + 1;\n",
    "    if add_hash != 0:\n",
    "        key_Node = SEARCH_LST(add_hash, key);\n",
    "    return [add_hash, add_hash_func, key_Node, hash_key];\n",
    "    \n",
    "#Search for value in linked list\n",
    "def SEARCH_LST(Node_Head, key):\n",
    "    flag = 0;\n",
    "    tmp_Node = Node_Head;\n",
    "    key_Node = None;\n",
    "    while (tmp_Node != None) and flag == 0:\n",
    "        if (tmp_Node.strng == key):\n",
    "            flag = 1;\n",
    "            key_Node = tmp_Node;\n",
    "        tmp_Node = tmp_Node.next;\n",
    "    return key_Node;\n",
    "\n",
    "#Insert new node\n",
    "def INSERT(A, key, val):\n",
    "    tmp = [];\n",
    "    tmp = FIND(A, key);\n",
    "    head = 0;\n",
    "    if tmp[0] == 0:\n",
    "        Lnkd_Lst = init_Lst();\n",
    "        val_1 = Node(key, val);                \n",
    "        Lnkd_Lst.head = val_1;\n",
    "        A.append([tmp[3], Lnkd_Lst.head]);\n",
    "    elif tmp[2] == None:\n",
    "        val_1 = Node(key, val);\n",
    "        node_rep = A[tmp[1]][1];\n",
    "        A[tmp[1]][1] = val_1;\n",
    "        val_1.next = node_rep;\n",
    "        node_rep.prev = val_1;\n",
    "    else:\n",
    "        INCREASE_KEY(A, key);\n",
    "    return A;\n",
    "\n",
    "#Delete node\n",
    "def DELETE(A, key):\n",
    "    tmp = FIND(A, key);\n",
    "    node_del = tmp[2];\n",
    "    if (node_del.prev != None and node_del.next != None):\n",
    "        tmp_1 = node_del.prev;\n",
    "        tmp_2 = node_del.next;\n",
    "        tmp_1.next = tmp_2;\n",
    "        tmp_2.prev = tmp_1;\n",
    "    elif (node_del.prev != None and node_del.next == None):       \n",
    "        tmp_1 = node_del.prev;\n",
    "        tmp_1.next = None;\n",
    "    elif (node_del.prev == None and node_del.next != None):\n",
    "        tmp_1 = node_del.next;\n",
    "        tmp_1.prev = None;\n",
    "        A[tmp[1]][1] = tmp_1;\n",
    "    else:\n",
    "        A[tmp[1]][1] = None;\n",
    "    return A;\n",
    "        \n",
    "#Increase Key of Node\n",
    "def INCREASE_KEY(A, key):\n",
    "    tmp = FIND(A, key);\n",
    "    tmp[2].cnt = tmp[2].cnt + 1;\n",
    "\n",
    "#List all key value pairs\n",
    "def LIST_ALL(A):\n",
    "    head = None;\n",
    "    s = \"\";\n",
    "    for h in A:\n",
    "        head = h[1];\n",
    "        while head != None:\n",
    "            s = s + (\"\\nString\\n\");\n",
    "            s = s + (head.strng);\n",
    "            s = s + (\"\\nCount\\n\");\n",
    "            s = s + str(head.cnt);\n",
    "            head = head.next;\n",
    "    return s;\n",
    "            \n",
    "#Taking the input and running it through the code\n",
    "A = [];\n",
    "\n",
    "inp = open('Random.txt','r');\n",
    "String_Val = inp.readlines();\n",
    "inp.close();\n",
    "\n",
    "for String_Value in String_Val:\n",
    "    if String_Value != \"\":\n",
    "        String_Value = (re.sub('[^A-Za-z0-9 ]+', '', String_Value)).lower();\n",
    "        str_Lst = String_Value.split(\" \");\n",
    "        for s in str_Lst:\n",
    "            if s!= \" \":\n",
    "                A = INSERT(A, s, 1);\n",
    "            \n",
    "\n",
    "\n",
    "output_file = open(\"Output_File.txt\", \"w\");\n",
    "output_file.write(LIST_ALL(A));"
   ]
  }