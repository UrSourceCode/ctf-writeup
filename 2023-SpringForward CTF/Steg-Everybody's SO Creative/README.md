## Steg - Everybody's SO Creative
> Ugh, why do they keep trying to make good music sound bad? There's NO way this is what the DJ intended to play. I can't believe they had the audacity to do this!
>
> Developed by Cyb3rSw0rd

In this challenge we were given a [wav music file](code/isthispopmusic.wav). Using `Audacity` an open-source digital audio editor and recording application software, we opened the file and opened the spectogram: <br />
![open](assets/Screenshot%202023-03-13%20141102.png) <br />
then I found: <br />
![spectogram](assets/Screenshot%202023-03-13%20141248.png) <br />

I got a hexadecimal
```
57 68 40 74 5F 52 40 6E 63 31 64 5F 54 31 6D 33 5F 62 30 6D 62
```

then I used [hexadecimal to ASCII converter tools](https://www.duplichecker.com/hex-to-text.php) and got this flag:
```
nicc{Wh@t_R@nc1d_T1m3_b0mb}
```
