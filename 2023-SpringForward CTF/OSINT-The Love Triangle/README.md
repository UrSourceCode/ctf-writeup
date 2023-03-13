## OSINT - The Love Triangle

> There's rumors of a love triangle on campus and we hate not knowing things.
> 
> All we know is that it might be between some faculty or maybe staff or maybe students who just really can't let go of the past.
> 
> The only two solid pieces of information we got were "heroic_tom" and witches, which really doesn't make sense.
> 
> Developed by royCardigan

We were given a hint to check their social media, so I go first to instagram and search username named `heroic_tom` and found hexadecimal in his bio. <br />
![bio](assets/Screenshot%202023-03-13%20130941.png) <br />

Then I convert using [hexadecimal to ASCII tools](https://www.duplichecker.com/hex-to-text.php) and got a string encoded with Base64
```
YmF5bC1iYXItZmdubGY=
```

Then, I decode using [Base64](https://www.base64decode.org/) decoder and got the flag:
```
nicc{bayl-bar-fgnlf}
```
