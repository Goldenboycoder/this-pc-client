
# ThisPc-Client
![python --version](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8-green)

ThisPc-Client is a web-based dashboard used in [ThisPc project](https://github.com/Goldenboycoder/this-pc-project), to monitor PCs running ThisPC-API.
## Appendix
[ThisPC-Project](https://github.com/Goldenboycoder/this-pc-project)

[ThisPC-API](https://github.com/Goldenboycoder/this-pc-api): installed on the PCs to monitor.

## Features

- Redis subscription to the PC-* pattern to which all the machines running ThisPC-API publish their data to.
- Using pandas and plotly, Charts and graphs are built to visualize CPU utilization and load for the past 15 minutes.
- Live Dashboard hosted locally using plotly-dash, displaying all publishers’ performance data.

## Installation

Clone this repository

```cmd
  git clone https://github.com/Goldenboycoder/this-pc-client.git
  cd this-pc-client
```

## Dependencies

```
pip install redis
pip install pandas
pip install dash
```
## Usage

Simply Run:

```
python Client.py
```
Wait ~20s then open your browser and go to: [localhost:8050](localhost:8050)

You will see the dashboard where each row corresponds to one of the PCs.

![Dashboard](https://github.com/Goldenboycoder/this-pc-project/blob/main/imgs/dashboard.png)

*N.B:If the web page isn’t loading refresh a few times.*


  
## License

[BSD 3-Clause License](./LICENSE)

  
## Author

- [@Patrick Balian](https://github.com/Goldenboycoder)

[![twitter](https://img.shields.io/twitter/follow/patrick_balian?style=social)](https://twitter.com/Patrick_Balian)

[![linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/patrick-balian-41b851147/)
