###
### NOTE: Working with temporal's codec is really really weird
###       This is a workaround to use pydantic models with temporal
###       The codec is used to serialize/deserialize the data
###       But this code is quite brittle. Be careful when changing it


import dataclasses
import logging
import pickle
from typing import Any, Optional, Type

import temporalio.converter

# from beartype import BeartypeConf
# from beartype.door import is_bearable, is_subhint
from lz4.frame import compress, decompress
from temporalio.api.common.v1 import Payload
from temporalio.converter import (
    CompositePayloadConverter,
    DefaultPayloadConverter,
    EncodingPayloadConverter,
)


def serialize(x: Any) -> bytes:
    return compress(pickle.dumps(x))


def deserialize(b: bytes) -> Any:
    return pickle.loads(decompress(b))


def from_payload_data(data: bytes, type_hint: Optional[Type] = None) -> Any:
    decoded = deserialize(data)

    if type_hint is None:
        return decoded

    decoded_type = type(decoded)

    # FIXME: Enable this check when temporal's codec stuff is fixed
    #
    # # Otherwise, check if the decoded value is bearable to the type hint
    # if not is_bearable(
    #     decoded,
    #     type_hint,
    #     conf=BeartypeConf(
    #         is_pep484_tower=True
    #     ),  # Check PEP 484 type hints. (be more lax on numeric types)
    # ):
    #     logging.warning(
    #         f"WARNING: Decoded value {decoded_type} is not bearable to {type_hint}"
    #     )

    # FIXME: Enable this check when temporal's codec stuff is fixed
    #
    # If the decoded value is a BaseModel and the type hint is a subclass of BaseModel
    # and the decoded value's class is a subclass of the type hint, then promote the decoded value
    # to the type hint.
    if (
        type_hint != decoded_type
        and hasattr(type_hint, "model_construct")
        and hasattr(decoded, "model_dump")
        #
        # FIXME: Enable this check when temporal's codec stuff is fixed
        #
        # and is_subhint(type_hint, decoded_type)
    ):
        try:
            decoded = type_hint(**decoded.model_dump())
        except Exception as e:
            logging.warning(
                f"WARNING: Could not promote {decoded_type} to {type_hint}: {e}"
            )

    return decoded


class PydanticEncodingPayloadConverter(EncodingPayloadConverter):
    encoding = "text/pickle+lz4"
    b_encoding = encoding.encode()

    def to_payload(self, value: Any) -> Optional[Payload]:
        return Payload(
            metadata={
                "encoding": self.b_encoding,
            },
            data=serialize(value),
        )

    def from_payload(self, payload: Payload, type_hint: Optional[Type] = None) -> Any:
        assert payload.metadata["encoding"] == self.b_encoding
        return from_payload_data(payload.data, type_hint)


class PydanticPayloadConverter(CompositePayloadConverter):
    def __init__(self) -> None:
        # Just add ours as first before the defaults
        super().__init__(
            PydanticEncodingPayloadConverter(),
            *DefaultPayloadConverter.default_encoding_payload_converters,
        )


# Use the default data converter, but change the payload converter.
pydantic_data_converter: Any = dataclasses.replace(
    temporalio.converter.default(),
    payload_converter_class=PydanticPayloadConverter,
)
