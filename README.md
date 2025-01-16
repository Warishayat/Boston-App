# House Price Prediction Web App

This project is a **House Price Prediction** model that predicts the price of a house based on several input features, such as the number of rooms, crime rate, property age, and more. The model is built using **Linear Regression** and **StandardScaler** for data preprocessing. The app is deployed as a web application using **Streamlit** on **Hugging Face Spaces**.

## Features
- Predict house prices based on various features like crime rate, number of rooms, property age, and more.
- Interactive user interface created with **Streamlit**.
- Deployed on **Hugging Face Spaces** for easy access.

## Demo

You can access the live demo of the app here:

[**Boston Prediction App**](https://huggingface.co/spaces/Waris01/Boston-Prediciton-App)

## Installation

To run this project locally, you can follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/boston-price-prediction.git
   cd boston-price-prediction
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

5. Navigate to `http://localhost:8501` in your browser to view the app.

## Project Structure

- `app.py`: The main Streamlit app file.
- `regression_model.pkl`: The trained machine learning model.
- `scaler.pkl`: The scaler file for data preprocessing.
- `requirements.txt`: The list of required dependencies for the project.
- `README.md`: This file.

## Dependencies

The following libraries are required to run this project:

- `streamlit`
- `scikit-learn`
- `numpy`
- `scipy`
- `pandas`

You can install all dependencies by running:

```bash
pip install -r requirements.txt
```

## Contributing

Feel free to fork the repository, make changes, and open a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Key Points in This README:
- **Description**: Brief overview of what the project does (House Price Prediction).
- **Demo Link**: Direct link to your **Hugging Face Space**.
- **Installation Instructions**: How to run the project locally, with setup for virtual environment and dependencies.
- **Project Structure**: Information on the project files, such as the main app file, model, and dependencies.
- **Dependencies**: List of required libraries to run the project.
- **Contributing**: Encouragement for others to contribute to the project.
- **License**: Add a license (MIT or others) to clarify the terms of use.

=
