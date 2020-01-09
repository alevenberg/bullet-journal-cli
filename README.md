# bullet-journal-cli


# File structure
```
├── README.md
├── calendar_grapher.py ------------> holds utility function to generate the matplotlib graph
├── driver.py ----------------------> reads the csv and saves the generated graph in ./graphs
├── graphs -------------------------> stores generated graphs
│   └── 2020-running.png
├── io_generator.py
├── log.py
└── logs
    └── 2020-running.csv
```

# Todo 
[ ] Make a calendar per month 
[ ] Pick color for calendar
[ ] Add file structure
[ ] Write sample commands to run 
    - python3 log.py -w running
    - python3 driver.py -g running
[ ] Handle already written lines
