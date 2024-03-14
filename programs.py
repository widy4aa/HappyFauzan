from Quotes import api
import time

quotes = api()

while True :
    print("halo fauzan ")
    time.sleep(2)
    askcui = input("bagaimana dengan kabarmu : ")
    print("emmm begituu...")
    time.sleep(2)
    ask = input('apakah kamu mau dengar quotes dariku (Y/N): ')
    ask = ask.lower()
    if ask== "y":
        time.sleep(2)
        print(quotes["quote"])
        time.sleep(10)
    else :
        break