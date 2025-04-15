from fastapi import APIRouter
from openeo import connect


default_backend = "openeo.dataspace.copernicus.eu"

router = APIRouter()

@router.get("/collections")
async def list_collections(backend: str = default_backend):

    connection = connect(url=backend)
    collections = connection.list_collections()

    return collections


@router.get("/collections/{collection_name}")
async def get_collection(collection_name: str, backend: str = default_backend):
    connection = connect(url=backend)
    collection = connection.describe_collection(collection_name)

    return collection