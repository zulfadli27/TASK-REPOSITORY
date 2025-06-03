# To-Day Calculator Apps


----
## Have you ever wondering what is the day when you are born?<br>Or, have you ever wonder what day is it when historical events happen? <br><br>Don't worry, we got it for you!

With this app, to-day calculator, you can solve your problem above and even more,
<br>we have 2 main features:
1. translate given date to its day of the week
2. inform about leap year from that date for 2 years ago and later


#
So, how to make use of this app? here's the manual:
1. you need python installed in your PC/Laptop (Yes, currently we only available in desktop)
2. download this file (attached below)
3. run the app.py, then input your choosen date (for now its only support gregorian calender)
4. voila! now you know what day of the week it is from that date

#
how to download<br> 
![how to download](https://github.com/doni-wahyudi/TASK-REPOSITORY/blob/to-day_calculator/assets/how%20to%20download.png)
#
open cmd<br> 
![open cmd](https://github.com/doni-wahyudi/TASK-REPOSITORY/blob/to-day_calculator/assets/open%20cmd.png)
#
run app.py<br>
![run app](https://github.com/doni-wahyudi/TASK-REPOSITORY/blob/to-day_calculator/assets/run%20app.py.png)

---
In case you wonder how this apps working, here is the flow of the app:

![flow image](https://github.com/doni-wahyudi/TASK-REPOSITORY/blob/to-day_calculator/assets/flow%20process%20to-day%20calculator.jpg)

---
For the technical aspect, here is the explanation:
1. app.py as orchestrator<br>
   it will call input_validation, leap_year, and zellers_congruence module.
2. input_validation module<br>
   it will check are the given input satisfy the condition from its parameter range, which is date ranged from 1-31, month 1-12, and year greater than 0, if the user input out of its range, it will give feedback to user to re-input again until the value is correct.
3. leap_year module<br>
   it will calculate and produce result which year is leap year from 2 years ago to 2 years later, based on criteria: the year is divisible by 4 and not divisible by 100, or the year is divisible by 400
4. zellers_congruence module<br>
   it will calculate given date using zeller's congruence algorithm (for gregorian calendar) and giving the output mapped to day of the week. here's the reference from wikipedia: [zeller's congruence](https://en.wikipedia.org/wiki/Zeller%27s_congruence)

---
That's the wrap of this app, 
<br>hope we can make more progress and making more apps that could benefit us, 
<br>and hopefully this first project will be the first step of us in Eco Techno Leader program towards AI Engineering.

Thankyou so much!
