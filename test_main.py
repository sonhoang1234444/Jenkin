from fastapi.testclient import TestClient
from main import app  # Import ứng dụng FastAPI từ file main.py

# Tạo client để gửi yêu cầu đến API
client = TestClient(app)

# 1. Test endpoint /get_version
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0"}

# 2. Test /check_prime với số nguyên tố
def test_check_prime_with_prime():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

# 3. Test /check_prime với số không phải nguyên tố
def test_check_prime_with_non_prime():
    response = client.get("/check_prime/8")
    assert response.status_code == 200
    assert response.json() == {"number": 8, "is_prime": False}

# 4. Test /check_prime với trường hợp đặc biệt (1 không phải số nguyên tố)
def test_check_prime_with_one():
    response = client.get("/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}

# 5. Test /check_prime với số nguyên tố lớn
def test_check_prime_with_large_prime():
    response = client.get("/check_prime/101")
    assert response.status_code == 200
    assert response.json() == {"number": 101, "is_prime": True}

# 6. Test /check_prime với số không phải nguyên tố lớn
def test_check_prime_with_large_non_prime():
    response = client.get("/check_prime/100")
    assert response.status_code == 200
    assert response.json() == {"number": 100, "is_prime": False}

# 7. Test /check_prime với số âm
def test_check_prime_with_negative():
    response = client.get("/check_prime/-7")
    assert response.status_code == 200
    assert response.json() == {"number": -7, "is_prime": False}

# 8. Test /check_prime với input không hợp lệ
def test_check_prime_with_invalid_input():
    response = client.get("/check_prime/abc")
    assert response.status_code == 422  # HTTP 422: Unprocessable Entity

# 9. Test một số nguyên tố khác cho /check_prime
def test_check_prime_with_another_prime():
    response = client.get("/check_prime/13")
    assert response.status_code == 200
    assert response.json() == {"number": 13, "is_prime": True}

# 10. Test một số không phải nguyên tố khác cho /check_prime
def test_check_prime_with_another_non_prime():
    response = client.get("/check_prime/15")
    assert response.status_code == 200
    assert response.json() == {"number": 15, "is_prime": False}
