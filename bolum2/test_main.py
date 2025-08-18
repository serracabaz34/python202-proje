import json
import httpx
from pathlib import Path
from library import Library, OPENLIB_BASE

def make_client_success(isbn: str, title: str, author_key: str, author_name: str) -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:

        if request.url.path == f"/isbn/{isbn}.json":
            return httpx.Response(200, json={"title": title, "authors": [{"key": author_key}]})
        
        if request.url.path == f"{author_key}.json":
            return httpx.Response(200, json={"name": author_name})
        
        return httpx.Response(404)
    transport = httpx.MockTransport(handler)
    return httpx.Client(transport=transport, base_url=OPENLIB_BASE)

def make_client_404(isbn: str) -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == f"/isbn/{isbn}.json":
            return httpx.Response(404)
        return httpx.Response(404)
    return httpx.Client(transport=httpx.MockTransport(handler), base_url=OPENLIB_BASE)

def make_client_network_error(isbn: str) -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:

        raise httpx.ConnectError("boom", request=request)
    return httpx.Client(transport=httpx.MockTransport(handler), base_url=OPENLIB_BASE)

def test_add_book_success_tmp(tmp_path: Path):
    file = tmp_path / "lib.json"
    client = make_client_success("9780141187761", "Ulysses", "/authors/OL23919A", "James Joyce")
    lib = Library(filename=str(file), client=client)

    ok = lib.add_book("9780141187761")
    assert ok is True
    assert lib.find_book("9780141187761") is not None

    # Control Of Persist
    lib2 = Library(filename=str(file))
    assert lib2.find_book("9780141187761") is not None

def test_add_book_not_found(tmp_path: Path):
    file = tmp_path / "lib.json"
    client = make_client_404("0000000000")
    lib = Library(filename=str(file), client=client)

    ok = lib.add_book("0000000000")
    assert ok is False
    assert lib.find_book("0000000000") is None

def test_add_book_network_error(tmp_path: Path):
    file = tmp_path / "lib.json"
    client = make_client_network_error("1234567890")
    lib = Library(filename=str(file), client=client)

    ok = lib.add_book("1234567890")
    assert ok is False
    assert lib.find_book("1234567890") is None