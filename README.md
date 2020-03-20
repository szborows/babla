# babla

bab.la dictionary CLI tool

# integration with i3/dmenu

although this tool is a CLI tool, you can easily integrate it with any window manager. e.g. for
i3 and dmenu you can create simple script:

```
#!/usr/bin/env bash
set -euo pipefail
exec xterm -e /bin/bash -c "babla $1 && read -n1 -r"
```

instad of xterm I suggest to use st (suckless terminal) that is pre-compiled with specific font size

e.g.

```
exec st -f "Liberation Mono:pixelsize=32:antialias=true:autohint=true" /bin/bash -c "babla $1 && read -n1 -r"
```
