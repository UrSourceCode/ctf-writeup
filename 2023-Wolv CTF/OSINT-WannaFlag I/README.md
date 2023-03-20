## OSINT - WannaFlag I

### Description

> WannaFlag I: An Introduction
> 
> 188
> 
> dree#0001 Easy
> 
> Welcome to WolvCTF's OSINT Category! We have a bunch of great OSINT lined up, assuming nothing goes wrong hahahhahahhahah but why would it?
> 
> For this challenge, find where the image was taken, and look at the Google Maps reviews!
> 
> Note: Flags can be found in standard format wctf{...} for ALL OSINT challenges
> 
> Note: As with the nature of OSINT, false flags can be found. If your flag does not work, it is one of these
> 
> The OSINT Category is as follows:
> 
> WannaFlag I: An Introduction
> 
> WannaFlag II: Payments
> 
> WannaFlag: III: Infiltration
> 
> WannaFlag IV: Exfiltration (visible after completion of WannaFlag: III: Infiltration)
> 
> WannaFlag V: The Mastermind (visible after completion of WannaFlag: III: Infiltration)

### Approach

This is well-designed OSINT challenge series and it's so fun to get the flag. In the first challenge we were given a [png](chall/image.png) image. Based on the instructions we were given directions to find it on google maps and see the reviews.

I use Google Lens and found that the image was Michigan Cube.
![michigan-cube](assets/michigan-cube.png). 

Then I take a look on the review and sort them from the newest first review.
![review](assets/reviews.png)

The `netcat wanna-flag-i dot wolvctf dot io one three three seven` can be converted into this command
```sh
nc wanna-flag-i.wolvctf.io 1337
```

Connect to that server I got a
```
== proof-of-work: disabled ==
Good job finding the Cube! It's a favorite destination among UofM students!
Anyways here is the flag:
wctf{sp1n
Huh???? Where did the rest of the flag g
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="")
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="")
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="")
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
██╗    ██╗ █████╗ ███╗   ██╗███╗   ██╗ █████╗ ███████╗██╗      █████╗  ██████╗
██║    ██║██╔══██╗████╗  ██║████╗  ██║██╔══██╗██╔════╝██║     ██╔══██╗██╔════╝
██║ █╗ ██║███████║██╔██╗ ██║██╔██╗ ██║███████║█████╗  ██║     ███████║██║  ███╗
██║███╗██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║██╔══╝  ██║     ██╔══██║██║   ██║
╚███╔███╔╝██║  ██║██║ ╚████║██║ ╚████║██║  ██║██║     ███████╗██║  ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝
HAHAHHAHAHHAHA Ohhhhh man what an easy CTF to pwn

And I mean also really?? At least make a geo-osint KIND of difficult
The CTF is HOSTED by UofM where else would that dumb cube be????

Oh man ok well organizers if you want your "challenge" back or flags or whatever send 500,000 Goerli here:
0x08f5AF98610aE4B93cD0A856682E6319bF1be8a6

Who knows maybe we'll take more flags if you don't pay in time >:)
#YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs
#YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs
#YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs #YourFlagsBelongToUs
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="")
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="")
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="")
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
██╗    ██╗ █████╗ ███╗   ██╗███╗   ██╗ █████╗ ███████╗██╗      █████╗  ██████╗
██║    ██║██╔══██╗████╗  ██║████╗  ██║██╔══██╗██╔════╝██║     ██╔══██╗██╔════╝
██║ █╗ ██║███████║██╔██╗ ██║██╔██╗ ██║███████║█████╗  ██║     ███████║██║  ███╗
██║███╗██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║██╔══╝  ██║     ██╔══██║██║   ██║
╚███╔███╔╝██║  ██║██║ ╚████║██║ ╚████║██║  ██║██║     ███████╗██║  ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝
██╗    ██╗ █████╗ ███╗   ██╗███╗   ██╗ █████╗ ███████╗██╗      █████╗  ██████╗
██║    ██║██╔══██╗████╗  ██║████╗  ██║██╔══██╗██╔════╝██║     ██╔══██╗██╔════╝
██║ █╗ ██║███████║██╔██╗ ██║██╔██╗ ██║███████║█████╗  ██║     ███████║██║  ███╗
██║███╗██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║██╔══╝  ██║     ██╔══██║██║   ██║
╚███╔███╔╝██║  ██║██║ ╚████║██║ ╚████║██║  ██║██║     ███████╗██║  ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝
██╗    ██╗ █████╗ ███╗   ██╗███╗   ██╗ █████╗ ███████╗██╗      █████╗  ██████╗
██║    ██║██╔══██╗████╗  ██║████╗  ██║██╔══██╗██╔════╝██║     ██╔══██╗██╔════╝
██║ █╗ ██║███████║██╔██╗ ██║██╔██╗ ██║███████║█████╗  ██║     ███████║██║  ███╗
██║███╗██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║██╔══╝  ██║     ██╔══██║██║   ██║
╚███╔███╔╝██║  ██║██║ ╚████║██║ ╚████║██║  ██║██║     ███████╗██║  ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝
Also all of you John OSINTs on twitter need to leave us alone
```

The output mentioned `John OSINTs on twitter` and we were given a hashtag. So let's take a look to twitter.

There is an account named @JohnOSINT_ who used #YourFlagsBelongToUs

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;ve been getting reports of a new ransomware group that have been specifically targeting CTFs. They&#39;ve been posting <a href="https://twitter.com/hashtag/YourFlagsBelongToUs?src=hash&amp;ref_src=twsrc%5Etfw">#YourFlagsBelongToUs</a> to their victims and demanding crypto in exchange for the flags and infra back. This is big.....</p>&mdash; John OSINT (@JohnOSINT_) <a href="https://twitter.com/JohnOSINT_/status/1634680651768270848?ref_src=twsrc%5Etfw">March 11, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

By read that's thread there is a flag encoded with `Base64`

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;ve only exfiltrated one flag from them so far: d2N0Znt1aGhoX3doM3IzX2QxZF80bGxfMHVyX2ZsNGdzX2cwP30=</p>&mdash; John OSINT (@JohnOSINT_) <a href="https://twitter.com/JohnOSINT_/status/1634682918764429313?ref_src=twsrc%5Etfw">March 11, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Using this command to decode, we got that the flag was
![flag](assets/flag.png)

Flag
```
wctf{uhhh_wh3r3_d1d_4ll_0ur_fl4gs_g0?}
```
