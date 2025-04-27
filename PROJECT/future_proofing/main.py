# Decentralized Storage with IPFS for Virtual Cards
# virtual_card_storage.py

import ipfshttpclient
import json
import io
import logging

logging.basicConfig(level=logging.INFO)

class DecentralizedCardStorage:
    def __init__(self, ipfs_gateway_url="/ip4/127.0.0.1/tcp/5001"):
        try:
            self.client = ipfshttpclient.connect(ipfs_gateway_url)
            logging.info("Connected to IPFS gateway successfully.")
        except Exception as e:
            logging.error(f"Failed to connect to IPFS gateway: {e}")
            raise

    def store_card_data(self, card_data: dict) -> str:
        """
        Store virtual card data on IPFS.
        Returns the CID (Content Identifier) for retrieval.
        """
        try:
            # TODO: Encrypt card_data before storing
            json_bytes = json.dumps(card_data).encode("utf-8")
            file_like = io.BytesIO(json_bytes)
            result = self.client.add(file_like)
            logging.info(f"Data stored on IPFS with CID: {result['Hash']}")
            return result['Hash']  # CID
        except Exception as e:
            logging.error(f"Failed to store card data: {e}")
            raise

    def retrieve_card_data(self, cid: str) -> dict:
        """
        Retrieve card data from IPFS using its CID.
        """
        try:
            raw_data = self.client.cat(cid)
            card_data = json.loads(raw_data.decode("utf-8"))
            # TODO: Decrypt card_data after retrieval
            logging.info(f"Data retrieved for CID: {cid}")
            return card_data
        except Exception as e:
            logging.error(f"Failed to retrieve card data for CID {cid}: {e}")
            raise

    def revoke_card_data(self, cid: str):
        """
        In IPFS, data is immutable and can't be deleted in the traditional sense.
        This method can be used to mark a card as revoked in off-chain metadata.
        """
        # TODO: Implement revocation logic in metadata layer or off-chain database
        logging.warning(f"Revocation requested for CID {cid}, but IPFS is immutable.")
        pass
