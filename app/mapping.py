# Mappings

# df['Sex'] = df['Sex'].map( {'male': 0, 'female': 1} ).astype(int) 
def map_sex(sex):
    if sex.lower() == 'male':
        return 0
    elif sex.lower() == 'female':
        return 1
    else:
        return -1 

# df['Family_size'] = df['Parch'] + df['SibSp'] + 1
def map_family_size(parch, sibsp):
    return parch + sibsp + 1

# df.loc[df['Family_size'] == 1, 'IsAlone'] = 1
def map_is_alone(family_size):
    if family_size > 1: 
        return  0
    else:
        return 1

# df['Title'] = df['Name'].apply(lambda x : x.split('.')[0].split(',')[1].strip())
# df.loc[df['Title'] == 'Mlle','Title'] = 'Miss'
# df.loc[df['Title'] == 'Mme', 'Title'] = 'Miss'
# df.loc[df['Title'] == 'Ms', 'Title'] = 'Miss'
# rare_titles = ['Dr', 'Rev', 'Col', 'Major', 'Don','Dona', 'Lady', 'the Countess','Capt','Sir', 'Jonkheer']
# for r in rare_titles:
#     df.loc[df['Title'] == r, 'Title'] = 'Rare Title'

# df['Title'] = df['Title'].map({'Mr':0, 'Miss':1, 'Mrs':2, 'Master':3, 'Rare Title':4}).astype(int)
def map_title(name):
    title =  name.split('.')[0].split(',')[1].strip()
    if title in ['Mlle', 'Mme', 'Ms']:
        title = 'Miss'
    elif title in ['Dr', 'Rev', 'Col', 'Major', 'Don','Dona', 'Lady', 'the Countess','Capt','Sir', 'Jonkheer']:
        title = 'Rare Title'
    
    if title == 'Mr': 
        return 0
    elif title == 'Miss':
        return 1
    elif title == 'Mrs':
        return 2
    elif title == 'Master':
        return 3
    elif title == 'Rare Title':
        return 4
    else:
        return -1

# bins = [0, 2, 12, 18, 25, 54, 65, np.inf]
# # labels = ['baby','child','teenager',"young adult",'adult','senior','older person']
# labels = [0,1,2,3,4,5,6]
def map_age(age):
    if age < 0:
        return -1
    elif age < 2:
        return 0
    elif age < 12:
        return 1
    elif age < 18:
        return 2
    elif age < 25:
        return 3
    elif age < 54:
        return 4
    elif age < 65:
        return 5
    else:
        return 6