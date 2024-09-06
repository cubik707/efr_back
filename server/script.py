import sys
import json
import model
if __name__ == "__main__":
    with open('input.json', 'r') as file:
        data = json.load(file)
    calculations = model.solve(data)
    if calculations[32]==None:
      calculations[32]=0
    module = data.get('cows').get('livestock')
    if(module == 0):
       module = 1
    module1 = data.get('youngCattle').get('livestock')
    if(module1 == 0):
       module1 = 1
    jsonfile = {
       "winterGrainsArea": calculations[0],
       "springGrainsArea": calculations[1],
       "pulsesArea": calculations[2],
       "rapeArea": calculations[3],
       "cropResiduesArea": calculations[4],
       "hayGrassHayArea": calculations[5],
       "haylageGrassHayArea": calculations[6],
       "greenFodderGrassHayArea": calculations[7],
       "annualGrassesGreenFodderArea": calculations[8],
       "cornOnSilageArea": calculations[9],
       "hayImprovedHayfieldsAndPasturesArea": calculations[10],
       "haylageImprovedHayfieldsAndPasturesArea": calculations[11],
       "haylageNaturalHayfieldsAndPasturesArea": calculations[12],
       "greenFodderNaturalHayfieldsAndPasturesArea": calculations[13],
       "additionalCowProductivity": calculations[14],
       "mainConcentratesCows": (calculations[15]+calculations[21])/module,
       "mainSilageCows": (calculations[16]+calculations[22])/module,
       "mainGreenFodderCows": (calculations[17]+calculations[23])/module,
       "mainHayCows": (calculations[18]+calculations[24])/module,
       "mainHaylageCows": (calculations[19]+calculations[25])/module,
       "mainStrawCows": (calculations[20]+calculations[26])/module,
       "additionalConcentratesCows": (calculations[15]+calculations[21])/module,
       "additionalSilageCows": (calculations[16]+calculations[22])/module * 0.2,
       "additionalGreenFodderCows": (calculations[17]+calculations[23])/module * 0.19,
       "additionalHayCows": (calculations[18]+calculations[24])/module * 0.45,
       "additionalHaylageCows": (calculations[19]+calculations[25])/module * 0.28,
       "additionalStrawCows": (calculations[20]+calculations[26])/module * 0.25,
       "mainConcentratesYoungCattle": calculations[27]/module1,
       "mainSilageYoungCattle": calculations[28]/module1,
       "mainGreenFodderYoungCattle": calculations[29]/module1,
       "mainhayYoungCattle": calculations[30]/module1,
       "mainhaylageYoungCattle": calculations[31]/module1,
       "mainStrawYoungCattle": calculations[32]/module1 or 0,
       "additionalConcentratesYoungCattle": calculations[27]/module1,
       "additionalSilageYoungCattle": calculations[28]/module1* 0.2,
       "additionalGreenFodderYoungCattle": calculations[29]/module1* 0.19,
       "additionalhayYoungCattle": calculations[30]/module1* 0.45,
       "additionalhaylageYoungCattle": calculations[31]/module1 * 0.28,
       "additionalStrawYoungCattle": calculations[32]/module1* 0.25 or 0,
       "concentrates": calculations[33],
       "silage": calculations[34],
       "greenFodder": calculations[35],
       "hay": calculations[36],
       "haylage": calculations[37],
       "straw": calculations[38],
       "concentratesToBuy": calculations[39],
       "silageToBuy": calculations[40],
       "greenFodderToBuy": calculations[41],
       "hayToBuy": calculations[42],
       "haylageToBuy": calculations[43],
       "strawToBuy": calculations[44],
       "nutritionForCows":calculations[45],
       "nutritionForYoungCattle":calculations[46],
       "revenue":calculations[47],
       "cost":calculations[48],
       "milk":calculations[49],
       "milkOnFeed":calculations[50],
       "milkSold":calculations[51]
    }
    print((calculations[15]+calculations[21])/700)
    with open('output.json', 'w') as json_file:
      json.dump(jsonfile, json_file, indent=4)
