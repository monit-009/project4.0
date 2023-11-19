import mlflow
import warnings

#ignore all warnings
warnings.filterwarnings("ignore")

def calculate(x,y):
    return(x+y)

if __name__=="__main__":
    result=calculate(20,50)
    print(result)