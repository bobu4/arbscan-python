from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules
from bscscan.enums.tags_enum import TagsEnum as tags


class Proxy:
    @staticmethod
    def get_proxy_block_number():
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_BLOCK_NUMBER}"
        )
        return url

    @staticmethod
    def get_proxy_block_by_number(tag: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_BLOCK_BY_NUMBER}"
            f"{fields.TAG}"
            f"{tag}"
            f"{fields.BOOLEAN}"
            f"true"
        )
        return url

    @staticmethod
    def get_proxy_block_transaction_count_by_number(tag: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_BLOCK_TRANSACTION_COUNT_BY_NUMBER}"
            f"{fields.TAG}"
            f"{tag}"
        )
        return url

    @staticmethod
    def get_proxy_transaction_by_hash(txhash: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_BY_HASH}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url

    @staticmethod
    def get_proxy_transaction_by_block_number_and_index(tag: str, index: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_BY_BLOCK_NUMBER_AND_INDEX}"
            f"{fields.TAG}"
            f"{tag}"
            f"{fields.INDEX}"
            f"{index}"
        )
        return url

    @staticmethod
    def get_proxy_transaction_count(address: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_COUNT}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url

    @staticmethod
    def get_proxy_transaction_receipt(txhash: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_RECEIPT}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url

    @staticmethod
    def get_proxy_call(to: str, data: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_CALL}"
            f"{fields.TO}"
            f"{to}"
            f"{fields.DATA}"
            f"{data}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url

    @staticmethod
    def get_proxy_code_at(address: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_CODE}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url

    @staticmethod
    def get_proxy_storage_position_at(position: str, address: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_STORAGE_AT}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.POSITION}"
            f"{position}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url

    @staticmethod
    def get_proxy_gas_price():
        # NOTE: Results are in WEI
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GAS_PRICE}"
        )
        return url

    @staticmethod
    def get_proxy_est_gas(
        from_addr: str, to_addr: str, data: str, value: str, gas_price: str, gas: str
    ):
        url = (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_ESTIMATE_GAS}"
            f"{fields.DATA}"
            f"{data}"
            f"{fields.FROM}"
            f"{from_addr}"
            f"{fields.TO}"
            f"{to_addr}"
            f"{fields.VALUE}"
            f"{value}"
            f"{fields.GAS_PRICE}"
            f"{gas_price}"
            f"{fields.GAS}"
            f"{gas}"
        )
        return url
