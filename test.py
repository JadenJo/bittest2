import pyupbit

access = "oMLHpvWeTmAMjzaPO69fx2hbLyXhfYMlfvYGuVp5"          # 본인 값으로 변경
secret = "xRIn4Wm0rEsPRSQMzf2talcYyfO1jy9mETxiq2T5"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-bct 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(upbit.get_balance("KRW-SAND") )   # KRW- SANDBOX 조회