## Beginner - baby-re

### Description

> baby-re
> 
> 50
> 
> Reverse iQlusion#4057
> 
> Just a wee little baby re challenge.

### Exploit

In this challenge, we were given a [file](chall/baby-re). To find out the information of the file, I used the file command and found that the file is  `ELF 64-bit LSB pie executable`.

![file-information](assets/file-information.png).

I opened the file using `Ghidra`, then decompile it.
![ghidra-decompile](assets/ghidra-decompile.png)

Because at the `FUN_00101155` function it says that the flag would be elsewhere, I scrolled down and got the flag.

![flag](assets/flag.png)

So the flag was
```
wctf{Oh10_Stat3_1s_Smelly!}
```