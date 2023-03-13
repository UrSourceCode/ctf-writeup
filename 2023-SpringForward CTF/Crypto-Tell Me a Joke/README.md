## Crypto - Tell Me a Joke
> I asked ChatGPT to tell me a joke, but it's encoded. Can you figure out what it is?
> 
> V2h5IGRpZCB0aGUgdG9tYXRvIHR1cm4gcmVkPwoKQmVjYXVzZSBpdCBzYXcgdGhlIHNhbGFkIGRyZXNzaW5nIQ==
>
> Format: nicc{words can be spaced}
>
> Developed by ch0p

This challenge is basically a sentence encoded with base64. Using [Base64 Decoder](https://www.base64decode.org/) and followed the flag format, I found that the flag was
```
nicc{Why did the tomato turn red? Because it saw the salad dressing!}
```