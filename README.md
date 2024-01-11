# work in progress

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/6f6c72c3-e357-4116-b191-6b647edfa518)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/1116ff88-59f6-4291-b046-e8c483decc93)


# dummy train data

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/9ae3c456-5f57-4909-b83e-356f71d4d3b6)
created by signals.py

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/14ed53ea-bea3-4ee6-869d-9e6d3ede1635)

# dummy station data::

### populating from excel to postgres via python script; in build django file:: myapp/management/commands/populate_myapp_station.py 
python manage.py populate_myapp_station (django automatically created it)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/3f26c01a-b359-421f-b1dc-5e6dd134019f)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/5c0feaa4-537c-4319-885e-e9475fe1f462)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/aff43a63-26e7-47c1-8dc7-5f69569a177a)

admin can add stations and then select trainnumber via one to many relationship; many station one train
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/1f68c193-90a3-4d2a-a5fe-836e1a767a66)

# search for train from train number and it will display list of multiple stations

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/8954a9a3-6b9d-44a9-884c-8bc24cc9c1f4)


## implemented From-to destination.

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/ef56cc52-64de-43be-a68a-bad26ded0f79)

## User registeration and login

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/b3549459-974a-4eb5-9470-7ed30dd67904)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/73924ff4-ffc1-4d3b-a20d-27643b5e3783)

## profile and wallet system added
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/5a174301-5c60-4673-8a24-2815704c030d)

## Booking models (was a challenging one for me)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/b96ba347-9bcd-4bed-bad1-0962ddf20f62)

let say we will book 2AC 37 available

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/aba1b221-4b37-4481-9918-49a0af2c2f1e)

used atomicity (all or nothing); django built in function
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/e98b312e-746e-40ca-945a-fdf1331fbad2)

currently basic css 
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/7389e2b4-8436-4617-b5f3-56c0e86e9e0c)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/740ba715-9acf-4b42-9e31-8aeffd25deae)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/ad49beca-f8c8-4bd9-9579-33b0584e927a)

after successfull payment user redirected to myticket page, wallet money deducted, seats updated in our case subtracted by 2 for train 1010 Ac

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/ed67f764-3b14-4acb-915d-07bb3dcc3cc7)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/d11530d6-a98a-4b82-80f1-114a2f082502)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/dd4821b6-cd81-49c6-b8e4-64ff88813880)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/2efd5594-dbf7-4c6c-b4b4-632e426eaec7)

==== 

As of 8 jan  [4jan to 8jan ] ; Deadline approached :( will add more in future, for the task judgement i have included most of the functionality

==
<br>
Todos: 2 remaining
1. Mail, PDF and Allauth
2. Cancellation
3. Live Train status <br>
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/c19685b5-43c3-4887-b598-26e52f2a777a) <br>
in def self im taking instance as passenger-name-createdby<br>
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/81df86dc-ea7b-4139-85d5-843da78cc4b0) <br>
if admin wants to cancel a ticket he check the checkbox <br>
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/4836aebe-fe5c-4dab-94e9-f6c2e8ceb241) <br>
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/04c3f7aa-bbc2-4b58-84ae-4fe0b74dc0da)

## added edit functionality for passenger information
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/3089d644-b27e-49ab-b3e2-d766fa4e2a15)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/c7cd3d06-6ae4-4840-a304-1804cfb3e7bf)

## Successfully added search and filter by data :)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/e0290be6-e74f-401b-9bdd-97af780d1ca1)
input the date get the day from date and simply filter in ORM
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/8823784d-03d5-43cd-92b5-91ff28389438)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/ccff6e6d-219c-4a01-acb8-2564543967ab)

## added export  option for Passenger Model, so that admin can download a excel view.

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/7b2f337b-66fb-4387-897c-6e20f5c9ed1e)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/106da77b-1c5f-4537-8b72-0669bc58ea48)


#### Yeah want to add more but i should also respect the deadline so now i will dockerise it and deploy. (i feel i have something to show probably 80/100). #trains
