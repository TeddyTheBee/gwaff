# gwaff

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bwac2517/gwaff/record-xp-data?label=Xp%20Data%20Recording&style=for-the-badge) ![GitHub](https://img.shields.io/github/license/bwac2517/gwaff?style=for-the-badge) ![code sytle](https://img.shields.io/badge/code%20style-black-black?style=for-the-badge)

A mee6 xp graphing python program using matplotlib.

Originally made for the Mumbo Jumbo Discord server.

### Steps to use for your own server
1. ![Fork](https://github.com/bwac2517/gwaff/fork) or ![download it](https://github.com/bwac2517/gwaff/archive/master.zip) and use it locally.
2. Next, edit the ![config.yml](https://github.com/bwac2517/gwaff/blob/master/config.yml)
```server_id: 377946908783673344 # your server id
darkmode: true # dark mode or not
title: "GWAFF V2"
bottom_message: "\n\ntemplate text.\nCheck out the github on bwac2517/gwaff" # example text
plot:
  range: 60 # how many users to include in the plots
  minium_xp: 500 # anyone with a xp gain below this will not be included in the plots
  rank_range: 20 # the interval it starts a new graph
bar:
  range: 15 # how many users to include in the bar graph
data:
  range: 300 # -1 for all users. how many people to include in data collection
```
4. You should ![make a venv](https://docs.python.org/3/library/venv.html).  
Install dependencies with `python3 -m pip install -r requirements.txt`
4. Run `python3 gwaff.py -s` every day to collect xp data (at the same time of day to keep consistency)  
![(we use a github action for this)](https://github.com/bwac2517/gwaff/blob/master/.github/workflows/main.yml)

5. Every two days, you can generate a graphs with `python3 gwaff.py -p`  
**you can use `python3 gwaff.py -s -p` to do both at once**

Make any changes you want! (make a pull request :p)
