# Import packages and connect to a Pinecone vector database.
import os

import warnings

warnings.filterwarnings("ignore")

# Vectorstore Index
index_name = 'podcasts'

api_key = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"

# find environment next to your API key in the Pinecone console
env = os.getenv("PINECONE_ENVIRONMENT") or "PINECONE_ENVIRONMENT"

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="62257ec4-6132-4d43-a6a7-78f453235ba7")

if index_name is not pc.list_indexes():
    pc.create_index(
        name=index_name,
        dimension=1536,  # Replace with your model dimensions
        metric="cosine",  # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-west-2"
        )

    )
