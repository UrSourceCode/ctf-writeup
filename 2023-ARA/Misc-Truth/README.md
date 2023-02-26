## Misc - Truth

We were given a locked PDF File but there is no information about the password. So I search using `brute force PDF Password` keyword on google and found [this website](https://ourcodeworld.com/articles/read/939/how-to-crack-a-pdf-password-with-brute-force-using-john-the-ripper-in-kali-linux). <br />
Next, I followed the instruction to clone, make and configure the tools on my Kali Linux WSL. Then, I copied the PDF file to `run` directory.
![pdf](assets/Screenshot%202023-02-26%20131537.png) <br />
The next step is use this command to generate PDF hash file:
```sh
pdf2john.pl Truth.pdf > pdf.hash
```
The tools generated a PDF hash file below:
![pdf2](assets/Screenshot%202023-02-26%20131758.png) <br />
To did brute forcing password using this tools I use:
```
./john pdf.hash
```
And the tools will brute forcing the password for some moments using their wordlist. After the process was finished, we can show the password using
```
./john --show pdf.hash
```
command and here is the result:
![pass](assets/Screenshot%202023-02-26%20132904.png) <br /> <br />
Based on the result, the password was `subarukun`. After the password was succesfully leaked, I opened the file and read the instructions. Based on the instructions we should erase the title then find uppercase letter, so i used this python code:
```py
result = ''.join(c for c in text if c.isupper())
```
or you can run [this code](isUpper.py). <br />
Based on that code, the result was:
![res](assets/Screenshot%202023-02-26%20134108.png). <br />
Then, followed the challenge's format, the flag should be:
```
ARA2023{SOUNDS_LIKE_FANDAGO}
```