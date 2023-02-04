# Schemas for JSON_PLACE_HOLDER
# Define the schema for each endpoint response
specific_post_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["id", "title", "body"],
}

comments_by_post_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "postId": {"type": "integer"},
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["postId", "id", "name", "email", "body"],
    },
}

all_users_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string"},
        },
        "required": ["id", "name", "username", "email"],
    },
}

specific_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "username", "email"],
}

user_posts_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["userId", "id", "title", "body"],
    },
}

# Schema for DOG_CEO
# Define the schema for each endpoint response
response_schema_image_random = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "status": {
            "type": "string",
            "enum": ["success"]
        },
        "message": {
            "type": "string",
            "format": "uri"
        }
    },
    "required": ["status", "message"],
    "additionalProperties": False
}

response_schema_all = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "message": {
            "type": "object",
            "patternProperties": {
                ".*": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        },
        "status": {
            "type": "string",
            "enum": ["success"]
        }
    },
    "required": ["status", "message"],
    "additionalProperties": False
}

response_schema_list_images = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "message": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "uri"
            }
        },
        "status": {
            "type": "string",
            "enum": ["success"]
        }
    },
    "required": ["status", "message"],
    "additionalProperties": False
}

response_schema_sub_breed = {
    "type": "object",
    "properties": {
        "message": {
            "type": "string",
            "format": "uri"
        },
        "status": {
            "type": "string",
            "enum": ["success"]
        }
    },
    "required": ["message", "status"],
    "additionalProperties": False
}

# Schema for OPENBREW service
# Define the schema for each endpoint response
brewery_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": ["string", "null"]},
            "brewery_type": {"type": ["string", "null"]},
            "street": {"type": ["string", "null"]},
            "city": {"type": ["string", "null"]},
            "state": {"type": ["string", "null"]},
            "postal_code": {"type": ["string", "null"]},
            "country": {"type": ["string", "null"]},
            "longitude": {"type": ["string", "null"]},
            "latitude": {"type": ["string", "null"]},
            "phone": {"type": ["string", "null"]},
            "website_url": {"type": ["string", "null"]},
        },
        "required": [
            "id",
        ],
    }
}
