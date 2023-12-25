import tkinter as tk
import time
import requests
from tkinter import *
import mysql.connector as c
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
from PIL import Image, ImageTk

def getWeather(canvas):
    try:
        city = textField.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=754d2ef2ba3f8f787ab3cdc68f8b4d9d"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        feels_like = int(json_data['main']['feels_like'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        visibility = float(json_data['visibility']/1000)
        sunrise = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunrise'] + 19800))
        sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset'] + 19800))
        icon_name = json_data['weather'][0]['icon']

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        res = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        IST = pytz.timezone(res)
        datetime_ist = datetime.now(IST)
        clock = datetime_ist.strftime('%d:%m:%Y'+'\n'+ '%H:%M:%S')
        
        result1 = str(temp) + " °C" 
        result2 = condition + " | " + "FEELS LIKE: "+ str(feels_like) + " °C"
        text1 = str(min_temp) +" °C"
        text2 = str(max_temp) +" °C"
        text3 = str(pressure) +" hPa"
        text4 = str(humidity) +" %"
        text5 = str(wind) +" m/s"
        text6 = str(visibility) +" KM"
        text7 = str(sunrise) + " IST"
        text8 = str(sunset) + " IST"
        text9 = "Tap Here"
        text10 = "Past 5 Days"+ "\n" + city + "'s Weather"+"\n"+"Details"
        result3 = ("Current " +city+"'s Weather At" "\n" + clock)

        label1.config(text = result1)
        label2.config(text = result2)
        label3.config(text = result3)
        label12.config(text = text9)
        label13.config(text = text10)

        mt.config(text=text1)
        mxt.config(text=text2)
        p.config(text=text3)
        h.config(text=text4)
        wp.config(text=text5)
        vi.config(text=text6)
        sr.config(text=text7)
        ss.config(text=text8)

    except Exception as e:
         messagebox.showwarning("Weather App","Entered City "+city+" Not Found"+"\n"+"    Please Enter A Valid City  ", )

    open_image(icon_name)
        
canvas = tk.Tk()
canvas.geometry("760x650")
canvas.title("Weather App")
canvas.resizable(False, False)
imgicon = PhotoImage(file = './Weather_icons/app logo.png')
canvas.iconphoto(False, imgicon)


m = Menu(canvas)
menubar = Menu(m, tearoff = 0)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Home', menu = file)

location = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Location', menu = location)
location.add_command(label ='Manage Location', command = None)
location.add_command(label ='Search Different Location', command = None)
location.add_command(label ='Search Location On Map', command = None)
location.add_separator()
location.add_command(label ='Close', command = location.destroy)

unit_setting = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Unit Setting', menu = unit_setting)
sub_menu = Menu(unit_setting, tearoff=0)
unit_setting.add_cascade(label='Temperature', menu=sub_menu)
sub_menu.add_command(label ='°C', command = None)
sub_menu.add_command(label ='°F', command = None)
sub_menu2 = Menu(unit_setting, tearoff=0)
unit_setting.add_cascade(label='Pressure', menu=sub_menu2)
sub_menu2.add_command(label ='mBar', command = None)
sub_menu2.add_command(label ='hpa', command = None)
sub_menu2.add_command(label ='psi', command = None)
sub_menu3 = Menu(unit_setting, tearoff=0)
unit_setting.add_cascade(label='Wind Speed', menu=sub_menu3)
sub_menu3.add_command(label ='m/s', command = None)
sub_menu3.add_command(label ='km/h', command = None)
sub_menu3.add_command(label ='mph', command = None)
sub_menu3.add_command(label ='kt', command = None)
sub_menu4 = Menu(unit_setting, tearoff=0)
unit_setting.add_cascade(label='Visibility', menu=sub_menu4)
sub_menu4.add_command(label ='Meter', command = None)
sub_menu4.add_command(label ='Kilometer', command = None)
sub_menu4.add_command(label ='Mile', command = None)
sub_menu5 = Menu(unit_setting, tearoff=0)
unit_setting.add_cascade(label='Time Format', menu=sub_menu5)
sub_menu5.add_command(label ='12 hours', command = None)
sub_menu5.add_command(label ='24 hours', command = None)
unit_setting.add_separator()
unit_setting.add_command(label ='Close', command = unit_setting.destroy)
  
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='About Us',command = None)
help_.add_command(label ='Contact Us', command = None)
help_.add_separator()
help_.add_command(label ='About API', command = None)

canvas.config(menu=menubar)

searchbox = PhotoImage(file = './Weather_icons/Search box.png')
Label(canvas,image=searchbox).place(x=28, y=16, bordermode="inside")

textField = tk.Entry(canvas, justify='center', width = 17, borderwidth='0', font =('Calibri', 25, 'bold'))
textField.pack(pady = 10)
textField.config(bg="Black", fg="white")
textField.focus()
textField.place(x=80, y=33)
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=('Garamond', 45, 'bold'), fg='#ee666d')
label1.place(x=350, y=120)
label2 = tk.Label(canvas, font=('Garamond', 18, 'bold'), )
label2.place(x=315, y=190)
label3 = tk.Label(canvas, font=('arial', 10), anchor='e', justify=CENTER)
label3.pack(padx=1, pady=1)
label3.place(x=580, y=5)

box = PhotoImage(file='./Weather_icons/Bottom Box.png')
frame_myimage = tk.Label(image=box)
frame_myimage.pack()
frame_myimage.place(x=60, y=240)

label4 = tk.Label(canvas, text="Min Temp", font=('Bodoni MT', 15, 'bold'), fg="black")
label4.place(x=140, y=275)
label5 = tk.Label(canvas, text="Humidity", font=('Bodoni MT', 15, 'bold'), fg="black")
label5.place(x=140, y=345)
label6 = tk.Label(canvas, text="Wind Speed", font=('Bodoni MT', 15, 'bold'), fg="black")
label6.place(x=140, y=415)
label7 = tk.Label(canvas, text="  sunrise", font=('Bodoni MT', 15, 'bold'), fg="black")
label7.place(x=140, y=485)
label8 = tk.Label(canvas, text="Max Temp", font=('Bodoni MT', 15, 'bold'), fg="black")
label8.place(x=390, y=275)
label9 = tk.Label(canvas, text="Pressure", font=('Bodoni MT', 15, 'bold'), fg="black")
label9.place(x=393, y=345)
label10 = tk.Label(canvas, text="Visibility", font=('Bodoni MT', 15, 'bold'), fg="black")
label10.place(x=392, y=415)
label11 = tk.Label(canvas, text="  Sunset", font=('Bodoni MT', 15, 'bold'), fg="black")
label11.place(x=390, y=485)

mt = tk.Label(text="   ....", font=('Hadassah Friedlaender', 12), fg="black")
mt.place(x=155, y=300)
h = tk.Label(text="   ....", font=('Hadassah Friedlaender', 12), fg="black")
h.place(x=155, y=370)
wp = tk.Label(text="    ....", font=('Hadassah Friedlaender', 12), fg="black")
wp.place(x=155, y=440)
sr = tk.Label(text="      ....", font=('Hadassah Friedlaender', 12), fg="black")
sr.place(x=145, y=510)
mxt = tk.Label(text="    ....", font=('Hadassah Friedlaender', 12), fg="black")
mxt.place(x=405, y=300)
p = tk.Label(text="      ....", font=('Hadassah Friedlaender', 12), fg="black")
p.place(x=395, y=370)
vi = tk.Label(text="     ....", font=('Hadassah Friedlaender', 12), fg="black")
vi.place(x=397, y=440)
ss = tk.Label(text="      ....", font=('Hadassah Friedlaender', 12), fg="black")
ss.place(x=395, y=510)

img1 = PhotoImage(file = './Weather_icons/MinTemp.png')
Label(canvas,image=img1).place(x=90, y=280, bordermode="outside")
img2 = PhotoImage(file = './Weather_icons/Humidity.png')
Label(canvas,image=img2).place(x=90, y=350, bordermode="outside")
img3 = PhotoImage(file = './Weather_icons/WindSpeed.png')
Label(canvas,image=img3).place(x=90, y=417, bordermode="outside")
img4 = PhotoImage(file = './Weather_icons/Sunrise.png')
Label(canvas,image=img4).place(x=90, y=485, bordermode="outside")
img5 = PhotoImage(file = './Weather_icons/MaxTemp.png')
Label(canvas,image=img5).place(x=340, y=280, bordermode="outside")
img6 = PhotoImage(file = './Weather_icons/Pressure.png')
Label(canvas,image=img6).place(x=340, y=350, bordermode="outside")
img7 = PhotoImage(file = './Weather_icons/Visibility.png')
Label(canvas,image=img7).place(x=340, y=420, bordermode="outside")
img8 = PhotoImage(file = './Weather_icons/Sunset.png')
Label(canvas,image=img8).place(x=340, y=485, bordermode="outside")

def open_image(icon):
    img = ImageTk.PhotoImage(Image.open('./Weather_icons/'+icon+'.png'))
    label14.delete('all')
    label14.create_image(60,50, image=img)
    label14.image=img

def View(*args):
    main = textField.get()
    place = (main)
    
    window2=Toplevel(canvas)
    window2.geometry("810x150")
    window2.title('Past 5 Days Weather Record')

    mydb =c.connect(host="localhost", user="root", passwd="root", database="weather_project")
    mycursor = mydb.cursor()
    query = "Select * from past_weather where city = '%s'" % (place, )
    mycursor.execute(query)

    tree = ttk.Treeview(window2, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8", "c9", "c10" ), show='headings')
    tree.column("#1" , width=70, anchor=tk.CENTER)
    tree.heading("#1", text="Dates")
    tree.column("#2", width=120, anchor=tk.CENTER)
    tree.heading("#2", text="Weather Condition")
    tree.column("#3", width=80, anchor=tk.CENTER)
    tree.heading("#3", text="Min Temp")
    tree.column("#4", width=80, anchor=tk.CENTER)
    tree.heading("#4", text="Max Temp")
    tree.column("#5", width=70, anchor=tk.CENTER)
    tree.heading("#5", text="Pressure")
    tree.column("#6", width=65, anchor=tk.CENTER)
    tree.heading("#6", text="Humidity")
    tree.column("#7", width=80, anchor=tk.CENTER)
    tree.heading("#7", text="Wind Speed")
    tree.column("#8", width=70, anchor=tk.CENTER)
    tree.heading("#8", text="Visibility")
    tree.column("#9", width=85, anchor=tk.CENTER)
    tree.heading("#9", text="Sunrise")
    tree.column("#10", width=85, anchor=tk.CENTER)
    tree.heading("#10", text="Sunset")
    tree.pack()
    tree.place(x=1, y=1)

    rows = mycursor.fetchall()
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)
    mydb.close()

label12 = tk.Label(canvas, font=("Yu Gothic UI Semibold", 13), fg='red')
label12.place(x=605, y=350)

label13 = tk.Label(canvas, font=("Yu Gothic UI Semibold", 13), justify=CENTER)
label13.pack(padx=1, pady=1)
label13.place(x=575, y=380)
label13.config(fg="Black")
label13.bind("<Button-1>", View)

button = tk.Button(canvas, text="Exit",width=10, font=('Bodoni MT', 14), relief="raised", borderwidth=3, bg="#cccccc", command=canvas.destroy)
button.place(x=580, y=575)

label14 = tk.Canvas(canvas, highlightthickness=0,bg='#f0f0f0')
label14.place(relx=0.23, rely=0.21, relwidth=0.16, relheight=0.15)

canvas.mainloop()