import requests

BASE_URL = "http://localhost:5000"

def test_home():
    """Test that the home page loads successfully."""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200, f"Unexpected status: {response.status_code}"
    # Check that the HTML response contains the <html> tag (or any other identifier from your index.html)
    assert "<html" in response.text.lower(), "Home page did not return valid HTML."

def test_predict():
    """
    Test the /predict endpoint by sending form data.
    For example, if the model expects 4 features (e.g., for the iris dataset):
    """
    # Prepare sample form data; adjust the keys/values based on your index.html form inputs.
    payload = {
        "Sepal_Length": "5.1",
        "Sepal_Width": "3.5",
        "Petal_Length": "1.4",
        "Petal_Width": "0.2"
    }
    # Since the route reads values from request.form, we pass the data as form data.
    response = requests.post(f"{BASE_URL}/predict", data=payload)
    assert response.status_code == 200, f"Predict endpoint returned {response.status_code}"
    # The response is rendered HTML containing the prediction text.
    # Check that the response includes the expected text.
    assert "The flower species is" in response.text, "Prediction text not found in the response."
