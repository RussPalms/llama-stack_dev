# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import List

from llama_stack.distribution.datatypes import *  # noqa: F403


def available_providers() -> List[ProviderSpec]:
    return [
        InlineProviderSpec(
            api=Api.evals,
            provider_type="meta-reference",
            pip_packages=[
                "matplotlib",
                "pillow",
                "pandas",
                "scikit-learn",
            ],
            module="llama_stack.providers.impls.meta_reference.evals",
            config_class="llama_stack.providers.impls.meta_reference.evals.MetaReferenceEvalsImplConfig",
            api_dependencies=[
                Api.inference,
            ],
        ),
    ]