import datetime, random, pandas
import pandas as pd
base_value = int(input("Current Balance\n"))
week = 0
month = 4
estimated_earnings = input("Estimated Earnings (i.e 350-380 or 350): \n")



if "-" in estimated_earnings:
    est = True
else:
    est = False
    estimated_earnings = int(estimated_earnings)
expenses = int(input("Expenses\n"))
e_week = int(input("Week\n"))
bankrupt = False
weeks = []
balances = []
once_bankrupt = False
while week < e_week:
    if week == 0:
        base_value -= 50
    if est == False:
        base_value += estimated_earnings
    elif est == True:
        base_value += int(estimated_earnings.split("-")[random.randint(0, 1)])
    base_value -= expenses
    balances.append(base_value)
    u = datetime.datetime.strptime("2019-09-01", "%Y-%m-%d")
    d = datetime.timedelta(days=week * 7)
    t = u + d
    weeks.append(t.strftime("%B %Y %A"))
    if base_value < 0:
        bankrupt = True
        once_bankrupt = True
        print("You'll be bankrupt on %s or in %d | balance: €%d" % (t.strftime("%x"), week, base_value))
    elif base_value > 1:
        bankrupt = False
        if once_bankrupt == True:
            print("You've bounced back on %s and your balance in %d weeks will be €%d " % (t.strftime("%x"), week, base_value))
    week += 1

u = datetime.datetime.strptime("2019-09-01", "%Y-%m-%d")
d = datetime.timedelta(days=week*7)
t = u + d
if bankrupt == False:
    print("Your balance on %s or in %d weeks will be €%d | " % (t.strftime("%x"), week, base_value))

analytics = {"Date": weeks, "Balance": balances}
dataframe = pd.DataFrame(data=analytics)
dataframe.to_excel("yourstruly.xlsx")
