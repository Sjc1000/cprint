# cprint

cprint is a python3 script. It lets you easily color the terminal.
Here is an example of how to use it.

```Python
from cprint import cprint
cprint('[.red]This will be red!')
```
You use [./color] to end the color or style. You can also use [.endall] to end all styling.

```Python
from cprint import cprint
cprint('[.red]This will be red.[.underline] This will be red and underlined.[./red] This will just be underlined!')
```

There is a list of all the colors in the cprint file.
