## OSINT - Time Machine

In this challenge, we were given these clue.

> There was a secret leaked on Official ARA Website. It can only seen on January 22nd 2023. Can you turn back the time?

So, we try to see the history or tracking back the website into January 22nd of 2023 using [WayBack Machine](https://archive.org/web/). First try we got tricked. It doesn't show the result as what we expected.

![res](assets/Screenshot%20(555).png)

Then, we realized that the clue were only said 'Official ARA Website', not the 'ARA CTF Website. So, we try to remove the subdomain. We got it.

![res](assets/Screenshot%20(556).png)

And we finally got the flag in `index` file.

![res](assets/Screenshot_20230226_082606.png)

</br>

So, this is the flag.

```
ARA2023{d1gIt4l_f00tpr1nt_1s_sC4ry}
```
