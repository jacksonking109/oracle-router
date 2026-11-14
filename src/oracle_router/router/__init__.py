"""Model router: config-driven adapters for local and hosted models, with budgets."""
from oracle_router.router.adapters import (AdapterError, CommandAdapter, Completion, OllamaAdapter,
                                     OpenAICompatibleAdapter, ScriptedAdapter)
from oracle_router.router.base import ModelRouter, ModelSpec, NullRouter, Proposal, Role, load_model_specs
from oracle_router.router.limits import RateLimited
from oracle_router.router.router import (SUBSCRIPTION_PROVIDERS, BudgetExceeded, Router, backend_key,
                                   make_adapter)

__all__ = ["AdapterError", "BudgetExceeded", "CommandAdapter", "Completion", "ModelRouter",
           "ModelSpec", "NullRouter", "OllamaAdapter", "OpenAICompatibleAdapter", "Proposal", "Role",
           "RateLimited", "Router", "SUBSCRIPTION_PROVIDERS", "ScriptedAdapter", "backend_key", "load_model_specs",
           "make_adapter"]
