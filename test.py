import pyupbit

access = "id"          # 본인 값으로 변경
secret = "pw"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-bct 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(upbit.get_balance("KRW-SAND") )   # KRW- SANDBOX 조회
