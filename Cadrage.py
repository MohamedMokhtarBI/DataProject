import importation as imported

class cadrage ():
    def __init__(self,path):
        self.path=path
        print(path)
        self.createdataframes()

    def readcsv(self,file):
        return imported.pd.read_csv(file,delimiter=";")

    def createdataframes(self):
        dataframe_sdd=imported.pd.concat(map(self.readcsv,imported.glob.glob(self.path+"*SDD*.csv"))).reset_index(drop=False)
        dataframe_assbv=imported.pd.concat(map(self.readcsv,imported.glob.glob(self.path+"*ASSBV*.csv"))).reset_index(drop=False)
        return dataframe_sdd,dataframe_assbv

    def dropnull(self,dataframe,colonnes):

        return dataframe.dropna(subset=colonnes,inplace=True)
    
    def drop_dupliactes(self,dataframe,colonnes):

        return dataframe.drop_duplicates(subset=colonnes,inplace=True)
    
    def fillnull(self,dataframe,dict):

        return dataframe.fillna(dict,inplace=True)
    
    def verifydate(self,chaine):        
        try:
            imported.parse(chaine,fuzzy=False)
            return True
        except ValueError:
            return False
        
    def changedate(self,dataframe):
        for i in dataframe.index : 
            if not self.verifydate(dataframe["Date"][i]):
                dataframe.loc[i,["Date"]]=imported.datetime.today().strftime("%d/%m/%Y")
        return dataframe
    def nettoyage(self,dataframesdd,dataframeassbv):
        self.drop_dupliactes(dataframesdd,["Compte"])        
        self.dropnull(dataframesdd,["Compte"])
        self.fillnull(dataframesdd,{"Date":"None","Montant":0})
        self.changedate(dataframesdd)
        dataframesdd=dataframesdd[["Compte","Date","Montant"]].reset_index(drop=True)
        self.drop_dupliactes(dataframeassbv,["Compte"])        
        self.dropnull(dataframeassbv,["Compte"])
        self.fillnull(dataframeassbv,{"Date":"None","Montant":0})
        self.changedate(dataframeassbv)
        dataframeassbv=dataframeassbv[["Compte","Date","Montant"]].reset_index(drop=True)
        return dataframesdd,dataframeassbv
    def calculsomme(self,dataframe,colonne):
        return dataframe[colonne].sum()
    def cadrage(self,dataframesdd,dataframeassbv):
        cadrageok=imported.pd.merge(dataframe_sdd,dataframe_assbv,on=['Compte','Date','Montant'],how="right",indicator=True)
        print(cadrageok)
        #cadrage_assbv_ko=
        #cadrage_sdd_ko=
        return "ok"

a=cadrage(imported.filepath)
dataframe_sdd ,dataframe_assbv=a.createdataframes()
dataframe_sdd ,dataframe_assbv=a.nettoyage(dataframe_sdd,dataframe_assbv)
print(dataframe_sdd)
print(dataframe_assbv)
a.cadrage(dataframe_sdd ,dataframe_assbv)
