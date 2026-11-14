"""Phase 3: model-driven hypothesis generation over cipher programs."""
from oracle_router.swarm.generators import (Feedback, GenContext, LLMGenerator, ModelRanker,
                                      RandomProgramGenerator, RawProposal, build_prompt,
                                      parse_proposals)
from oracle_router.swarm.loop import GeneratorStats, SwarmConfig, SwarmResult, run_swarm

__all__ = ["Feedback", "GenContext", "GeneratorStats", "LLMGenerator", "ModelRanker",
           "RandomProgramGenerator", "RawProposal", "SwarmConfig", "SwarmResult", "build_prompt",
           "parse_proposals", "run_swarm"]
