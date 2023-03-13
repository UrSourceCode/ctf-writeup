## Forensics-Say Cheese
> This photo was given to us and we believe this man may play an important part into all this craziness. Can you find out what the make and model of the device used to take the selfie was? Flag will be in this format
> 
> nicc{MakeWord1_MakeWord2_ModelWord1_ModelWord2}
> 
> Developed by ihanna2

We were given a .jpg [file](code/Selfie.jpg) and a flag format. Using `exiftool` I tried to get the metadata. <br />

![metadata](assets/Screenshot%202023-03-13%20104246.png) <br />

Based on the flag format, the flag was:
```
nicc{Security_Camera_Kmart_Special}
```
