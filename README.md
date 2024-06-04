Besoin d'aide :
https://www.avhiral.com/forum
https://discord.gg/GP6p6jSH

DON PAYPAL : https://www.paypal.com/donate/?hosted_button_id=FSX7RHUT4BDRY

BOT COINBASE V1.3 TRAIDING 2024 - CODE : DAVID PILATO

Install :
sudo apt update
sudo apt install python3-pip
python3 -m pip install ccxt

Edit whith your API COINBASE for avhiral_bot_coinbase_linux_v1.3.py:

nano avhiral_bot_coinbase_linux_v1.3.py

API_KEY = 'YOUR API KEY HERE'
API_SECRET = 'YOUR API SECRET KEY HERE'

Save "avhiral_bot_coinbase_linux_v1.3.py"

Fonction:

python3 avhiral_bot_coinbase_linux_v1.3.py --start --desired_profit 5
python3 avhiral_bot_coinbase_linux_v1.3.py --status
python3 avhiral_bot_coinbase_linux_v1.3.py --monitor
python3 avhiral_bot_coinbase_linux_v1.3.py --stop

EXEMPLE :

python3 avhiral_bot_coinbase_linux_v1.3.py --start --desired_profit 0.008
/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (2.0.3) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
Bot Coinbase Started with a daily profit goal of $0.008
Available pairs for trading with positive balance:
1. SOL/USD : 0.089809476 SOL
2. SOL/USDC : 0.089809476 SOL
3. AVAX/USD : 0.01380457 AVAX
4. AVAX/USDC : 0.01380457 AVAX
5. SOL/EUR : 0.089809476 SOL
6. ADA/USD : 0.011662 ADA
7. ADA/USDC : 0.011662 ADA
8. SOL/USDT : 0.089809476 SOL
9. CBETH/USD : 1.64e-06 CBETH
10. CBETH/USDC : 1.64e-06 CBETH
11. AKT/USDC : 0.153605 AKT
12. AKT/USD : 0.153605 AKT
13. ATOM/USD : 0.00052 ATOM
14. ATOM/USDC : 0.00052 ATOM
15. SOL/GBP : 0.089809476 SOL
16. ZETA/USD : 0.31198698 ZETA
17. ZETA/USDC : 0.31198698 ZETA
18. VET/USD : 1.54716706 VET
19. VET/USDC : 1.54716706 VET
20. AVAX/EUR : 0.01380457 AVAX
21. AVAX/USDT : 0.01380457 AVAX
22. ADA/EUR : 0.011662 ADA
23. 00/USD : 0.01774438 00
24. 00/USDC : 0.01774438 00
25. SAND/USDC : 0.00187863 SAND
26. SAND/USD : 0.00187863 SAND
27. ADA/USDT : 0.011662 ADA
28. ATOM/USDT : 0.00052 ATOM
29. ADA/GBP : 0.011662 ADA
30. ATOM/EUR : 0.00052 ATOM
31. ATOM/GBP : 0.00052 ATOM
32. SAND/USDT : 0.00187863 SAND
33. SOL/ETH : 0.089809476 SOL
34. CBETH/ETH : 1.64e-06 CBETH
35. SOL/BTC : 0.089809476 SOL
36. ADA/ETH : 0.011662 ADA
37. AVAX/BTC : 0.01380457 AVAX
38. ADA/BTC : 0.011662 ADA
39. ATOM/BTC : 0.00052 ATOM
40. SOL/USDC:USDC : 0.089809476 SOL
41. AVAX/USDC:USDC : 0.01380457 AVAX
42. ADA/USDC:USDC : 0.011662 ADA
Select the pair number you want to trade: 1
root@avhiral-MS-7369:~/coinbase# python3 avhiral_bot_coinbase_linux_v1.3.py --status
/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (2.0.3) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
The trading bot is currently active.
root@avhiral-MS-7369:~/coinbase# python3 avhiral_bot_coinbase_linux_v1.3.py --monitor
/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (2.0.3) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
2024-05-18 17:20:36,552 - INFO - Exchange initialized successfully.
2024-05-18 17:20:36,816 - INFO - Active crypto pairs with positive balance: ['SOL/USDC', 'SOL/USD', 'AVAX/USD', 'AVAX/USDC', 'SOL/EUR', 'ADA/USDC', 'ADA/USD', 'SOL/USDT', 'CBETH/USD', 'CBETH/USDC', 'AKT/USD', 'AKT/USDC', 'ATOM/USDC', 'ATOM/USD', 'SOL/GBP', 'ZETA/USDC', 'ZETA/USD', 'VET/USD', 'VET/USDC', 'AVAX/EUR', 'AVAX/USDT', 'ADA/EUR', '00/USD', '00/USDC', 'SAND/USDC', 'SAND/USD', 'ADA/USDT', 'ATOM/USDT', 'ADA/GBP', 'ATOM/EUR', 'ATOM/GBP', 'SAND/USDT', 'SOL/ETH', 'CBETH/ETH', 'SOL/BTC', 'ADA/ETH', 'AVAX/BTC', 'ADA/BTC', 'ATOM/BTC', 'SOL/USDC:USDC', 'AVAX/USDC:USDC', 'ADA/USDC:USDC']
2024-05-18 17:25:26,027 - INFO - Exchange initialized successfully.
2024-05-18 17:25:26,266 - INFO - Active crypto pairs with positive balance: ['SOL/USD', 'SOL/USDC', 'AVAX/USD', 'AVAX/USDC', 'SOL/EUR', 'ADA/USD', 'ADA/USDC', 'SOL/USDT', 'CBETH/USD', 'CBETH/USDC', 'AKT/USDC', 'AKT/USD', 'ATOM/USD', 'ATOM/USDC', 'SOL/GBP', 'ZETA/USD', 'ZETA/USDC', 'VET/USD', 'VET/USDC', 'AVAX/EUR', 'AVAX/USDT', 'ADA/EUR', '00/USD', '00/USDC', 'SAND/USDC', 'SAND/USD', 'ADA/USDT', 'ATOM/USDT', 'ADA/GBP', 'ATOM/EUR', 'ATOM/GBP', 'SAND/USDT', 'SOL/ETH', 'CBETH/ETH', 'SOL/BTC', 'ADA/ETH', 'AVAX/BTC', 'ADA/BTC', 'ATOM/BTC', 'SOL/USDC:USDC', 'AVAX/USDC:USDC', 'ADA/USDC:USDC']

