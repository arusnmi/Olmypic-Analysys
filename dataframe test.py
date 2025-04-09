import pandas as pd
df = pd.read_csv("hf://datasets/AkashPS11/recipes_data_food.com/recipes.csv")

nesecary_data={'Name of food':df["Name"],'Total time of making':df["TotalTime"],'Ingredeants':df["RecipeIngredientParts"], 'Quantity of ingredeients':df["RecipeIngredientQuantities"], 'Type of food':df["RecipeCategory"]}

print(df.iloc[3200])

df_final=pd.DataFrame(nesecary_data)


df_final= df_final.dropna()

print (df_final)