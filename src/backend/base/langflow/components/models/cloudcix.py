from openai import OpenAI
from langchain_openai import ChatOpenAI

from langflow.base.models.cloudcix_constants import CLOUDCIX_MODEL_NAMES, CLOUDCIX_BASE_URL
from langflow.base.models.model import LCModelComponent
from langflow.inputs import BoolInput, SliderInput, SecretStrInput, IntInput, DropdownInput
from langflow.field_typing import LanguageModel
from langflow.field_typing.range_spec import RangeSpec

class CloudCIXModelComponent(LCModelComponent):
    display_name = "CloudCIX"
    description = "Generate text using CloudCIX LLMs."
    name = "CloudCIXModel"
    icon = "CloudCIX"

    inputs = [
        SecretStrInput(
            name="api_key",
            display_name="API Key",
            info="Enter your CloudCIX API Key."
        ),
        DropdownInput(
            name="model_name",
            display_name="Model Name",
            options=CLOUDCIX_MODEL_NAMES,
            refresh_button=True,
            real_time_refresh=True,
        ),
        IntInput(
            name="max_tokens",
            display_name="Max Tokens",
        ),
        SliderInput(
            name="temperature",
            display_name="Temperature",
            value=0.1,
            range_spec=RangeSpec(min=0, max=1, step=0.01),
        ),
        BoolInput(
            name="json_mode",
            display_name="JSON Mode",
            advanced=True,
            info="If True, it will output JSON regardless of passing a schema.",
        ),
        *LCModelComponent._base_inputs,
    ]

    def build_model(self) -> LanguageModel:        
        api_key = self.api_key
        temperature = self.temperature
        model_name = self.model_name
        max_tokens = self.max_tokens
        json_mode = self.json_mode

        output = ChatOpenAI(
            max_tokens=max_tokens or None,
            model=model_name,
            base_url=CLOUDCIX_BASE_URL,
            api_key=api_key,
            temperature=temperature if temperature is not None else 0.1,
        )
        if json_mode:
            output = output.bind(response_format={"type": "json_object"})

        return output
