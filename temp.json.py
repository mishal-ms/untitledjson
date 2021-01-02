import json
temp = d

with('temp.json','w')as fp:
    json.dump(temp,fp)
    print('thank you')
    exit()
x=input('do you want to save this the master dataset yes/no:')
if(x=='yes'):
    data={}
    import json
    with open('master.json.py','r')as fp:
        data = json_load(fp)
        master = dict(data)
        master.update(temp)
        with open('master.json.py','w')as fp:
            json.dump(master,fp)
            print('all task done,thank you')