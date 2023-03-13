## Misc - Old Habits DIe Hard
> We found this zip file but its encrypted so we can't read the contents. Do you think you could crack it?
> 
> Developed by ihanna2

We were given an encrypted [zip](code/Encryptedfile.zip) and [wordlist](code/wordlist.txt). Based on the challenge description, we should crack the password. Using this [tutorial](https://linuxconfig.org/how-to-crack-zip-password-on-kali-linux) on the internet, I installed `fcrackzip` in Kali Linux to brute force the zip password using the wordlist.

Use this command `fcrackzip -u -D -p wordlist.txt Encryptedfile.zip` and brute force the password, we got that the password was <br />
![password](assets/Screenshot%202023-03-13%20114749.png) <br />

Then, I unzip the encrypted zip file and got [this file](code/Decrypted_Flag.txt) <br />
![unzip](assets/Screenshot%202023-03-13%20120509.png) <br />

Easy we cat the file and got that the flag was:
```
nicc{P@$$w0rd_l!$t$}
```