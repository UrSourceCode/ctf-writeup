## OSINT - Ow, my head
> We went out last night to party during spring break, or was it a few nights from now or the other day we went out? Look, I don't know. It's spring break. All I know is this dude Arbys was buying drinks and then next thing I know: Bam, wake up and everybody's all weird. Can you come get me? Anna's god knows where, but I'll help you find her if you find me. No idea where I am though. Here's a pic of a super shady atm by the bar I woke up in front of. Everything's closed but I think we sang here last night.
> 
> Find when I created this and where I am. No spaces, no cases. flag format nicc{yyyymmddbarname}
> Developed by Cyb3rSw0rd

In this challenge we were given an [image](code/totallysafeatm.jpg) of ATM. Using exiftool, we got some information from the metadata: <br />
![metadata](assets/Screenshot%202023-03-13%20122040.png) <br />

Then I go to [GPS Coordinates Finder](https://gps-coordinates.org/) based on GPS positions from that metadata, and I got <br />
![loc](assets/Screenshot%202023-03-13%20122536.png) <br />

I go to google maps to find the bar name, using street view I got: <br />
![planetrose](assets/Screenshot%202023-03-13%20124104.png)

Based on that information, I got the flag:
```
nicc{20330316planetrose}
```