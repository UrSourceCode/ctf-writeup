## Web - NICC 98
> Here’s an archive of the original NICC website from when we used to be hosted by Geocities! (Cut us some slack, it was 1998.)
> 
> Developed by drodrii
>
> https://nicc-nicc-98.chals.io/nicc98.html

In this challenge there is a web. And from hint I got an information that the flag maybe can be found at the JavaScript. So, I inspect the element, go to source, and check it's JavaScript <br />
![js](assets/Screenshot%202023-03-13%20150712.png)

And found a string encoded with Base64, using [Base64 Decoder](https://www.base64decode.org/), I found that the flag was

```
nicc{flip_th3_script}
```