'''
Printer_charge V1.2
Lee Zhi Wei
14/7/22
'''
def calculate_charge(pages):
    rate1 = 0.03
    rate2 = 0.02
    rate3 = 0.01
    if pages <= 100:
        cost = rate1 * pages
    elif 100 < pages <= 300:
        cost = (100 * rate1) + ((pages-100) * rate2)
    elif pages > 300:
        cost = (100 * rate1) + (200 * rate2) +((pages - 300) * rate3)
    return cost
def calculate_gst(cost):
    withgst = cost * 1.07
    return withgst
print("{:<10}{:<10}{:<10}".format("Pages","Charge($)","Include gst($)"))
x = 0
while x <= 500:
    print("{:<10}{:<10.2f}{:<10.2f}".format(x,calculate_charge(x),calculate_gst(calculate_charge(x))))
    x += 50
