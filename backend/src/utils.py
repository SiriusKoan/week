from fastapi.responses import JSONResponse


def get_token(auth_header):
    header = auth_header.split(" ")
    if len(header) == 2 and header[0] == "Bearer":
        return header[1]
    return False


def gen_json_response(content, code):
    return JSONResponse({"detail": content}, code)
