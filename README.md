# excel-scanner
This project provides all the necessary features for Dr. Ken Long's day trading. Mainly RLCO and Frogbox.

## daily frog box calculation
```buildoutcfg
# conda env update -f scanner.yml
# activate scanner
# python frogbox.py --start_date yyyymmdd
```
The above command will update daily frogbox in frogbox folder. It requires iqfeed running.


## daily trade files processing
download the html trade report from IB and place it in data folder
```buildoutcfg
# conda env update -f scanner.yml
# activate scanner
# python main.py
```
It will produce a trade csv file.


## Frog Trade Service
Run frog box calculation and serve it to NT Frog Indicator
```buildoutcfg
# conda env update -f scanner.yml
# activate scanner
# python frogboxservice.py
```
