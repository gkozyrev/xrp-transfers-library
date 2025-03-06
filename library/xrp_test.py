import unittest

from library.xrp import XRPConnector


# test wallet 1: sEdTpdqhCXsRrTznnVBNX5dRTqT1P1x / rhybzrhLMB9z69WbmyRmJ8BNnQYn9TfDfM
# test wallet 2: sEdTfB9LGyn6CgEPLAHB6k7H6FPfKj1 / rw7n6xQWg7UkXD6YsDEVRL9KwjMx1caZap / 5381415

class XRPConnectorTest(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.seed = "sEdTpdqhCXsRrTznnVBNX5dRTqT1P1x"  # Replace with a valid test seed
        # self.rpc_url = "https://s.altnet.rippletest.net:51234" # testnet
        self.rpc_url = "https://xrplcluster.com/" # mainnet
        self.wallet = XRPConnector(self.seed, self.rpc_url)
        print(self.wallet.address())

    def test_generate_wallet(self):
        """Test if wallet is generated successfully"""
        wallet = XRPConnector.generate_wallet()
        self.assertIsNotNone(wallet)
        print(wallet.address, wallet.seed)

    def test_get_self_balance(self):
        """Test if balance is returned successfully"""
        balance = self.wallet.get_balance()
        self.assertIsNotNone(balance)
        print(balance)

    def test_get_balance(self):
        """Test if balance is returned successfully"""
        balance = self.wallet.get_balance("rJn2zAPdFA193sixJwuFixRkYDUtx3apQh")
        self.assertIsNotNone(balance)
        print(balance)

    def test_transfer(self):
        """Test if transfer is successful"""
        destination = "rhybzrhLMB9z69WbmyRmJ8BNnQYn9TfDfM"
        amount_xrp = 0.1
        memo_content = "501264541"
        response = self.wallet.transfer(destination, amount_xrp, memo_content)
        self.assertIsNotNone(response)
        print(response) # {'close_time_iso': '2025-03-06T01:16:12Z', 'ctid': 'C0521DB600060001', 'hash': 'DDAC20F543D99D53E725C521D7CF06B8F82475A3519AAE457D20EEA8FEB71EF6', 'ledger_hash': '822270BBABC3399F65DBDB33CD7C52F5DBB24B72C3F1F18A1272F7ADD0460C96', 'ledger_index': 5381558, 'meta': {'AffectedNodes': [{'CreatedNode': {'LedgerEntryType': 'AccountRoot', 'LedgerIndex': '2FBD0AD47BF288D0007ADC3AAA58D19DCC338B09333E730244E2810663DA7055', 'NewFields': {'Account': 'rhybzrhLMB9z69WbmyRmJ8BNnQYn9TfDfM', 'Balance': '10000000', 'Sequence': 5381558}}}, {'ModifiedNode': {'FinalFields': {'Account': 'rw7n6xQWg7UkXD6YsDEVRL9KwjMx1caZap', 'Balance': '89999980', 'Flags': 0, 'OwnerCount': 0, 'Sequence': 5381417}, 'LedgerEntryType': 'AccountRoot', 'LedgerIndex': '47EDEFF57EE6D79F802191CD2B31B9AE83AC359DD6D4B1BFF74CC0DB3B60C76F', 'PreviousFields': {'Balance': '99999990', 'Sequence': 5381416}, 'PreviousTxnID': '6116F2ACD1CA4419791696C2E617164FB407FCB9423DE4206874879D9E9A6CD3', 'PreviousTxnLgrSeq': 5381533}}], 'TransactionIndex': 6, 'TransactionResult': 'tesSUCCESS', 'delivered_amount': '10000000'}, 'tx_json': {'Account': 'rw7n6xQWg7UkXD6YsDEVRL9KwjMx1caZap', 'DeliverMax': '10000000', 'Destination': 'rhybzrhLMB9z69WbmyRmJ8BNnQYn9TfDfM', 'Fee': '10', 'Flags': 0, 'LastLedgerSequence': 5381576, 'Memos': [{'Memo': {'MemoData': '353031323634353431', 'MemoFormat': '706C61696E', 'MemoType': '74657874'}}], 'Sequence': 5381416, 'SigningPubKey': 'ED26D1B8058B5EAAEB272308B92C99554874B07BC4F6E62134573B2D37A0600169', 'TransactionType': 'Payment', 'TxnSignature': 'D11954AC65D2AC235BC18532400F91B4C0C771EED930133DEA4E017BFBAF827247105C0CCE896CDA54569BC27BCF77A2DFD381AC0A6C3960F675A94DBCAB7606', 'date': 794538972, 'ledger_index': 5381558}, 'validated': True}


if __name__ == '__main__':
    unittest.main()
