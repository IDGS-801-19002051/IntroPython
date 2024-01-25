class OperaBas:
  #declaración de propiedades
    num1=0
    num2=0
    res=0
  #declaración o definicion del constructor de la clase
    def __init__(self,a,b) -> None:
        self.num1=a  
        self.num2=b  
  #declaración de los metodos de la clase
    def suma(self):
        self.res=self.num1 + self.num2
        print("la suma es: {}".format(self.res))

def main():
  obj=OperaBas(3,4)
  obj.suma()

if __name__=="__main__":
  main()