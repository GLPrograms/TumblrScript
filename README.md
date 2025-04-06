# Tumblr Script
This is an all-purpose script to read out new Tumblr 
posts from almost any user on the site.
##### Created by [<img src="https://avatars.githubusercontent.com/u/100171133?v=4&size=64" width="16" style="border-radius:100px;"/>](image.png) [Kauntar](https://kauntar.github.io/)

## Requirements
To use this script, you will need the following:

### Software
> Python (preferrably Python 3)
> A CLI (command-line) of some sort

### Modules
> BeautifulSoup
```pip install bs4```

> Requests
```pip install requests```

> Colorama
```pip install colorama```

## How to run the program
In order to run the program, enter the directory of the file and 
run the following command
```python run.py```

## Starting off
### User Prompt
![User Choice Image](https://kauntar.github.io/cdn/giggleland/github/tumblrscript/1.png)
Here you can put the username of any Tumblr user.

### Old Data Prompt 
**Recommended:** `y`
![Data File Image](https://kauntar.github.io/cdn/giggleland/github/tumblrscript/2.png)
What does this mean? Well, every time the program gets a 
new post, it logs that post to `<username>.txt`, this then gets
used to avoid duplication of posts (which is really annoying if
you enable Discord pinging on the first run).

### [Discord](https://discord.com/) Related Prompts
![Webhook Prompt](https://kauntar.github.io/cdn/giggleland/github/tumblrscript/3.png)

![Webhook URL Prompt](https://kauntar.github.io/cdn/giggleland/github/tumblrscript/4.png)
You can read more about webhooks [here]().

![Ping Prompt](https://kauntar.github.io/cdn/giggleland/github/tumblrscript/5.png)
This will add an `@everyone` to the end of the message that
is sent in the webhook.