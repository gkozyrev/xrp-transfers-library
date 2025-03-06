from decimal import Decimal

from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.models import Payment, Memo, Tx
from xrpl.transaction import submit_and_wait, autofill_and_sign
from xrpl.utils import xrp_to_drops
from xrpl.wallet import Wallet


class XRPConnector:
    def __init__(self, seed: str, rpc_url: str):
        """
        Initialize XRP Wallet

        Args:
            seed: Wallet seed (secret)
            rpc_url: WebSocket URL for JSON-RPC connection
                      Example: 'wss://s.altnet.rippletest.net:51233'
        """
        self.client = JsonRpcClient(rpc_url)
        self.wallet = Wallet.from_seed(seed)

    def address(self) -> str:
        """Get the XRP address associated with the wallet"""
        return self.wallet.address

    def get_balance(self, address: str = None) -> Decimal:
        """Get XRP balance in decimal format"""
        if address is None:
            address = self.address()
        balance = get_balance(address, self.client)

        return Decimal(balance) / 1_000_000

    def transfer(
            self,
            destination: str,
            amount_xrp: float,
            memo_content: str = "",
    ) -> dict:
        """Send XRP with optional memo"""
        # Prepare memo if provided
        memos = []
        if memo_content:
            memos.append(
                Memo(
                    memo_data=memo_content.encode().hex(),
                )
            )

        # Prepare transaction
        payment = Payment(
            account=self.address(),
            destination=destination,
            amount=xrp_to_drops(amount_xrp),
            memos=memos
        )

        # Autofill, sign, and submit
        tx_payment_signed = autofill_and_sign(payment, self.client, self.wallet)
        response = submit_and_wait(tx_payment_signed, self.client)

        if not response.is_successful():
            raise Exception(f"Transaction failed: {response.result}")

        # Create a "Tx" request to look up the transaction on the ledger
        tx_response = self.client.request(Tx(transaction=response.result["hash"]))

        # Check whether the transaction was actually validated on ledger
        print("Validated:", tx_response.result["validated"])

        return response.result

    @classmethod
    def generate_wallet(cls):
        """Class method to generate a new wallet"""
        wallet = Wallet.create()

        return wallet