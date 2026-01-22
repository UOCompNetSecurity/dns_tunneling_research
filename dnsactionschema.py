"""
Detector -> Resolver Control Message whenever an action is determined on a domain through classification/analysis
"""

from dataclasses import dataclass
from enum import Enum

class ActionType (str, Enum):
    BLOCK = "BLOCK"
    SINKHOLE = "SINKHOLE"
    ALLOW = "ALLOW"
    RATE_LIMIT = "RATE_LIMIT"

class ScopeType (str, Enum):
    EXACT = "exact"
    SUFFIX = "suffix"
    WILDCARD = "wildcard"

@dataclass
class EnforcementAction:
    action: ActionType
    scope: ScopeType
    value: str
    ttl: int
    confidence: float