class Univariate():
    def QuanQual(dataset):
        qual=[]
        quan=[]
        
        for column in dataset.columns:
            if dataset[column].dtypes=='O':
                #print("Qual")
                qual.append(column)
            else:
                #print("Quan")
                quan.append(column)
        return quan, qual
    