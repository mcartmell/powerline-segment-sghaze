# Singapore Haze Powerline Segment

A [Powerline](https://github.com/Lokaltog/powerline) segment for displaying the
[PSI](http://www.nea.gov.sg/psi/) reading in Singapore.

# Installing

1. First, install this module:

```
$ git clone https://github.com/mcartmell/powerline-segment-sghaze
$ cd powerline-segment-sghaze
$ pip install .
```

2. If you already have Powerline configuration in your `~/.config`, skip this step. Otherwise, copy the entire set of default Powerline configuration files to your user's config directory:

```
mkdir ~/.config/powerline
cp -R /path/to/powerline/config_files/* ~/.config/powerline
```

3. Now define colours for it, eg. by editing `~/.config/powerline/colorschemes/tmux/default.json`

```
"sghaze": { "fg": "gray10", "bg": "black" }
```

4. Finally, add this module to your segment configuration, eg. `~/.config/powerline/themes/tmux/default.json`

```
{
  "name": "sghaze",
  "module": "powerline_sghaze.segments",
  "args": {
    "area": "West"
  }
},
```

It looks like this for me:

![screenshot](/screenshot.png?raw=true)
