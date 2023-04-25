import httpx


class ShinamiClient:
    def __init__(
        self,
        token: str,
        api_url: str = "https://api.shinami.com",
    ) -> None:
        self.api_url = api_url
        self.headers = {
            "X-API-Key": token,
            "Content-Type": "application/json",
        }

    async def create_session(
        self,
        secret: str,
    ) -> str:
        """
        Create a Shinami session token for a given secret.

        Args:
            secret (str): The secret to use to create the session token.
        """
        data = {
            "jsonrpc": "2.0",
            "method": "shinami_key_createSession",
            "params": [secret],
            "id": 1,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/key/v1", headers=self.headers, json=data
            )
        response.raise_for_status()
        return response.json()["result"]["SessionToken"]

    async def create_wallet(
        self,
        wallet_id: str,
        session_token: str,
    ) -> str:
        """
        Create a Shinami wallet for a given wallet ID and session token.

        Args:
            wallet_id (str): The wallet ID to use to create the wallet.
            session_token (str): The session token to use to create the wallet.
        """
        data = {
            "jsonrpc": "2.0",
            "method": "shinami_wal_createWallet",
            "params": [wallet_id, session_token],
            "id": 1,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/wallet/v1", headers=self.headers, json=data
            )
        response.raise_for_status()
        return response.json()["result"]["WalletAddress"]

    async def get_wallet(
        self,
        wallet_id: str,
    ) -> str:
        """
        Get a Shinami wallet for a given wallet ID.

        Args:
            wallet_id (str): The wallet ID to use to get the wallet.
        """
        data = {
            "jsonrpc": "2.0",
            "method": "shinami_wal_getWallet",
            "params": [wallet_id],
            "id": 1,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/wallet/v1", headers=self.headers, json=data
            )
        response.raise_for_status()
        return response.json()["result"]["WalletAddress"]

    async def sign_transaction_block(
        self,
        wallet_id: str,
        session_token: str,
        tx_bytes: str,
    ) -> str:
        """
        Sign a Shinami transaction block for a given wallet ID,
        session token, and transaction bytes.

        Args:
            wallet_id (str): The wallet ID to use to sign the transaction block.
            session_token (str): The session token to use to sign the transaction block.
            tx_bytes (str): The transaction bytes to use to sign the transaction block.
        """
        data = {
            "jsonrpc": "2.0",
            "method": "shinami_wal_signTransactionBlock",
            "params": [wallet_id, session_token, tx_bytes],
            "id": 1,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/wallet/v1", headers=self.headers, json=data
            )
        response.raise_for_status()
        return response.json()["result"]["Signature"]
