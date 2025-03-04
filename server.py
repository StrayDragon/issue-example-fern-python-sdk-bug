from pathlib import Path
from flask import Flask, request, jsonify
import json
import time
import uuid
from flask_swagger_ui import get_swaggerui_blueprint
import yaml
import os

app = Flask(__name__)

# Mock data storage
documents = {}

# Configure Swagger UI
SWAGGER_URL = "/api/docs"
SCHEMA_PATH = "fern/openapi/openapi.yaml"
API_URL = f"/{SCHEMA_PATH}"


# Generate OpenAPI schema
def generate_openapi_schema():
    schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "Document API",
            "description": "API for managing documents in datasets",
            "version": "1.0.0",
        },
        "servers": [
            {"url": "http://localhost:5000", "description": "Local development server"}
        ],
        "paths": {
            "/v1/datasets/{dataset_id}/documents/{document_id}/update-by-file": {
                "post": {
                    "summary": "Update document by file",
                    "description": "Updates a document in a dataset by uploading a file",
                    "operationId": "updateDocumentByFile",
                    "parameters": [
                        {
                            "name": "dataset_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                            "description": "ID of the dataset",
                        },
                        {
                            "name": "document_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                            "description": "ID of the document",
                        },
                        {
                            "name": "Authorization",
                            "in": "header",
                            "required": True,
                            "schema": {"type": "string"},
                            "description": "Bearer {api_key}",
                        },
                    ],
                    "requestBody": {
                        "content": {
                            "multipart/form-data": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "data": {
                                            "type": "object",
                                            "description": "Document configuration JSON as string",
                                            "properties": {
                                                "name": {
                                                    "type": "string",
                                                    "description": "Name of the document",
                                                },
                                                "indexing_technique": {
                                                    "type": "string",
                                                    "description": "Indexing technique to use",
                                                    "enum": ["high_quality"],
                                                },
                                                "process_rule": {
                                                    "type": "object",
                                                    "properties": {
                                                        "mode": {
                                                            "type": "string",
                                                            "enum": ["custom"],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        "file": {
                                            "type": "string",
                                            "format": "binary",
                                            "description": "File to upload",
                                        },
                                    },
                                    "required": ["data", "file"],
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Document updated successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "document": {
                                                "type": "object",
                                                "properties": {
                                                    "id": {"type": "string"},
                                                    "position": {"type": "integer"},
                                                    "data_source_type": {
                                                        "type": "string"
                                                    },
                                                    "data_source_info": {
                                                        "type": "object",
                                                        "properties": {
                                                            "upload_file_id": {
                                                                "type": "string"
                                                            }
                                                        },
                                                    },
                                                    "dataset_process_rule_id": {
                                                        "type": "string"
                                                    },
                                                    "name": {"type": "string"},
                                                    "created_from": {"type": "string"},
                                                    "created_by": {"type": "string"},
                                                    "created_at": {"type": "integer"},
                                                    "tokens": {"type": "integer"},
                                                    "indexing_status": {
                                                        "type": "string"
                                                    },
                                                    "error": {
                                                        "type": "string",
                                                        "nullable": True
                                                    },
                                                    "enabled": {"type": "boolean"},
                                                    "disabled_at": {
                                                        "type": "integer",
                                                        "nullable": True
                                                    },
                                                    "disabled_by": {
                                                        "type": "string",
                                                        "nullable": True
                                                    },
                                                    "archived": {"type": "boolean"},
                                                    "display_status": {
                                                        "type": "string"
                                                    },
                                                    "word_count": {"type": "integer"},
                                                    "hit_count": {"type": "integer"},
                                                    "doc_form": {"type": "string"},
                                                },
                                            },
                                            "batch": {"type": "string"},
                                        },
                                    }
                                }
                            },
                        },
                        "400": {"description": "Invalid request"},
                        "401": {"description": "Unauthorized"},
                    },
                }
            }
        },
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }
        },
        "security": [{"bearerAuth": []}],
    }

    # Write the schema to a YAML file
    with open(SCHEMA_PATH, "w") as f:
        yaml.dump(schema, f, sort_keys=False)

    return schema


# Generate the OpenAPI schema when the app starts
openapi_schema = generate_openapi_schema()


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Document API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route(
    "/v1/datasets/<dataset_id>/documents/<document_id>/update-by-file", methods=["POST"]
)
def update_document_by_file(dataset_id, document_id):
    # Check authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401

    # Extract API key
    api_key = auth_header.split("Bearer ")[1]

    # In a real app, validate the API key here

    # Check if required form data is present
    if "data" not in request.form or "file" not in request.files:
        return jsonify({"error": "Missing required form data"}), 400

    try:
        # Parse the data JSON
        data = json.loads(request.form["data"])

        # Get the uploaded file
        file = request.files["file"]
        file_name = file.filename or "unnamed_file.txt"

        # Create a mock document response
        document_response = {
            "id": document_id or str(uuid.uuid4()),
            "position": 1,
            "data_source_type": "upload_file",
            "data_source_info": {"upload_file_id": str(uuid.uuid4())},
            "dataset_process_rule_id": str(uuid.uuid4()),
            "name": file_name,
            "created_from": "api",
            "created_by": str(uuid.uuid4()),
            "created_at": int(time.time()),
            "tokens": 0,
            "indexing_status": "waiting",
            "error": None,
            "enabled": True,
            "disabled_at": None,
            "disabled_by": None,
            "archived": False,
            "display_status": "queuing",
            "word_count": 0,
            "hit_count": 0,
            "doc_form": "text_model",
        }

        # Store document in memory
        documents[document_id] = document_response

        # Generate batch ID (timestamp format)
        batch_id = time.strftime("%Y%m%d%H%M%S") + str(int(time.time() * 1000))[-6:]

        # Return the response
        return jsonify({"document": document_response, "batch": batch_id})

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in data field"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/openapi.yaml")
def get_openapi():
    return jsonify(openapi_schema)


if __name__ == "__main__":
    app.run(debug=True)
