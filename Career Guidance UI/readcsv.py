import csv

def Get_career(test):
    with open('DB_master.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = csv.reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

    res=['','','','']
    for i in list_of_rows:
        if (test[0][0]==i[0] and test[0][1]==i[1] and test[0][2]==i[2]):
            res[0]=i[3]

        if (test[1][0]==i[0] and test[1][1]==i[1] and test[1][2]==i[2]):
            res[1]=i[3]
            
        if (test[2][0]==i[0] and test[2][1]==i[1] and test[2][2]==i[2]):
            res[2]=i[3]

        if (test[3][0]==i[0] and test[3][1]==i[1] and test[3][2]==i[2]):
            res[3]=i[3]
    res = [i for n, i in enumerate(res) if i not in res[:n]]
    return(res)
