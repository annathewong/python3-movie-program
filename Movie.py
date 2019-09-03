class Movie:

    def __init__(self,name,category,description,price): 
        self.__name=name
        self.__category=category
        self.__description=description
        self.__price=price

    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name=name

    def getCategory(self):
        return self.__category 

    def setCategory(self,category):
        self.__category=category

    def getDescription(self):
        return self.__description

    def setDescription(self,description):
        self.__description=description

    def getPrice(self):
        return self.__price   

    def setPrice(self,price):
        self.__price=price

    def getPriceWithGST(self):
        return(round(self.__price*1.07, 2))

    


