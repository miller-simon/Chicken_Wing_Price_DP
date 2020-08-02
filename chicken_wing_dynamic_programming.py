price_dict = {}
price_dict[4] =  4.55
price_dict[5] =  5.7
price_dict[6] =  6.8
price_dict[7] =  7.95
price_dict[8] =  9.10
price_dict[9] =  10.2
price_dict[10] =  11.35
price_dict[11] =  12.50
price_dict[12] =  13.6
price_dict[13] =  14.75
price_dict[14] =  15.9
price_dict[15] =  17.0
price_dict[16] =  18.15
price_dict[17] =  19.3
price_dict[18] =  20.4
price_dict[19] =  21.55
price_dict[20] =  22.7
price_dict[21] =  23.8
price_dict[22] =  24.95
price_dict[23] =  26.1
price_dict[24] =  27.25
price_dict[25] =  27.8
price_dict[26] =  28.95
price_dict[27] =  30.1
price_dict[28] =  31.2
price_dict[29] =  32.35
price_dict[30] =  33.5
price_dict[35] =  39.15
price_dict[40] =  44.8
price_dict[45] =  50.5
price_dict[60] =  67.0
price_dict[70] =  78.3
price_dict[80] =  89.1
price_dict[90] =  100.45
price_dict[100] =  111.25
price_dict[125] =  139.0
price_dict[150] =  166.85
price_dict[200] =  222.5

optimal_price = [100000] * 200
for key in price_dict:
    optimal_price[key - 1] = price_dict[key]

optimal_order = [[]] * 200
for key in price_dict:
    optimal_order[key - 1] = [key]


#initialize all orders under 201
for i in range(4, 201):
    if i not in price_dict:
        optimal_price[i - 1] = 100000
        optimal_order[i - 1] = [*optimal_order[3], *(optimal_order[i-5])]


for i in range(4,201):
    for j in range(i, 201):
        if i + j < 201 and ((optimal_price[i-1] + optimal_price[j-1]) < optimal_price[i + j -1]):
            optimal_price[i + j - 1] = optimal_price[i - 1] + optimal_price[j - 1]
            optimal_order[i + j - 1] = [*optimal_order[i - 1], *(optimal_order[j - 1])]
            optimal_order[i + j - 1].sort()

for i in range(4,201):
    if i in price_dict and price_dict[i] - optimal_price[i - 1] > 0:
        print('Wings: {:<7} Order: {:<30} Total Price: ${:<10.2f} Savings: ${:<10.2f}'.format(i, str(
            optimal_order[i - 1]).lstrip('[').rstrip(']'), optimal_price[i - 1], price_dict[i] - optimal_price[i - 1]))
    else:
        print('Wings: {:<7} Order: {:<30} Total Price: ${:<10.2f}'.format(i, str(
            optimal_order[i - 1]).lstrip('[').rstrip(']'), optimal_price[i - 1]))