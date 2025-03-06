# XRP Ledger Connector

A Python library for interacting with the XRP Ledger, providing functionalities for wallet management, balance checks, and XRP transfers with memos.

## Features

- **Wallet Management**:
  - Generate new XRP wallets
  - Retrieve wallet address from seed
- **Balance Checks**:
  - Get balance of any XRP address
  - Returns balance in XRP (decimal format)
- **Transactions**:
  - Send XRP with optional memos
  - Automatic transaction signing & submission
  - Real-time transaction validation checks

## Prerequisites

- Python 3.7+
- [xrpl-py](https://pypi.org/project/xrpl-py/) library
```bash
pip install xrpl-py
```

## Usage

### Initialize Connector
```python
from xrp_connector import XRPConnector

# For Testnet
connector = XRPConnector(
    seed="sEdT...",
    rpc_url="wss://s.altnet.rippletest.net:51233"
)

# For Mainnet
connector = XRPConnector(
    seed="sEdT...",  # Your mainnet seed
    rpc_url="wss://xrplcluster.com/"
)
```

### Generate New Wallet
```python
new_wallet = XRPConnector.generate_wallet()
print(f"Address: {new_wallet.address}")
print(f"Seed: {new_wallet.seed}")
```

### Check Balance
```python
# Check self balance
balance = connector.get_balance()
print(f"Your balance: {balance} XRP")

# Check other address balance
external_balance = connector.get_balance("rJn2zAPdFA193sixJWuFixRkYDUtx3apQh")
print(f"External balance: {external_balance} XRP")
```

### Send XRP
```python
try:
    tx = connector.transfer(
        destination="rhybzrhLMB9z69WbmyRmJ8BNnQYn9TfDfM",
        amount_xrp=0.1,
        memo_content="501264541"  # Required for exchanges
    )
    print(f"Transaction successful: {tx['hash']}")
except Exception as e:
    print(f"Transaction failed: {str(e)}")
```

## Testing

1. **Testnet Setup**:
   - Get test XRP from [Testnet Faucet](https://xrpl.org/xrp-testnet-faucet.html)
   
2. **Run Tests**:
```bash
python -m unittest discover -s tests
```

## Important Notes

- **Memo Requirements**:
  - Exchanges like Bybit require memo tags for deposits
  - Always verify memo format with your exchange

- **Account Activation**:
  - New accounts require 10 XRP minimum balance
  - Use `transfer(..., amount_xrp=10)` for activation

- **Network Fees**:
  - Transactions cost ~0.00001 XRP
  - Maintain at least 20 XRP for active usage

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open Pull Request
