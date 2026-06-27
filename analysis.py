#STEP - 1

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#STEP - 2 : LOAD JSON-----------------------------------------------------------------------------------------------------------

data = pd.read_json("ecommerce_sales.json")
print("Ecommerce sale Data :\n", data)



#STEP - 3 : DATA EXPLORATION-----------------------------------------------------------------------------------------------------
#head() - dispaly first five rows of the dataset
Head = data.head()
print("First five rows : \n", Head)

#tail() - display last five rows of the dataset
Tail = data.tail()
print("Last five rows : \n", Tail)

#shape - dispaly dimensions of dataset
dimension = data.shape
print("Dimensions of dataset : \n", dimension)

#info() - gives information of each columns like datatype, count and non-null
data.info()

#describe() - describes statistics of the dataset
data.describe()

#columns - display total columns in a dataset
data.columns

#dtypes - display datatype of each column
data.dtypes

#sample() - displaya a sample random row
data.sample()
'''
data.sample(n = 4)           #select 4 random rows
data.sample(n=3, random_state = 42)      #same rows are returned everytime if we run the code
data.sample(frac = 0.5)   #select 250 rows randomly
'''

#isnull() - display whether the columns or rows contains null values (ture / false)
data.isnull()
data.isnull().sum()   #display how many null values are there in columns(1/2/3 like integers)

#duplicated() - check whether the row is duplicated from previous row or not
data.duplicated()    #true - for duplicated / false - non duplicated
data[data.duplicated()]    #display only duplicated rows


#STEP - 4 : DATA CLEANING -----------------------------------------------------------------------------------------------------
#drop duplicates
remove_duplicates = data.drop_duplicates
print("Removing Duplicates :\n ", remove_duplicates)

#drop missing value rows
missing_values = data.dropna()
print("Remove missing rows :\n", missing_values)

#remane columns
data.rename(columns = {"Category" : "Category_Name", "Product" : "Product_Name"}, inplace = True)
print(data)

#change datatype
data["Order_Date"] = pd.to_datetime(data["Order_Date"])
data.dtypes

data["Price"] = data["Price"].astype(float)


#STEP - 5 : DESCRIPTIVE STATISTICS-------------------------------------------------------------------------------------------------
Avg_price = data["Price"].mean()                                 #MEAN
print("Average of price :", Avg_price)

Avg_quantity = data["Quantity"] .mean()
print("Average of quantity :", Avg_quantity)

Avg_discount = data["Discount"].mean()
print("Average of discount :", Avg_discount)


med_price = data["Price"].median()                                 #MEDIAN
print("Median of price :", med_price)

med_quantity = data["Quantity"] .median()
print("Median of quantity :", med_quantity)

med_discount = data["Discount"].median()
print("Median of discount :", med_discount)


Mode_price = data["Price"].mode()                                 #MODE
print("Mode of price :", Mode_price)

Mode_quantity = data["Quantity"].mode()
print("Mode of quantity :", Mode_quantity)

Mode_discount = data["Discount"].mode()
print("Mode of discount :", Mode_discount)


Max_price = data["Price"].max()                                #MAXIMUM
print("Maximum price :", Max_price)

Max_quantity = data["Quantity"].max()                             
print("Maximum quantity :", Max_quantity)

Max_discount = data["Discount"].max()                     
print("Maximum discount :", Max_discount)


Min_price = data["Price"].min()                                #MINIMUM
print("Minimum price :", Min_price)

Min_quantity = data["Quantity"].min()                             
print("Minimum quantity :", Min_quantity)

Min_discount = data["Discount"].min()                     
print("Minimum discount :", Min_discount)


Var_price = data["Price"].var()                                #VARIANCE
print("Var of price :", Var_price)

Var_quantity = data["Quantity"].var()                             
print("Var of quantity :", Var_quantity)

Var_discount = data["Discount"].var()                     
print("Var of discount :", Var_discount)


Std_price = data["Price"].std()                                #STANDARD DEVIATION
print("Std of price :", Std_price)

Std_quantity = data["Quantity"].std()                             
print("Std of quantity :", Std_quantity)

Std_discount = data["Discount"].std()                     
print("Std of discount :", Std_discount)


price_count = data["Price"].value_counts()                                #COUNT
print("Count of price :", price_count)

quantity_count = data["Quantity"].value_counts()                             
print("Count of quantity :", quantity_count)

discount_count = data["Discount"].value_counts()                    
print("Count of discount :", discount_count)


Unique_price = data["Price"].unique()                                #UNIQUE
print("Unique  price :", Unique_price)

Unique_quantity = data["Quantity"].unique()                             
print("Unique quantity :", Unique_quantity)

Unique_discount = data["Discount"].unique()                    
print("Unique discount :", Unique_discount)     

Unique_OrderId = data["Order_ID"].unique()
print("Unique order Id's :", Unique_OrderId) 


#STEP - 6 : FILTERING--------------------------------------------------------------------------------------------------------------
print("Price greaterthan 60000\n")
print(
    data[data["Price"] > 60000]
)


print(
    data[
       (data["Price"] > 55000) &
       (data["Quantity"] > 3) 
    ]
)

#CHECKING MULTIPLE CONDITIONS
print(
    data[
        (data["Category_Name"] == "Home") &
        (data["Price"] > 65000) &
        (data["Quantity"] > 3)
    ]
)


print(
    data[
        (data["Delivery_Status"] == "Shipped")  |
        (data["Quantity"] > 4)
    ]
)

#STEP - 7 : SORTING
print("price by ascending order :\n", data.sort_values("Price"))
print("price by descending :\n", data.sort_values("Price", ascending = False))


print("Quantity by ascending :\n", data.sort_values("Quantity"))
print("Quantity by descending :\n", data.sort_values("Quantity", ascending = False))


print("Discount by ascending :\n", data.sort_values("Discount"))
print("Discount by descending :\n", data.sort_values("Discount", ascending = False))


#STEP - 8 : GROUPING----------------------------------------------------------------------------------------------------------------
data

category_sum = data.groupby("Category_Name")["Quantity"].sum()
print("Category wise total quantity :\n", category_sum)  

product_sum = data.groupby("Product_Name")["Discount"].sum()
print("Product wise total discount :\n", product_sum)

product_min = data.groupby("Product_Name")["Discount"].min()
print("Product wise min discount :\n", product_min)

data.groupby("Delivery_Status")["Quantity"].max()

data.groupby("Product_Name")["Price"].sum()

data.groupby("City")["Quantity"].sum()

data.groupby("Category_Name")["Price"].sum()


#STEP - 9 : AGGREGATION ---------------------------------------------------------------------------------------------------------
print(
    data.groupby("Product_Name").agg({
        "Price" : ["sum", "mean", "max", "min", "std" ],
        "Discount" : ["sum", "mean", "max", "min", "std" ],
        "Quantity" : ["sum", "mean", "max", "min", "std" ],
    }

    )
)


#STEP - 10 : VISUALIZATION --------------------------------------------------------------------------------------------------------
#HISTOGRAM
sns.histplot(            #Hist for Discount
    data,
    x = "Discount",
    kde = True
)
plt.title("Distribution of Discount")
plt.show()

sns.histplot(           #Hist for Price
    data,
    x = "Price",
    kde = True
)
plt.title("Distribution of Price")
plt.show()

#BARCHART
#Bar for product_name and quantity
product_quantity = data.groupby("Product_Name")["Quantity"].sum().reset_index()
sns.barplot(               
    product_quantity,
    x = "Product_Name",
    y = "Quantity"
)

plt.title("Total Quantity for each product")
plt.show()


#SCATTERPLOT
sns.scatterplot(
    data,
    x="Price",
    y="Quantity"
)

plt.title("Price vs Quantity")
plt.grid(True)
plt.show()


#BOX PLOT
sns.boxplot(
    data,
    x = "Category_Name",
    y = "Price"
)
plt.title("Price distribution by category")
plt.show()

#HEAT MAP
corr = data[["Price", "Discount", "Quantity"]].corr()

sns.heatmap(
    corr,
    annot = True,
    cmap = "pink"
)
plt.title("Correlation Heatmap")
plt.show()

#PIECHART
category_count = data["Category_Name"].value_counts()


plt.pie(
    category_count,
    labels=category_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Product Category Distribution")
plt.show()