## Steg - Great Scott
> Decode the coded message in the jpg file!
> 
> Developed by theamazins17

In this challenge we were given a [jpg file](code/great-scott.jpg). Using `strings`, `objdump`, and `binwalk`, I don't really found any clue. So using the powerful google, I search for some steg tools and found [steghide](https://github.com/StefanoDeVuono/steghide). <br />

So let's use this tools, <br />
![flagg](assets/Screenshot%202023-03-13%20144539.png) <br />

The flag was:
```
nicc{It's_All_About_the_Mets!}
```