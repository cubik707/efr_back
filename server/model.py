from pyomo.environ import *

# Создаем модель
model = ConcreteModel()

# Определяем переменные
model.X1 = Var(domain=NonNegativeReals)
model.X2 = Var(domain=NonNegativeReals)
model.X3 = Var(domain=NonNegativeReals)
model.X4 = Var(domain=NonNegativeReals)
model.X5 = Var(domain=NonNegativeReals)
model.X6 = Var(domain=NonNegativeReals)
model.X7 = Var(domain=NonNegativeReals)
model.X8 = Var(domain=NonNegativeReals)
model.X9 = Var(domain=NonNegativeReals)
model.X10 = Var(domain=NonNegativeReals)
model.X11 = Var(domain=NonNegativeReals)
model.X12 = Var(domain=NonNegativeReals)
model.X13 = Var(domain=NonNegativeReals)
model.X14 = Var(domain=NonNegativeReals)
model.X15 = Var(domain=NonNegativeReals)
model.X16 = Var(domain=NonNegativeReals)
model.X17 = Var(domain=NonNegativeReals)
model.X18 = Var(domain=NonNegativeReals)
model.X19 = Var(domain=NonNegativeReals)
model.X20 = Var(domain=NonNegativeReals)
model.X21 = Var(domain=NonNegativeReals)
model.X22 = Var(domain=NonNegativeReals)
model.X23 = Var(domain=NonNegativeReals)
model.X24 = Var(domain=NonNegativeReals)
model.X25 = Var(domain=NonNegativeReals)
model.X26 = Var(domain=NonNegativeReals)
model.X27 = Var(domain=NonNegativeReals)
model.X28 = Var(domain=NonNegativeReals)
model.X29 = Var(domain=NonNegativeReals)
model.X30 = Var(domain=NonNegativeReals)
model.X31 = Var(domain=NonNegativeReals)
model.X32 = Var(domain=NonNegativeReals)
model.X33 = Var(domain=NonNegativeReals)
model.X34 = Var(domain=NonNegativeReals)
model.X35 = Var(domain=NonNegativeReals)
model.X36 = Var(domain=NonNegativeReals)
model.X37 = Var(domain=NonNegativeReals)
model.X38 = Var(domain=NonNegativeReals)
model.X39 = Var(domain=NonNegativeReals)
model.X40 = Var(domain=NonNegativeReals)
model.X41 = Var(domain=NonNegativeReals)
model.X42 = Var(domain=NonNegativeReals)
model.X43 = Var(domain=NonNegativeReals)
model.X44 = Var(domain=NonNegativeReals)
model.X45 = Var(domain=NonNegativeReals)
model.X46 = Var(domain=NonNegativeReals)
model.X47 = Var(domain=NonNegativeReals)
model.X48 = Var(domain=NonNegativeReals)
model.X49 = Var(domain=NonNegativeReals)
model.X50 = Var(domain=NonNegativeReals)
model.X51 = Var(domain=NonNegativeReals)
model.X52 = Var(domain=NonNegativeReals)

solver = SolverFactory('cbc', executable="D:\\univer\\efr-py\\back\\Cbc-releases.2.10.11-msvs-w64-mingw64\\bin\\cbc.exe")
# Целевая функция
model.obj = Objective(expr=model.X48 - model.X49, sense=maximize)
norm_cows = {
    25:{
        'conc_min':18,
        'conc_max':22,
        'seno_min':8,
        'seno_max':10,
        'senazh_min':10.5,
        'senazh_max':14.5,
        'soloma_min':2,
        'soloma_max':3,
        'silos_min':17,
        'silos_max':21,
        'green_min':30,
        'green_max':35,
    },
    26:{
        'conc_min':19,
        'conc_max':23,
        'seno_min':8,
        'seno_max':10,
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':2,
        'soloma_max':3,
        'silos_min':17,
        'silos_max':21,
        'green_min':30,
        'green_max':35,
    },
    27:{
        'conc_min':19,
        'conc_max':23,
        'seno_min':8,
        'seno_max':10,
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':2,
        'soloma_max':3,
        'silos_min':17,
        'silos_max':21,
        'green_min':30,
        'green_max':35,
    }, 
    28:{
        'conc_min':20,
        'conc_max':24,
        'seno_min':7.5,
        'seno_max':9.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':2,
        'soloma_max':3,
        'silos_min':16,
        'silos_max':20,
        'green_min':30,
        'green_max':35,
    }, 
    29:{
        'conc_min':20,
        'conc_max':24,
        'seno_min':8,
        'seno_max':11, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':16,
        'silos_max':20,
        'green_min':30,
        'green_max':35,
    }, 
    30:{
        'conc_min':21,
        'conc_max':25,
        'seno_min':8,
        'seno_max':11, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':15,
        'silos_max':19,
        'green_min':30,
        'green_max':35,
    }, 
    31:{
        'conc_min':21,
        'conc_max':25,
        'seno_min':8,
        'seno_max':11, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':16,
        'silos_max':20,
        'green_min':29,
        'green_max':34,
    }, 
    32:{
        'conc_min':21,
        'conc_max':25,
        'seno_min':8,
        'seno_max':11, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':16,
        'silos_max':20,
        'green_min':29,
        'green_max':34,
    }, 
    33:{
        'conc_min':22,
        'conc_max':26,
        'seno_min':7.5,
        'seno_max':10.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':15.5,
        'silos_max':19.5,
        'green_min':29,
        'green_max':34,
    }, 
    34:{
        'conc_min':22,
        'conc_max':26,
        'seno_min':7.5,
        'seno_max':10.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':15.5,
        'silos_max':19.5,
        'green_min':29,
        'green_max':34,
    }, 
    35:{
        'conc_min':23,
        'conc_max':27,
        'seno_min':7.5,
        'seno_max':10.5, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':14.5,
        'silos_max':18.5,
        'green_min':29,
        'green_max':34,
    }, 
    36:{
        'conc_min':23,
        'conc_max':27,
        'seno_min':9,
        'seno_max':12, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':1,
        'soloma_max':2,
        'silos_min':15,
        'silos_max':19,
        'green_min':28,
        'green_max':33,
    }, 
    37:{
        'conc_min':24,
        'conc_max':28,
        'seno_min':9,
        'seno_max':12, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':15,
        'silos_max':19,
        'green_min':28,
        'green_max':33,
    }, 
    38:{
        'conc_min':24,
        'conc_max':28,
        'seno_min':9,
        'seno_max':12, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':15,
        'silos_max':19,
        'green_min':28,
        'green_max':33,
    }, 
    39:{
        'conc_min':25,
        'conc_max':29,
        'seno_min':9,
        'seno_max':12, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':14.5,
        'silos_max':18.5,
        'green_min':28,
        'green_max':33,
    }, 
    40:{
        'conc_min':26,
        'conc_max':30,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':15.5,
        'silos_max':19.5,
        'green_min':28,
        'green_max':33,
    }, 
    41:{
        'conc_min':26,
        'conc_max':30,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':15.5,
        'silos_max':19.5,
        'green_min':28,
        'green_max':33,
    }, 
    42:{
        'conc_min':27,
        'conc_max':31,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':13.5,
        'silos_max':17.5,
        'green_min':28,
        'green_max':33,
    }, 
    43:{
        'conc_min':28,
        'conc_max':32,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':12.5,
        'silos_max':16.5,
        'green_min':28,
        'green_max':33,
    }, 
    44:{
        'conc_min':28,
        'conc_max':32,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':10,
        'senazh_max':14,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':12.5,
        'silos_max':16.5,
        'green_min':28,
        'green_max':33,
    }, 
    45:{
        'conc_min':29,
        'conc_max':33,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':12.5,
        'silos_max':16.5,
        'green_min':28,
        'green_max':33,
    }, 
    46:{
        'conc_min':29,
        'conc_max':33,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':13.5,
        'silos_max':17.5,
        'green_min':27,
        'green_max':32,
    }, 
    47:{
        'conc_min':30,
        'conc_max':34,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':12.5,
        'silos_max':16.5,
        'green_min':27,
        'green_max':32,
    }, 
    48:{
        'conc_min':30,
        'conc_max':34,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':12.5,
        'silos_max':16.5,
        'green_min':27,
        'green_max':32,
    }, 
    49:{
        'conc_min':30,
        'conc_max':34,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':11.5,
        'silos_max':15.5,
        'green_min':27,
        'green_max':32,
    }, 
    50:{
        'conc_min':31,
        'conc_max':35,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':10.5,
        'silos_max':14.5,
        'green_min':27,
        'green_max':32,
    }, 
    51:{
        'conc_min':31,
        'conc_max':35,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':10.5,
        'silos_max':14.5,
        'green_min':27,
        'green_max':32,
    }, 
    52:{
        'conc_min':31,
        'conc_max':35,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':9,
        'senazh_max':13,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':10,
        'silos_max':14,
        'green_min':27,
        'green_max':32,
    }, 
    53:{
        'conc_min':32,
        'conc_max':36,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':8,
        'senazh_max':12,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':10,
        'silos_max':14,
        'green_min':27,
        'green_max':32,
    }, 
    54:{
        'conc_min':32,
        'conc_max':36,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':7,
        'senazh_max':11,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':10,
        'silos_max':14,
        'green_min':26,
        'green_max':31,
    }, 
    55:{
        'conc_min':33,
        'conc_max':37,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':7,
        'senazh_max':11,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':10,
        'silos_max':14,
        'green_min':26,
        'green_max':31,
    }, 
    56:{
        'conc_min':33,
        'conc_max':37,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':7,
        'senazh_max':11,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':10,
        'silos_max':14,
        'green_min':26,
        'green_max':31,
    }, 
    57:{
        'conc_min':34,
        'conc_max':38,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':7,
        'senazh_max':11,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':8,
        'silos_max':13,
        'green_min':26,
        'green_max':31,
    }, 
    58:{
        'conc_min':34,
        'conc_max':38,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':7,
        'senazh_max':11,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':8,
        'silos_max':13,
        'green_min':26,
        'green_max':31,
    }, 
    59:{
        'conc_min':35,
        'conc_max':39,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':7,
        'senazh_max':11,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':8,
        'silos_max':13,
        'green_min':26,
        'green_max':31,
    }, 
    60:{
        'conc_min':35,
        'conc_max':39,
        'seno_min':7,
        'seno_max':10, 
        'senazh_min':7,
        'senazh_max':11,
        'soloma_min':0,
        'soloma_max':0,
        'silos_min':8,
        'silos_max':13,
        'green_min':26,
        'green_max':31,
    }, 
}
norm_krs ={
    350:{
        'conc_min':20,
        'conc_max':23,
        'seno_min':7.5,
        'seno_max':9.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':6,
        'soloma_max':8,
        'silos_min':9,
        'silos_max':13,
        'green_min':25,
        'green_max':35,
        'milk_min':3.5,
        'milk_max':5,
    }, 
    400:{
        'conc_min':22,
        'conc_max':26,
        'seno_min':7.5,
        'seno_max':9.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':6,
        'soloma_max':8,
        'silos_min':10,
        'silos_max':13,
        'green_min':25,
        'green_max':35,
        'milk_min':3.5,
        'milk_max':4.5,
    }, 
    450:{
        'conc_min':22,
        'conc_max':26,
        'seno_min':7.5,
        'seno_max':9.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':6,
        'soloma_max':8,
        'silos_min':10,
        'silos_max':13,
        'green_min':26,
        'green_max':34,
        'milk_min':3.5,
        'milk_max':4.5,
    }, 
    500:{
        'conc_min':24,
        'conc_max':27,
        'seno_min':7.5,
        'seno_max':9.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':5,
        'soloma_max':7,
        'silos_min':10,
        'silos_max':13,
        'green_min':26,
        'green_max':34,
        'milk_min':4.5,
        'milk_max':5.5,
    }, 
    550:{
        'conc_min':24,
        'conc_max':27,
        'seno_min':7.5,
        'seno_max':9.5, 
        'senazh_min':11,
        'senazh_max':15,
        'soloma_min':5,
        'soloma_max':7,
        'silos_min':11,
        'silos_max':14,
        'green_min':26,
        'green_max':33,
        'milk_min':4.5,
        'milk_max':5.5,
    }, 
    600:{
        'conc_min':24,
        'conc_max':27,
        'seno_min':7,
        'seno_max':9, 
        'senazh_min':12,
        'senazh_max':16,
        'soloma_min':4,
        'soloma_max':6,
        'silos_min':11,
        'silos_max':14,
        'green_min':26,
        'green_max':33,
        'milk_min':4.5,
        'milk_max':5.5,
    }, 
    650:{
        'conc_min':25,
        'conc_max':28,
        'seno_min':7,
        'seno_max':9, 
        'senazh_min':12,
        'senazh_max':16,
        'soloma_min':4,
        'soloma_max':6,
        'silos_min':11,
        'silos_max':14,
        'green_min':26,
        'green_max':33,
        'milk_min':4.5,
        'milk_max':5.5,
    }, 
    700:{
        'conc_min':26,
        'conc_max':29,
        'seno_min':7,
        'seno_max':9, 
        'senazh_min':12,
        'senazh_max':16,
        'soloma_min':4,
        'soloma_max':6,
        'silos_min':11,
        'silos_max':15,
        'green_min':24,
        'green_max':32,
        'milk_min':4.5,
        'milk_max':5.5,
    }, 
    750:{
        'conc_min':26,
        'conc_max':30,
        'seno_min':7,
        'seno_max':9, 
        'senazh_min':13,
        'senazh_max':17,
        'soloma_min':3,
        'soloma_max':5,
        'silos_min':11,
        'silos_max':15,
        'green_min':23,
        'green_max':31,
        'milk_min':4.5,
        'milk_max':5.5,
    }, 
    800:{
        'conc_min':26.5,
        'conc_max':31,
        'seno_min':6.5,
        'seno_max':8.5, 
        'senazh_min':13,
        'senazh_max':17,
        'soloma_min':3,
        'soloma_max':5,
        'silos_min':11,
        'silos_max':15,
        'green_min':21,
        'green_max':30,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    850:{
        'conc_min':27,
        'conc_max':31,
        'seno_min':6.5,
        'seno_max':8.5, 
        'senazh_min':13,
        'senazh_max':17,
        'soloma_min':3,
        'soloma_max':5,
        'silos_min':11,
        'silos_max':15,
        'green_min':21,
        'green_max':30,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    900:{
        'conc_min':28,
        'conc_max':32,
        'seno_min':6.5,
        'seno_max':8.5, 
        'senazh_min':13,
        'senazh_max':17,
        'soloma_min':3,
        'soloma_max':5,
        'silos_min':11,
        'silos_max':15,
        'green_min':20,
        'green_max':29,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    950:{
        'conc_min':28,
        'conc_max':33,
        'seno_min':6,
        'seno_max':8, 
        'senazh_min':14,
        'senazh_max':18,
        'soloma_min':2,
        'soloma_max':4,
        'silos_min':12,
        'silos_max':16,
        'green_min':20,
        'green_max':29,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    1000:{
        'conc_min':28,
        'conc_max':33,
        'seno_min':6,
        'seno_max':8, 
        'senazh_min':14,
        'senazh_max':18,
        'soloma_min':2,
        'soloma_max':4,
        'silos_min':12,
        'silos_max':16,
        'green_min':20,
        'green_max':28,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    1050:{
        'conc_min':29,
        'conc_max':34,
        'seno_min':6,
        'seno_max':8, 
        'senazh_min':14,
        'senazh_max':18,
        'soloma_min':2,
        'soloma_max':4,
        'silos_min':12,
        'silos_max':16,
        'green_min':19,
        'green_max':27,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    1100:{
        'conc_min':29,
        'conc_max':35,
        'seno_min':6,
        'seno_max':8, 
        'senazh_min':14,
        'senazh_max':18,
        'soloma_min':2,
        'soloma_max':4,
        'silos_min':13,
        'silos_max':17,
        'green_min':17,
        'green_max':26,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    1150:{
        'conc_min':30,
        'conc_max':36,
        'seno_min':6,
        'seno_max':8, 
        'senazh_min':15,
        'senazh_max':19,
        'soloma_min':1,
        'soloma_max':3,
        'silos_min':13,
        'silos_max':17,
        'green_min':15,
        'green_max':25,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
    1200:{
        'conc_min':32,
        'conc_max':38,
        'seno_min':6,
        'seno_max':8, 
        'senazh_min':15,
        'senazh_max':19,
        'soloma_min':1,
        'soloma_max':3,
        'silos_min':13,
        'silos_max':17,
        'green_min':14,
        'green_max':24,
        'milk_min':5.5,
        'milk_max':6.5,
    }, 
}
def find_nearest_key(dictionary, number):
    keys = list(dictionary.keys())
    nearest_key = min(keys, key=lambda k: abs(k - number))
    return nearest_key

# Ограничения
model.constraints = ConstraintList()
def solve(vals):
# 1.1	по площади пашни
    model.constraints.add(
        model.X1 + model.X2 + model.X3 + model.X4 + model.X5 + model.X6 + model.X7 + model.X8 + model.X9 + model.X10 == vals.get('arableLand'))
# 1.2 по площади сенокосов и пастбищ улучшенных
    model.constraints.add(model.X11 + model.X12 == vals.get('hayfieldsAndPastureImproved'))
# 1.3 по площади сенокосов и пастбищ естественных:
    model.constraints.add(model.X13 + model.X14 == vals.get('hayfieldsAndPastureNatural'))

# 2.1	По наличию концентратов
    model.constraints.add(model.X34 == vals.get('winterGrains').get('onFeed') * model.X1 + vals.get('springGrains').get('onFeed') * model.X2 + vals.get('pulses').get('onFeed') * model.X3 + model.X40)
# 2.2	По наличию силоса
    model.constraints.add(model.X35 == vals.get('cornOnSilage').get('onFeed') * model.X10 + model.X41)
# 2.3	По наличию зеленого корма
    model.constraints.add(model.X36 == vals.get('greenFodderGrassHay').get('onFeed') * model.X8 + vals.get('annualGrasses').get('onFeed') * model.X9 + vals.get('pasturesOnGreenFodder').get('onFeed') * model.X13 + model.X42)
# 2.4	По наличию сена
    model.constraints.add(model.X37 == vals.get('hayGrassHay').get('onFeed') * model.X6 + vals.get('hayfieldsOnHay').get('onFeed') * model.X11 + model.X43)
# 2.5	По наличию сенажа
    model.constraints.add(model.X38 == vals.get('haylageGrassHay').get('onFeed') * model.X7 + vals.get('hayfieldsOnSilage').get('onFeed') * model.X12 + model.X44)
# 2.6	По наличию соломы
    model.constraints.add(model.X39 == 12.4 * model.X1 + 14.3 * model.X2 + model.X45)

# 3.1	По приобретению концентратов
    model.constraints.add(model.X40 <= vals.get('concentrates').get('volume'))
# 3.2	По приобретению силоса
    model.constraints.add(model.X41 <= vals.get('silo').get('volume'))
# 3.3	По приобретению зеленого корма
    model.constraints.add(model.X42 <= vals.get('greenFodder').get('volume'))
# 3.4	По приобретению сена
    model.constraints.add(model.X43 <= vals.get('hay').get('volume'))
# 3.5	По приобретению сенажа
    model.constraints.add(model.X44 <= vals.get('haylage').get('volume'))
# 3.6	По приобретению соломы
    model.constraints.add(model.X45 <= vals.get('straw').get('volume'))

# 4.1	По использованию концентратов
    model.constraints.add(model.X16 + model.X22 + model.X28 <= model.X34)
# 4.2	По использованию силоса
    model.constraints.add(model.X17 + model.X23 + model.X29 <= model.X35)
# 4.3	По использованию зеленого корма
    model.constraints.add(model.X18 + model.X24 + model.X30 <= model.X36)
# 4.4	По использованию сена
    model.constraints.add(model.X19 + model.X25 + model.X31 <= model.X37)
# 4.5	По использованию сенажа
    model.constraints.add(model.X20 + model.X26 + model.X32 <= model.X38)
# 4.6	По использованию соломы
    model.constraints.add(model.X21 + model.X27 <= model.X39)

# 5.1 Баланс кормовых единиц
    model.constraints.add(vals.get('cows').get('livestock') * vals.get('cows').get('productivity') * vals.get('cows').get('consumptionOfFU') + vals.get('cows').get('livestock') * model.X15 * vals.get('cows').get('consumptionOfFU') + vals.get('youngCattle').get('livestock') * vals.get('youngCattle').get('productivity') * 30.5 * 12 * 0.00001 * vals.get('youngCattle').get('consumptionOfFU') <=
                      vals.get('winterGrains').get('onFeed') * model.X1 + vals.get('springGrains').get('onFeed') * model.X2 + vals.get('pulses').get('onFeed') * model.X3 +
                      vals.get('hayGrassHay').get('onFeed') * 0.2 * model.X6 + vals.get('haylageGrassHay').get('onFeed') * 0.28 * model.X7 +
                      vals.get('greenFodderGrassHay').get('onFeed') * 0.19 * model.X8 + vals.get('annualGrasses').get('onFeed') * 0.19 * model.X9 +
                      vals.get('cornOnSilage').get('onFeed') * 0.2 * model.X10 + vals.get('hayfieldsOnHay').get('onFeed') * 0.45 * model.X11 +
                      vals.get('hayfieldsOnSilage').get('onFeed') * 0.28 * model.X12 + vals.get('pasturesOnGreenFodder').get('onFeed') * 0.19 * model.X13 +
                      vals.get('pasturesOnSilage').get('onFeed')* 0.28 * model.X14 + model.X40 +
                      0.2 * model.X41 + 0.19 * model.X42 + 0.45 * model.X43 +
                      0.28 * model.X28 + 0.25 * model.X29)

# 5.2 Баланс переваримого протеина
    model.constraints.add(vals.get('cows').get('livestock') * vals.get('cows').get('productivity') * vals.get('cows').get('consumptionOfFU') * 0.105 + vals.get('cows').get('livestock') *  vals.get('cows').get('consumptionOfFU') * model.X15  * 0.105 + vals.get('youngCattle').get('livestock') * vals.get('youngCattle').get('productivity') * 30.5 * 12 * 0.00001 * vals.get('youngCattle').get('consumptionOfFU') * 0.102 <=
                      vals.get('winterGrains').get('onFeed') * 0.105 * model.X1 + vals.get('springGrains').get('onFeed') * 0.105 * model.X2 + vals.get('pulses').get('onFeed') * 0.105 * model.X3 +
                      vals.get('hayGrassHay').get('onFeed') * 0.01 * model.X6 + vals.get('haylageGrassHay').get('onFeed') * 0.033 * model.X7 +
                      vals.get('greenFodderGrassHay').get('onFeed') * 0.021 * model.X8 + vals.get('annualGrasses').get('onFeed') * 0.02 * model.X9 +
                      vals.get('cornOnSilage').get('onFeed') * 0.001 * model.X10 + vals.get('hayfieldsOnHay').get('onFeed') * 0.05 * model.X11 +
                      vals.get('hayfieldsOnSilage').get('onFeed') * 0.03 * model.X12 + vals.get('pasturesOnGreenFodder').get('onFeed') * 0.021 * model.X13 +
                      vals.get('pasturesOnSilage').get('onFeed') * 0.033 * model.X14 + 0.105 * model.X40 +
                      0.014 * model.X41 + 0.021 * model.X42 + 0.053 * model.X43 +
                      0.033 * model.X28 + 0.011 * model.X29)

# Баланс кормовых единиц
    model.constraints.add(vals.get('cows').get('livestock') * vals.get('cows').get('productivity') * vals.get('cows').get('consumptionOfFU') <= model.X16 + 0.2 * model.X17 + 0.19 * model.X18 +
                      0.45 * model.X19 + 0.28 * model.X20 + 0.25 * model.X21)

# 6.2 Баланс переваримого протеина
    model.constraints.add(vals.get('cows').get('livestock') * vals.get('cows').get('productivity') * vals.get('cows').get('consumptionOfFU') * 0.105 <= 0.105 * model.X16 + 0.014 * model.X17 +
                      0.021 * model.X18 + 0.053 * model.X19 + 0.033 * model.X20 +
                      0.011 * model.X21)

# 7.1 Баланс кормовых единиц
    model.constraints.add(vals.get('cows').get('livestock') * vals.get('cows').get('consumptionOfFU') * model.X15  <= model.X22 + 0.2 * model.X23 + 0.19 * model.X24 +
                      0.45 * model.X25 + 0.28 * model.X26 + 0.25 * model.X27)

# 7.2 Баланс переваримого протеина
    model.constraints.add(vals.get('cows').get('livestock')  * vals.get('cows').get('consumptionOfFU') * model.X15 * 0.105 <= 0.105 * model.X22 + 0.014 * model.X23 +
                      0.021 * model.X24 + 0.053 * model.X25 + 0.033 * model.X26 +
                      0.011 * model.X27)

# 8.1 Баланс кормовых единиц
    model.constraints.add(vals.get('youngCattle').get('livestock') * vals.get('youngCattle').get('productivity') * 30.5 * 12 * 0.00001 * vals.get('youngCattle').get('consumptionOfFU')<= model.X28 + 0.2 * model.X29 + 0.19 * model.X30 +
                      0.45 * model.X31 + 0.28 * model.X32 + 0.3 * model.X51)

# 8.2 Баланс переваримого протеина
    model.constraints.add(vals.get('youngCattle').get('livestock') * vals.get('youngCattle').get('productivity') * 30.5 * 12 * 0.00001 * vals.get('youngCattle').get('consumptionOfFU') * 0.102 <= 0.105 * model.X28 + 0.014 * model.X29 +
                      0.021 * model.X30 + 0.053 * model.X31 + 0.033 * model.X32 +
                      0.033 * model.X51)

# 9.1 по общей питательности кормов для коров:
    model.constraints.add(model.X46 == model.X16 + 0.2 * model.X17 + 0.19 * model.X18 +
                      0.45 * model.X19 + 0.28 * model.X20 + 0.25 * model.X21 +
                      model.X22 + 0.2 * model.X23 + 0.19 * model.X24 +
                      0.45 * model.X25 + 0.28 * model.X26 + 0.25 * model.X27)

# 9.2 по общей питательности кормов для КРС:
    model.constraints.add(model.X47 == model.X28 + 0.2 * model.X29 + 0.19 * model.X30 +
                      0.45 * model.X31 + 0.28 * model.X32)

# минимальная доля концентратов для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('conc_min')*0.01 * model.X46 <= model.X16 + model.X22)
# максимальная доля концентратов для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('conc_max')*0.01 * model.X46 >= model.X16 + model.X22)

# минимальная доля силоса для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('silos_min')*0.01 * model.X46 <= 0.2 * model.X17 + 0.2 * model.X23)
# максимальная доля силоса для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('silos_max')*0.01 * model.X46 >= 0.2 * model.X17 + 0.2 * model.X23)

# минимальная доля зеленого корма для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('green_min')*0.01 * model.X46 <= 0.19 * model.X18 + 0.19 * model.X24)
# максимальная доля зеленого корма для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('green_max')*0.01 * model.X46 >= 0.19 * model.X18 + 0.19 * model.X24)

# минимальная доля сена для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('seno_min')*0.01 * model.X46 <= 0.45 * model.X19 + 0.45 * model.X25)
# максимальная доля сена для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('seno_max')*0.01 * model.X46 >= 0.45 * model.X19 + 0.45 * model.X25)

# максимальная доля сена для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('senazh_min')*0.01 * model.X46 <= 0.28 * model.X20 + 0.28 * model.X26)
# максимальная доля сенажа для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('senazh_max')*0.01 * model.X46 >= 0.28 * model.X20 + 0.28 * model.X26)

# минимальная доля соломы для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('soloma_min')*0.01 * model.X46 <= 0.25 * model.X21 + 0.25 * model.X27)
# максимальная доля соломы для коров
    model.constraints.add(norm_cows.get(vals.get('cows').get('productivity')).get('soloma_max')*0.01* model.X46 >= 0.25 * model.X21 + 0.25 * model.X27)

    close_key=find_nearest_key(norm_krs, vals.get('youngCattle').get('productivity'))

# минимальная доля концентратов для КРС
    model.constraints.add(norm_krs.get(close_key).get('conc_min')*0.01 * model.X47 <= model.X28)
# максимальная доля концентратов для КРС
    model.constraints.add(norm_krs.get(close_key).get('conc_max')*0.01 * model.X47 >= model.X28)

# минимальная доля силоса для КРС
    model.constraints.add(norm_krs.get(close_key).get('silos_min')*0.01 * model.X47 <= 0.2 * model.X29)
# максимальная доля силоса для КРС
    model.constraints.add(norm_krs.get(close_key).get('silos_max')*0.01 * model.X47 >= 0.2 * model.X29)

# минимальная доля зеленого корма для КРС
    model.constraints.add(norm_krs.get(close_key).get('green_min')*0.01 * model.X47 <= 0.19 * model.X30)
# максимальная доля зеленого корма для КРС
    model.constraints.add(norm_krs.get(close_key).get('green_max')*0.01 * model.X47 >= 0.19 * model.X30)

# минимальная доля сена для КРС
    model.constraints.add(norm_krs.get(close_key).get('seno_min')*0.01 * model.X47 <= 0.45 * model.X31)
# максимальная доля сена для КРС
    model.constraints.add(norm_krs.get(close_key).get('seno_max')*0.01 * model.X47 >= 0.45 * model.X31)

# минимальная доля сенажа для КРС
    model.constraints.add(norm_krs.get(close_key).get('senazh_min')*0.01 * model.X47 <= 0.28 * model.X32)
# максимальная доля сенажа для КРС
    model.constraints.add(norm_krs.get(close_key).get('senazh_max')*0.01 * model.X47 >= 0.28 * model.X32)

# минимальная доля молока для КРС
    model.constraints.add(norm_krs.get(close_key).get('milk_min')*0.01 * model.X47 <= 0.3 * model.X51)
# максимальная доля молока для КРС
    model.constraints.add(norm_krs.get(close_key).get('milk_max')*0.01 * model.X47 >= 0.3 * model.X51)

# Ограничения по величине прироста продуктивности
    model.constraints.add(model.X15 <= 0.1 * vals.get('cows').get('productivity'))
# 6 или ввод какой-либо????
#  по технологическим ограничениям для растениеводства
    model.constraints.add(model.X1 >= 0.25 * (model.X1 + model.X2 + model.X3))  # минимальная площадь озимых зерновых
    model.constraints.add(model.X3 >= 0.07 * (model.X1 + model.X2 + model.X3))  # минимальная площадь зернобобовых
    model.constraints.add(model.X3 <= 0.1 * (model.X1 + model.X2 + model.X3))  # максимальная площадь зернобобовых
    model.constraints.add(model.X1 <= 0.4 * (model.X1 + model.X2 + model.X3))  # максимальная площадь озимых зерновых
    model.constraints.add(model.X4 <= 0.15 * vals.get('arableLand'))  # максимальная площадь рапса

# по реализации продукции
    model.constraints.add(vals.get('winterGrains').get('onProduct') * model.X1 + vals.get('springGrains').get('onProduct') * model.X2 >= vals.get('seedsContractDeliveries'))  # по реализации зерна
    model.constraints.add(vals.get('rape').get('onProduct') * model.X4 >= vals.get('rape').get('contractDeliveries'))  # по реализации рапса

# по производству молока
    model.constraints.add(vals.get('cows').get('livestock') * vals.get('cows').get('productivity') + vals.get('cows').get('livestock') * model.X15 == model.X50)  # по производству молока

# по реализации молока
    model.constraints.add(model.X52 == model.X50 - model.X51)

# по стоимости товарной продукции
    model.constraints.add(vals.get('winterGrains').get('onProduct') * vals.get('winterGrains').get('costPrice') * model.X1 + vals.get('springGrains').get('onProduct') * vals.get('springGrains').get('costPrice') * model.X2 + vals.get('rape').get('onProduct') * vals.get('rape').get('costPrice') * model.X3 +
                      + vals.get('cows').get('livestock') * vals.get('cows').get('productivity') * vals.get('milk').get('price') + vals.get('youngCattle').get('livestock') * vals.get('youngCattle').get('productivity') * vals.get('meat').get('price') * 30.5 * 12 * 0.00001 == model.X48)

# по сумме материально-денежных затрат
    model.constraints.add((vals.get('winterGrains').get('onProduct') + vals.get('winterGrains').get('onFeed')) * vals.get('winterGrains').get('sellingPricePerCent') * model.X1 + (vals.get('springGrains').get('onProduct') + vals.get('springGrains').get('onFeed')) * vals.get('springGrains').get('sellingPricePerCent') * model.X2 +
                      vals.get('pulses').get('onFeed')  * vals.get('pulses').get('sellingPricePerCent')  * model.X3 + vals.get('rape').get('yieldForecast') * vals.get('rape').get('sellingPricePerCent') * model.X4 + vals.get('hayGrassHay').get('onFeed') * vals.get('hayGrassHay').get('sellingPricePerCent') * model.X6 +
                      vals.get('haylageGrassHay').get('onFeed') * vals.get('haylageGrassHay').get('sellingPricePerCent')  * model.X7 + vals.get('greenFodderGrassHay').get('onFeed') * vals.get('greenFodderGrassHay').get('sellingPricePerCent') * model.X8 + vals.get('annualGrasses').get('onFeed') * vals.get('annualGrasses').get('sellingPricePerCent') * model.X9 +
                      vals.get('cornOnSilage').get('onFeed')* vals.get('cornOnSilage').get('sellingPricePerCent') * model.X10 + vals.get('hayfieldsOnHay').get('onFeed') * vals.get('hayImprovedHayfieldsAndPastures').get('sellingPricePerCent')* model.X11 + vals.get('hayfieldsOnSilage').get('onFeed') *vals.get('haylageImprovedHayfieldsAndPastures').get('sellingPricePerCent') * model.X12 +
                      vals.get('pasturesOnGreenFodder').get('onFeed') * vals.get('haylageNaturalHayfieldsAndPastures').get('sellingPricePerCent') * model.X13 + vals.get('pasturesOnSilage').get('onFeed') * vals.get('greenFodderNaturalHayfieldsAndPastures').get('sellingPricePerCent') * model.X14 + vals.get('concentrates').get('price') * model.X40 +
                      vals.get('silo').get('price') * model.X41 + vals.get('greenFodder').get('price') * model.X42 + vals.get('hay').get('price') * model.X43 + vals.get('haylage').get('price') * model.X44 +
                      vals.get('straw').get('price') * model.X45 + vals.get('youngCattle').get('livestock') * vals.get('youngCattle').get('productivity') *vals.get('meat').get('sellingPricePerCent') + vals.get('milk').get('sellingPricePerCent') * model.X50 == model.X49)
# по площади зерновых min
    model.constraints.add(model.X1 + model.X2 + model.X3 >= 0.4 * vals.get('arableLand'))                                             

# по площади зерновых max
    model.constraints.add(model.X1 + model.X2 + model.X3 <= 0.6 * vals.get('arableLand'))

# # по площади озимых min
    model.constraints.add(0.75 * model.X1 - 0.25 * model.X2 - 0.25 * model.X3 >= 0)
# # по площади озимых max
    model.constraints.add(0.6*model.X1-0.4 * model.X2-0.4*model.X3 <= 0)
# по площади зернобобовых min
    model.constraints.add(model.X3 >= 0.07 * (model.X1 + model.X2 + model.X3))
# по площади зернобобовых max
    model.constraints.add(model.X3 <= 0.1 * (model.X1 + model.X2 + model.X3))
# Решение модели
    result = solver.solve(model, tee=False)
    res = []
# Проверка результата
    #if result.solver.termination_condition == TerminationCondition.infeasible:
        #print("Model is infeasible")
    #elif result.solver.termination_condition == TerminationCondition.optimal:
        #print("Optimal solution found")
        #print("Результаты оптимизации:")
        #print(f"Значение целевой функции: {model.obj()}")
        #print("Значения переменных:")
    for var in model.component_data_objects(Var, active=True):
            #print(f"{var} = {var.value}")
        res.append(var.value)
    #else:
        #print(f"Solver terminated with condition: {result.solver.termination_condition}")
    return res

# Функция для вывода ограничений
def print_constraints(model):
    for i, constraint in enumerate(model.constraints):
        expr = model.constraints[i + 1].expr
        if model.constraints[i + 1].has_ub():
            print(f"{expr} <= {model.constraints[i + 1].upper}")
        if model.constraints[i + 1].has_lb():
            print(f"{expr} >= {model.constraints[i + 1].lower}")
        if value(model.constraints[i + 1].lower) == value(model.constraints[i + 1].upper):
            print(f"{expr} == {model.constraints[i + 1].lower}")

#print_constraints(model)
