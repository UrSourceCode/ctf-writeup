## Web - Trapped Source

### Description

> 300pts
> 
> Intergalactic Ministry of Spies tested Pandora's movement and intelligence abilities. She found herself locked in a room with no apparent means of escape. Her task was to unlock the door and make her way out. Can you help her in opening the door?


### Knowledge Requirements

1. Basic understanding of Web Source

### Exploit

This challenge was very easy. We were given a web who look like this

![web](assets/Web.png)

First, let's take a look at the page source. In the page source there is a script who look like this
```html
<script>
    window.CONFIG = window.CONFIG || {
        buildNumber: "v20190816",
        debug: false,
        modelName: "Valencia",
        correctPin: "8291",
    }
</script>
```

Let's input the correct pin and we got the flag.
![pin](assets/pin.png)

The flag was:
```
HTB{V13w_50urc3_c4n_b3_u53ful!!!}
```