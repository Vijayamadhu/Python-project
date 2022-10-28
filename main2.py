from fastapi import FastAPI,Form,UploadFile,File
import uvicorn
import multipart
from extractor import extract
import uuid
import os
app=FastAPI()



@app.post("/extract_from_doc")
def extract_from_doc(
        file_format:str=Form(...),
        file:UploadFile= File(...),
):
    content = file.file.read()
    file_path="../uploads/"+str(uuid.uuid4()) +".pdf"
    with open(file_path,"wb") as f:
        f.write(content)
    try:
        data=extract(file_path,file_format)
    except Exception as e:
        data={'error':str(e)}
    import os
    if os.path.exists("demofile.pdf"):
        os.remove("demofile.pdf")

    return data
if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=9090)