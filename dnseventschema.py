from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

class DNSProtocol (str, Enum):
    UDP = "UDP"
    TCP = "TCP"

@dataclass(frozen=True)
class DNSQueryEvent:
    timestamp: float
    client_ip: str
    client_id: Optional[str]
    qname: str
    qtype: str
    qclass: str
    protocol: DNSProtocol
    query_size: int
    edns_size: Optional[int]
    recursion_desired: bool
    labels: List[str]
    label_lengths: List[int]
    num_labels: int
    max_label_length: int
    rcode: Optional[str]
    ttl: Optional[int]
    response_size: Optional[int]
    cache_hit: Optional[bool]