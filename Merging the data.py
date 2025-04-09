import pandas as pd


Dataframe1= pd.read_csv('cleaned_ingredients.csv')

Dataframe2= pd.read_csv('food_ingredients_and_allergens.csv')

Dataframe3= pd.read_csv('nutrition.csv')


# print (Dataframe1.columns.tolist())
# print (Dataframe2.columns.tolist())
# print (Dataframe3.columns.tolist())




dataframe1=Dataframe1.drop(columns=['NDB_No','Energy_kcal', 'Protein_g', 'Saturated_fats_g', 'Fat_g', 'Carb_g', 'Fiber_g', 'Sugar_g', 'Calcium_mg', 'Iron_mg', 'Magnesium_mg', 'Phosphorus_mg', 'Potassium_mg', 'Sodium_mg', 'Zinc_mg', 'Copper_mcg', 'Manganese_mg', 'Selenium_mcg', 'VitC_mg', 'Thiamin_mg', 'Riboflavin_mg', 'Niacin_mg', 'VitB6_mg', 'Folate_mcg', 'VitB12_mcg', 'VitA_mcg', 'VitE_mg', 'VitD2_mcg'],axis=1)
df1=pd.DataFrame(dataframe1)

dataframe2=Dataframe2.drop(columns=['Food Product','Sweetener', 'Fat/Oil', 'Seasoning', 'Allergens', 'Prediction'],axis=1)
df2=pd.DataFrame(dataframe2)

dataframe3=Dataframe3.drop(columns=['Unnamed: 0','serving_size', 'calories', 'total_fat', 'saturated_fat', 'cholesterol', 'sodium', 'choline', 'folate', 'folic_acid', 'niacin', 'pantothenic_acid', 'riboflavin', 'thiamin', 'vitamin_a', 'vitamin_a_rae', 'carotene_alpha', 'carotene_beta', 'cryptoxanthin_beta', 'lutein_zeaxanthin', 'lucopene', 'vitamin_b12', 'vitamin_b6', 'vitamin_c', 'vitamin_d', 'vitamin_e', 'tocopherol_alpha', 'vitamin_k', 'calcium', 'copper', 'irom', 'magnesium', 'manganese', 'phosphorous', 'potassium', 'selenium', 'zink', 'protein', 'alanine', 'arginine', 'aspartic_acid', 'cystine', 'glutamic_acid', 'glycine', 'histidine', 'hydroxyproline', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'proline', 'serine', 'threonine', 'tryptophan', 'tyrosine', 'valine', 'carbohydrate', 'fiber', 'sugars', 'fructose', 'galactose', 'glucose', 'lactose', 'maltose', 'sucrose', 'fat', 'saturated_fatty_acids', 'monounsaturated_fatty_acids', 'polyunsaturated_fatty_acids', 'fatty_acids_total_trans', 'alcohol', 'ash', 'caffeine', 'theobromine', 'water'],axis=1)
df3=pd.DataFrame(dataframe3)

df1.columns=["Ingredient"]
df2.columns=["Ingredient"]
df3.columns=["Ingredient"]



df1.merge(df2, on="Ingredient", how="outer")
df1.merge(df3, on="Ingredient", how="outer")

print (df1)

inventory= pd.DataFrame(df1)



inventory['Quantity']=200

inventory.to_csv('inventory.csv', index=False)