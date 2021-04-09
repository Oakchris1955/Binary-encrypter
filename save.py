import pickle, close_notification as cl
in_list = []
out_list = []
inp = input('Enter characters: ')
filename = input('Enter filename: ')
for ch in inp:
    in_list.append(ord(ch))
#print(in_list)

for con in in_list:
    res = [int(i) for i in list('{0:0b}'.format(con))]
    out_list.append(res)
    
#print(out_list)

with open(filename+'.dll','wb') as f:
    pickle.dump(out_list, f)
cl.main(5)
