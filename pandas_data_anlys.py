import pandas as pd
class Process():
    def __init__(self,fn):
        self.fn = fn
        self.header = 5 # the head of 5 rows is not expect to read
        self.pd_in = pd.read_table(self.fn,header=None,skiprows=self.header)
        self.pd_in.drop(labels=[0,1,3,4,5,6,7],axis=1,inplace=True) #delete the colums dont wanted
        self.gen_id ,self.gen_name ,self.gen_type= 'gene_id','gene_name','gene_type' #the index of out dataframe
        self.pd_out = pd.DataFrame()
    def process(self):
        self.pd_out = self.pd_in[8].apply(self.mapfunc)
        self.pd_out["exon"] = self.pd_in[2]
        self.pd_out.to_csv(self.fn + "out.csv")
    def mapfunc(self,line):
        dic = {self.gen_id:None,self.gen_name:None,self.gen_type:None}
        line = [x.strip(" ") for x in line.split(";")]
        for i in line:
            i = i.split(" ")
            if len(i)==2 and self.gen_id in i[0] :
                dic[self.gen_id] = i[1]
            if len(i)==2 and self.gen_name in i[0]:
                dic[self.gen_name] = i[1]
            if len(i)==2 and self.gen_type in i[0]:
                dic[self.gen_type] = i[1]
        return pd.Series([dic[self.gen_id],dic[self.gen_name],self.gen_type],index = [self.gen_id,self.gen_name,self.gen_type])
if __name__ == '__main__':
    path = r"./data/origin_data.txt"
    Process(path).process()