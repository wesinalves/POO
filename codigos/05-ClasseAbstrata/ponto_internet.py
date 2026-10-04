from abc import abstractmethod, ABCMeta

class PontoPresenca(metaclass=ABCMeta):
    @abstractmethod
    def consultar(self):
        pass

    @abstractmethod
    def cadastrar(self):
        pass


class PontoInternet(PontoPresenca):
    def __init__(self, idGesac, upload, download, beam):
            self.idGesac = idGesac
            self.upload = upload
            self.download = download
            self.beam = beam

    def cadastrar(self, bd):
        try:
            bd[self.idGesac] = self
        except:
            raise ValueError("Falha ao cadastrar registro")
        return self.idGesac


class PontoWifi(PontoPresenca):
    def __init__(self, idGesac, upload, download, beam):
            self.idGesac = idGesac
            self.upload = upload
            self.download = download
            self.beam = beam
    def consultar(self):
        pass        
    def cadastrar(self, bd):
        try:
            if self.download < 300:
                raise ValueError(f"Velocidade de download abaixo do limite -> {self.download}")
                

            if self.upload < 30:
                raise ValueError(f"Velocidade upload abaixo do limite -> {self.upload}")

            bd[self.idGesac] = self
        except:
            raise ValueError("Falha ao cadastrar registro")
        return self.idGesac


if __name__ == "__main__":

    base_internet = {}
    p1 = PontoInternet(1, 250, 890 , 24)
    p1.cadastrar(base_internet)
    p2 = PontoInternet(2, 260, 890 , 23)
    p2.cadastrar(base_internet)
    p3 = PontoInternet(3, 250, 900 , 25)
    p3.cadastrar(base_internet)
    p4 = PontoInternet(4, 280, 890 , 28)
    p4.cadastrar(base_internet)

    for k,v in base_internet.items():
        print(f"[{k}]", v, v.consultar())

    print("*"*50)
    base_wifi = {}
    p1 = PontoWifi(1, 250, 890 , 24)
    p1.cadastrar(base_wifi)
    p2 = PontoWifi(2, 260, 890 , 23)
    p2.cadastrar(base_wifi)
    p3 = PontoWifi(3, 50, 900 , 25)
    p3.cadastrar(base_wifi)
    p4 = PontoWifi(4, 280, 890 , 28)
    p4.cadastrar(base_wifi)

    for k,v in base_wifi.items():
        print(f"[{k}]", v, v.consultar())
    
