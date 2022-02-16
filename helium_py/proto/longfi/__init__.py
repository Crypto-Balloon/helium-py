# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: longfi.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class LongFiSpreading(betterproto.Enum):
    SF_INVALID = 0
    SF7 = 1
    SF8 = 2
    SF9 = 3
    SF10 = 4


@dataclass(eq=False, repr=False)
class LongFiReq(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    tx: "LongFiTxPacket" = betterproto.message_field(2, group="kind")


@dataclass(eq=False, repr=False)
class LongFiResp(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    tx_status: "LongFiTxStatus" = betterproto.message_field(2, group="kind")
    rx: "LongFiRxPacket" = betterproto.message_field(3, group="kind")
    parse_err: bytes = betterproto.bytes_field(4, group="kind")
    miner_name: bytes = betterproto.bytes_field(5)


@dataclass(eq=False, repr=False)
class LongFiTxStatus(betterproto.Message):
    success: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class LongFiRxPacket(betterproto.Message):
    # Status of CRC check.
    crc_check: bool = betterproto.bool_field(1)
    # 1uS-resolution timestamp derived from concentrator's internal counter.
    timestamp: int = betterproto.uint64_field(2)
    # Average packet RSSI in dB.
    rssi: float = betterproto.float_field(3)
    # Average packet SNR, in dB.
    snr: float = betterproto.float_field(4)
    # Organization Unique ID
    oui: int = betterproto.uint32_field(5)
    # Device ID
    device_id: int = betterproto.uint32_field(6)
    # Fingerprint
    fingerprint: int = betterproto.uint32_field(7)
    # Sequence
    sequence: int = betterproto.uint32_field(9)
    # Spreading to be used
    spreading: "LongFiSpreading" = betterproto.enum_field(10)
    # the fully reassembled payload
    payload: bytes = betterproto.bytes_field(11)
    # De-golayed datagram id and flag bits. NOTE: only the lowest 12 bits are
    # valid.
    tag_bits: int = betterproto.uint32_field(12)


@dataclass(eq=False, repr=False)
class LongFiTxPacket(betterproto.Message):
    # is device receiver (downlink) or is router receiver (uplink) note: when
    # Hotspot is sending Proof of Coverage packet, it should behave as a device
    # and flag this as "uplink"
    downlink: bool = betterproto.bool_field(1)
    # should the receiver ACK
    should_ack: bool = betterproto.bool_field(2)
    # on uplink, this indicates the device is ready to receive downlink
    cts: bool = betterproto.bool_field(3)
    # is the packet urgent
    priority: bool = betterproto.bool_field(4)
    # the packet beyond the tag field is encoded with LDPC
    ldpc: bool = betterproto.bool_field(5)
    # Organization Unique ID
    oui: int = betterproto.uint32_field(6)
    # Device ID
    device_id: int = betterproto.uint32_field(7)
    # Fingerprint
    fingerpint: int = betterproto.uint32_field(8)
    # Sequence
    sequence: int = betterproto.uint32_field(9)
    # Spreading to be used
    spreading: "LongFiSpreading" = betterproto.enum_field(10)
    payload: bytes = betterproto.bytes_field(11)
