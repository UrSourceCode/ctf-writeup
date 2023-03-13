## Steg - plainsight
> this 󠁮󠁩󠁣is 󠁣󠁻󠀰just 󠁲󠁟󠀱a 󠀵󠁟󠀱simple 󠀷text file

In this challenge we were not given any clue, only the string. I copied the string to notepad and get something interesting <br />
![strings](assets/Screenshot%202023-03-13%20145933.png) <br />

I guess that was unicode letter that cannot display in some text editor, so after surfing some converter tools, I found this [ascii to utf-8 tools](https://onlineutf8tools.com/convert-ascii-to-utf8). <br />

And the result was
```
this nicis c{0just r_1a 5_1simple 7}text file
```

So, I remove the simple text and its space and got the flag:
```
nicc{0r_15_17}
```