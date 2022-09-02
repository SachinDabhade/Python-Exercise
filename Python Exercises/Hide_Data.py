# *************************************** Hide the Data *******************************

# Importing libraries
import pickle
import requests

if __name__ == '__main__':
    
    # Using Data form google and data name is iris dataset and spliting it by newline character
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    data = requests.get(url).text
    datalist = []
    a = data.split("\n")

    for item in a:
        if len(item) != 0:
            a = item.split(", ")
            datalist.append(a)
    
    # # This methed we can use by list comprehension
    # b = [item.split(",") for item in a if len(item) != 0]
    # print(b)

    # Hiding data
    with open("data.pkl", "wb") as f:
        pickle.dump(datalist, f)

    # Unhiding data
    with open("data.pkl", "rb") as f:
        a = pickle.load(f)
        print(a)
