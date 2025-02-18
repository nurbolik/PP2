import datetime
#1
print(datetime.date.today()-datetime.timedelta(days=5))

#2
print(f"yesterday - {datetime.date.today()-datetime.timedelta(days=1)}")
print(f"today - {datetime.date.today()}")
print(f"tomorrow - {datetime.date.today()-datetime.timedelta(days=-1)}")

#3
print(datetime.datetime.now().strftime("%c"))

#4
d=input('YYYY-MM-DD HH:MM:SS - ')
t=datetime.datetime.now()-datetime.datetime.strptime(d,'%Y-%m-%d %H:%M:%S')
print("seconds:",t.days*24*60*60+t.seconds)