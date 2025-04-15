from openeo import connect
from typing import Optional


def openeo_auth(option: str = "device_flow",
                url_backend: str = "openeo.dataspace.copernicus.eu",
                client_id: Optional[str] = None,
                client_secret: Optional[str] = None):
    if option == "credentials":
        # Use user credentials
        connection = connect(url=url_backend).authenticate_oidc_client_credentials(
            client_id=client_id,
            client_secret=client_secret
        )
    elif option == "device_flow":
        connection = connect(url=url_backend).authenticate_oidc_device()
    else:
        raise ValueError("Invalid authentication option. Use 'credentials' or 'device_flow'.")

    return connection