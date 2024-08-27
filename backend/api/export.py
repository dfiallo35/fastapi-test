from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import yaml

from main import app


def export_openapi_yaml(app: FastAPI, output_file: str):
    # Generate OpenAPI schema
    openapi_schema = get_openapi(
        title="Your API",
        version="1.0.0",
        description="This is a sample API",
        routes=app.routes,
    )

    # Convert to YAML
    yaml_schema = yaml.dump(openapi_schema, default_flow_style=False)

    # Save to file
    with open(output_file, 'w') as file:
        file.write(yaml_schema)

# Export to 'openapi.yaml'
export_openapi_yaml(app, 'openapi.yaml')