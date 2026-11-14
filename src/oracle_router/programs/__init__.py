"""Declarative cipher programs proposed by generators and run by deterministic code."""
from oracle_router.programs.sequences import SEQUENCES
from oracle_router.programs.spec import (SpecError, canonical, compile_spec, decrypt, describe, encrypt,
                                   expand, expand_iter, expansion_size, roundtrips, spec_hash, with_offset)

__all__ = ["SEQUENCES", "SpecError", "canonical", "compile_spec", "decrypt", "describe", "encrypt", "expand",
           "expand_iter", "expansion_size", "roundtrips", "spec_hash", "with_offset"]
