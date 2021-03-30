import pickle, closenot as cl

in_list = []
out_list = []
filename = input('Enter filename: ')

try:
    with open(filename+'.dll', 'rb') as f:
        inp = pickle.load(f)

    for con in inp:
        res = int("".join(str(x) for x in con), 2)
        in_list.append(res)

    #print(in_list,out_list)

    for ch in in_list:
        out_list.append(chr(ch))

    out = ''.join(out_list)

    with open(filename+'.txt', 'w') as f:
        f.write(out)

    print('The output is:', out)
    
    cl.main()
except FileNotFoundError:
    print('Error. Encrypted file not found')
    cl.main()
except Exception as error:
    print('Error. ',error)
    cl.main()
