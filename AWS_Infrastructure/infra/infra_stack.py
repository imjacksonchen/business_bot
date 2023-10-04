from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as api_gateway,
)
from constructs import Construct
from dotenv import load_dotenv
import os

load_dotenv()

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Set up Lambda layer
        layer = _lambda.LayerVersion(
            self,
            "BaseLayer",
            code = _lambda.Code.from_asset("lambda_base_layer/layer.zip"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            )
        
        # Set up Lambda function
        api_lambda = _lambda.Function(
            self,
            'ApiFunction',
            runtime = _lambda.Runtime.PYTHON_3_11,
            code = _lambda.Code.from_asset('../python-backend/'),
            handler = "business_bot_api.handler",
            layers = [layer],
            environment = {
                "OPENAI_API_KEY" : os.getenv("OPENAI_API_KEY") or "",
                "SERPAPI_API_KEY" : os.getenv("SERPAPI_API_KEY") or "",
                },
        )

        # Set up the API gateway
        business_bot_api = api_gateway.RestApi(
            self,
            "RestApi",
            rest_api_name = "Business bot API"
        )

        lambda_api_integration = api_gateway.LambdaIntegration(
            api_lambda
        )

        # Set up the connecton between the function and API gateway
        business_bot_api.root.add_proxy(
            default_integration = api_gateway.LambdaIntegration(api_lambda)
        )
