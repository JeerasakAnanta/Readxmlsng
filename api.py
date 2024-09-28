from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class ReadXmlSngResponse(BaseModel):
    message: str 

@app.post("/read_xml_sgn", response_model=ReadXmlSngResponse)
async def read_xml_sgn(file_path: str) -> ReadXmlSngResponse:
    """
    Read an XML file and return its content.

    Args:
    - file_path: The path to the XML file to be read.

    Returns:
    - A ReadXmlSngResponse object with the message being the content of the
      XML file.
    """
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Read the content of the file
        xml_content = file.read()
  
    # Return the content of the file as a string
    return {"message": f"{xml_content}"}

@app.get("/")
async def root() -> dict[str, str]:
    """
    This endpoint simply returns a message indicating that FastAPI is running.

    Returns:
    - A dictionary with a single key "message" and a value of "FastAPI is running".
    """
    return {"message": "FastAPI is running"}

