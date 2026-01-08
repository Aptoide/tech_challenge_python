from pydantic import BaseModel
from typing import Optional

class AppResponse(BaseModel):
    #Schema de resposta da API
    name: str
    size: str
    downloads: str
    version: str
    release_date: str
    min_screen: str
    supported_cpu: str
    package_id: str
    sha1_signature: str
    developer_cn: str
    organization: str
    local: str
    country: str
    state_city: str

    class Config:
        json_schema_extra = {
            "example":{
                "name": "Facebook",
                "size": "152.5 MB",
                "downloads": "2B",
                "version": "532.0.0.55.71",
                "release_date": "2025-09-30 17:06:59",
                "min_screen": "SMALL",
                "supported_cpu": "arm64-v8a",
                "package_id": "com.facebook.katana",
                "sha1_signature": "8A:3C:4B:26:2D:72:1A:CD:49:A4:BF:97:D5:21:31:99:C8:6F:A2:B9",
                "developer_cn": "Facebook Corporation",
                "organization": "Facebook Mobile",
                "local": "Palo Alto",
                "country": "US",
                "state_city": "CA"
        }
    }