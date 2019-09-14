import numpy as np
from sklearn.cluster import KMeans

def loadData(filePath):
    file = open(filePath, 'r+')
    lines = file.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1,len(items))])
    for i in range(1, len(items)):
        return retData, retCityName

if __name__ == '__main__':
    data, cityName = loadData('C:\\Users\\Vilily\\OneDrive\\桌面\\python\\vs code\\mooc_ml\\city.txt')
    # print(data)
    # print(cityName)
    km = KMeans(n_clusters=4)
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_,axis=1)
    #print(expenses)
    CityCluster = [[],[],[],[]]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])