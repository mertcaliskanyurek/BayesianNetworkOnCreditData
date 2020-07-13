class table
      bad    good
0  0.2925  0.7075

property_magnitude table
  class  real estate  life insurance  no known property       car
0   bad     0.200855        0.226496           0.230769  0.341880
1  good     0.318021        0.227915           0.118375  0.335689

own_telephone table
  class                        job       yes      none
0   bad  high qualif/self emp/mgmt  0.833333  0.166667
1   bad                    skilled  0.290780  0.709220
2   bad         unskilled resident  0.177778  0.822222
3   bad    unemp/unskilled non res  0.166667  0.833333
4  good  high qualif/self emp/mgmt  0.862500  0.137500
5  good                    skilled  0.396694  0.603306
6  good         unskilled resident  0.153153  0.846847
7  good    unemp/unskilled non res  0.333333  0.666667

housing table
  class property_magnitude      rent       own  for free
0   bad        real estate  0.255319  0.723404  0.021277
1   bad     life insurance  0.226415  0.754717  0.018868
2   bad  no known property  0.148148  0.222222  0.629630
3   bad                car  0.262500  0.737500  0.000000
4  good        real estate  0.183333  0.816667  0.000000
5  good     life insurance  0.217054  0.775194  0.007752
6  good  no known property  0.119403  0.179104  0.701493
7  good                car  0.142105  0.852632  0.005263

job table
  class property_magnitude  high qualif/self emp/mgmt   skilled  unskilled resident  unemp/unskilled non res
0   bad        real estate                   0.085106  0.553191            0.319149                 0.042553
1   bad     life insurance                   0.113208  0.698113            0.169811                 0.018868
2   bad  no known property                   0.333333  0.500000            0.129630                 0.037037
3   bad                car                   0.175000  0.637500            0.175000                 0.012500
4  good        real estate                   0.055556  0.583333            0.338889                 0.022222
5  good     life insurance                   0.108527  0.627907            0.248062                 0.015504
6  good  no known property                   0.328358  0.582090            0.029851                 0.059701
7  good                car                   0.178947  0.726316            0.084211                 0.010526

personal_status table
  class   housing  male div/sep  male mar/wid  male single  female div/dep/mar
0   bad      rent      0.094340      0.056604     0.264151            0.584906
1   bad       own      0.075862      0.117241     0.468966            0.337931
2   bad  for free      0.000000      0.000000     0.805556            0.194444
3  good      rent      0.000000      0.156250     0.312500            0.531250
4  good       own      0.047506      0.085511     0.610451            0.256532
5  good  for free      0.020408      0.020408     0.816327            0.142857

purpose table
  class   housing  furniture/equipment   repairs   new car  radio/tv  business     other  used car  education
0   bad      rent             0.320755  0.018868  0.226415  0.150943  0.169811  0.018868  0.056604   0.037736
1   bad       own             0.213793  0.027586  0.317241  0.248276  0.089655  0.034483  0.020690   0.048276
2   bad  for free             0.083333  0.055556  0.305556  0.083333  0.083333  0.027778  0.250000   0.111111
3  good      rent             0.270833  0.010417  0.197917  0.239583  0.041667  0.010417  0.166667   0.062500
4  good       own             0.173397  0.023753  0.209026  0.318290  0.104513  0.040380  0.099762   0.030879
5  good  for free             0.122449  0.020408  0.224490  0.142857  0.040816  0.040816  0.285714   0.122449

credit_history table
  class own_telephone  critical/other existing credit  delayed previously  existing paid  no credits/all paid  all paid
0   bad           yes                        0.164706            0.141176       0.505882             0.094118  0.094118
1   bad          none                        0.154362            0.060403       0.624161             0.073826  0.087248
2  good           yes                        0.354701            0.081197       0.525641             0.012821  0.025641
3  good          none                        0.325301            0.075301       0.533133             0.030120  0.036145

employment table
  class                        job    1<=X<4       >=7        <1    4<=X<7  unemployed
0   bad  high qualif/self emp/mgmt  0.214286  0.404762  0.119048  0.047619    0.214286
1   bad                    skilled  0.404255  0.184397  0.212766  0.163121    0.035461
2   bad         unskilled resident  0.422222  0.133333  0.333333  0.111111    0.000000
3   bad    unemp/unskilled non res  0.000000  0.000000  0.166667  0.000000    0.833333
4  good  high qualif/self emp/mgmt  0.162500  0.362500  0.100000  0.200000    0.175000
5  good                    skilled  0.349862  0.289256  0.151515  0.192837    0.016529
6  good         unskilled resident  0.378378  0.216216  0.171171  0.225225    0.009009
7  good    unemp/unskilled non res  0.000000  0.000000  0.250000  0.000000    0.750000

results  tp: 22 tn: 123 fp: 11 fn: 44 tpr: 0.3333333333333333 tnr: 0.917910447761194 acc: 0.725