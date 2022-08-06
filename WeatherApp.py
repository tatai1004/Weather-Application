from tkinter import*
from PIL import Image,ImageTk  #pip install pillow from cmd
import key
import time                    
import requests
class WeatherApp:
    def __init__(self,root):
        self.root=root
        #Weather layout size determining
        
        self.root.title("Weather")
        self.root.geometry("400x400+500+150")
        self.root.config(bg="seagreen")
        
        #Set icon for search button
        
        self.set_icon=Image.open("icons/search1.png")
        self.set_icon=self.set_icon.resize((20,20),Image.ANTIALIAS)
        self.set_icon=ImageTk.PhotoImage(self.set_icon)
        
        #Varible define
        
        self.var_search_city=StringVar()

        #Upper search buttons and icons setting
        
        title=Label(self.root,text="Weather-Checker",font=("gill sans mt",20,"bold",),bg="green",fg="black").place(x=0,y=0,relwidth=1,height=40)
        city_name=Label(self.root,text="Enter City:",font=("ariel",15,"bold"),bg="green",fg="maroon",anchor="w",padx=5).place(x=0,y=40,relwidth=1,height=33)
        city_type=Entry(self.root,textvariable=self.var_search_city,font=("ariel",10,"bold"),bg="white",fg="purple").place(x=108,y=43,width=150,height=25)
        search_button=Button(self.root,cursor="hand2",image=self.set_icon,bd=0,command=self.weather_data).place(x=258.48,y=43,width=38,height=25)
        

        #Show weather data
        
        self.show_city=Label(self.root,font=("ariel",15,"bold"),bg="seagreen",fg="black")
        self.show_city.place(x=0,y=80,relwidth=1,height=20)
        
        self.show_icon=Label(self.root,font=("ariel",15,"bold"),bg="seagreen",fg="black")
        self.show_icon.place(x=0,y=105,relwidth=1,height=100)
        
        self.show_temp=Label(self.root,font=("ariel",15,"bold"),bg="seagreen",fg="midnightblue")
        self.show_temp.place(x=0,y=210,relwidth=1,height=20)
        
        self.show_wind=Label(self.root,font=("ariel",15,"bold"),bg="seagreen",fg="purple")
        self.show_wind.place(x=0,y=235,relwidth=1,height=20)

        self.show_sunrise=Label(self.root,font=("ariel",15,"bold"),bg="seagreen",fg="gold")
        self.show_sunrise.place(x=0,y=285,relwidth=1,height=20)

        self.show_sunset=Label(self.root,font=("ariel",15,"bold"),bg="seagreen",fg="brown")
        self.show_sunset.place(x=0,y=310,relwidth=1,height=20)

        self.show_weather_description=Label(self.root,font=("ariel",12,"bold"),bg="seagreen",fg="mediumblue")
        self.show_weather_description.place(x=0,y=340,relwidth=1,height=20)

        #Display error
        
        self.show_error=Label(self.root,font=("ariel",15,"bold"),bg="seagreen",fg="red")
        self.show_error.place(x=0,y=260,relwidth=1,height=20)

        #Developer credit
        
        dev_credit=Label(self.root,text="Developed by- Zidane",font=("ariel",10,"italic"),bg="green",fg="black",pady=5).pack(side=BOTTOM,fill=X)

        #Weather data load from API
        
    def weather_data(self):
        api_key=key.api_key
        weather_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search_city.get()}&appid={api_key}"

        #Show city name, country name, icons, temp in c and f, wind condition, sunset and sunrise
        
        if self.var_search_city.get()=="":
            
             self.show_city.config(text="")
             
             self.show_icon.config(image="")
             
             self.show_temp.config(text="")
             
             self.show_wind.config(text="")
             
             self.show_sunrise.config(text="")
             
             self.show_sunset.config(text="")

             self.show_weather_description.config(text="")
             
             self.show_error.config(text="Invalid City Name!")
             
             self.show_error.config(text="City is required to show weather data!")
            
        else:    
            show_weather_data=requests.get(weather_url)
            if show_weather_data:
                json=show_weather_data.json()
                city_data=json["name"]
                country_data=json["sys"]["country"]
                icon_data=json["weather"][0]["icon"]
                temp_in_c=json["main"]["temp"]-273.15
                temp_in_f=(json["main"]["temp"]-273.15)*9/5+32
                wind_data=json["weather"][0]["main"]
                sunrise_data=time.strftime("%I:%M:%S", time.gmtime(json["sys"]["sunrise"]-23400))
                sunset_data=time.strftime("%I:%M:%S", time.gmtime(json["sys"]["sunset"]-23400))
                weather_description_data=json["weather"][0]["description"]
                
                #Display country
                
                self.show_city.config(text=city_data+" , "+country_data)
                
                #Weather Icons loading
                
                self.set_icon2=Image.open(f"icons/{icon_data}.png")
                self.set_icon2=self.set_icon2.resize((100,100),Image.ANTIALIAS)
                self.set_icon2=ImageTk.PhotoImage(self.set_icon2)

                self.show_icon.config(image=self.set_icon2)

                #load the degree icon
                
                degree=u"\N{DEGREE SIGN}"

                #Display temp, wind, sunset, sunrise and weather description
                
                self.show_temp.config(text=str(round(temp_in_c,2))+degree+" C | "+str(round(temp_in_f,2))+degree+" F")
                self.show_wind.config(text=wind_data)
                self.show_sunrise.config(text="Sunrise: "+sunrise_data)
                self.show_sunset.config(text="Sunset : "+sunset_data)
                self.show_weather_description.config(text="Weather Description: "+weather_description_data)

                self.show_error.config(text="")
                
            else:
                self.show_city.config(text="")
                
                self.show_icon.config(image="")
                
                self.show_temp.config(text="")
                
                self.show_wind.config(text="")
                
                self.show_sunrise.config(text="")
                
                self.show_sunset.config(text="")

                self.show_weather_description.config(text="")
                
                self.show_error.config(text="Invalid City Name!")
            
            
root=Tk()
obj=WeatherApp(root)
root.mainloop()
