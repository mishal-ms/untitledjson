import json
import time
x = input('do you want to import  database and perform operations on it yes/no:')
if(x=='yes'):
    print('loading master database in temp..')
    with open('master.json.py.','r') as masteropen:
        data_load = json.load(masteropen)
        temp = data_load
        print('loaded master database')
        print(temp)
        d = temp
        def read(k):
            if k not in d:
                print('error: this key is not present')
            else:
                b = d[k]
                if b[1]!=0:
                    if time.time()<b[1]:
                        stri=str(k)+":"str(b[0])
                        return stri
                    else:
                        print('error:time to live of',k,'has expired')
                        if(x==4):
                            break
                        if(x==1):
                            key = input('enter key for input')
                            value = int(input('enter its corresponding value'))
                            create(key,value)
                        if(x==2):
                            key = input('enter a key to read')
                            print(read(str(key)))
                        if(x==3):
                            key = input('enter key')
                            delete(key)
                            print('key deleted')
                        if(x==5):
                            print(d)
                            import json
                            temp = d

                            with('temp.json', 'w')as fp:
                                json.dump(temp, fp)
                                print('thank you')
                                exit()
                            x = input('do you want to save this the master dataset yes/no:')
                            if (x == 'yes'):
                                data = {}
                                import json
                                with open('master.json.py', 'r')as fp:
                                    data = json_load(fp)
                                    master = dict(data)
                                    master.update(temp)
                                    with open('master.json.py', 'w')as fp:
                                        json.dump(master, fp)
                                        print('all task done,thank you')


