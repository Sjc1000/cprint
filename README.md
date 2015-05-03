# cprint

cprint is a python3 script. It lets you easily color the terminal.
Here is an example of how to use it.

```Python
from cprint import cprint
cprint('[.red]This will be red!')
```

there is a list of all the colors in the cprint file. You can use [./] or [.end] to end the last style used. So if you use [.red]red[./] not red. Red will be red and not red will be well, not red.
You can take it even further. [.red][.underline]red and underline[.end] just red.

There is also an endall that you can use, which ends all of styles at once.
