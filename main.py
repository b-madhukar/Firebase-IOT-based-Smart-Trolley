import sys,time
import network
import ufirebase as firebase
from machine import Pin
import read

def wlan_connect(ssid,pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
    
wlan_connect('SSID', 'PWD')
led=Pin(14,Pin.OUT)
firebase.put('https://firebaseio.com/Prod1_Qty',0)
count=0
while True:
    res=read.do_read()
    if(res==553):
        count=count+1
        firebase.put('https://firebaseio.com/Prod1_Qty',count)
    if(res==110 and count > 0):
        count=count-1
        firebase.put('https://firebaseio.com/Prod1_Qty',count)
    Prod1_Qty=int(firebase.get('https://firebaseio.com/Prod1_Qty'))
    Prod1_PerUnit=float(firebase.get('https://firebaseio.com/Prod1_PerUnit'))
    Prod1_Price=Prod1_Qty*Prod1_PerUnit
    firebase.put('https://firebaseio.com/Prod1_Price',Prod1_Price)
    Prod2_Qty=int(firebase.get('https://firebaseio.com/Prod2_Qty'))
    Prod2_PerUnit=float(firebase.get('https://firebaseio.com/Prod2_PerUnit'))
    Prod2_Price=Prod2_Qty*Prod2_PerUnit
    firebase.put('https://firebaseio.com/Prod2_Price',Prod2_Price)
    Total=Prod1_Price+Prod2_Price
    firebase.put('https://firebaseio.com/Total',Total)
    print(Prod1_Qty,Prod1_PerUnit,Prod1_Price)
    print(Prod2_Qty,Prod2_PerUnit,Prod2_Price)
    print(Total)

